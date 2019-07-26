"""Linear demand.actuator with heating and cooling days."""
import logging
import numpy as np
import pandas as pd
import xarray as xr
from sklearn import linear_model
from sklearn.model_selection import KFold, GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin, clone
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score
from sklearn.exceptions import NotFittedError
from ..data_source import Composer
from ..actuator_base import FeatureExtractorBase, EstimatorBase

#: Logger.
log = logging.getLogger(__name__)


class Actuator(FeatureExtractorBase, EstimatorBase):
    def __init__(self, output_variable, cfg=None, **kwargs):
        """Naming constructor.

        :param output_variable: Output variable to estimate. Default is `None`,
          in which case implementations of this class should set
          :py:attr:`out_var_name`.
        :param cfg: Actuator configuration. Default is `None`.
        :type output_variable: :py:class:`OutputVariable`
        :type cfg: dict
        """
        name = 'demand_heat_cool_linear'
        default_output_variable = 'demand'
        if output_variable.name != default_output_variable:
            log.warning(
                'Output variable {} given to constructor does not correspond '
                'to {} output variable to be estimated by {}'.format(
                    output_variable.name, default_output_variable,
                    self.name))

        super(Actuator, self).__init__(
            output_variable=output_variable, name=name, cfg=cfg,
            **kwargs)

        self.coef = {
            'daily_cycle_mean': None, 'regressor': None,
            'r2': None, 't_heat': None, 't_cool': None, 'alpha': None}

        #: Climate-variable name.
        self.clim_var = 'surface_temperature'
        #: Calendar-variable name.
        self.cal_var = 'calendar'

    def transform(self, multi_data_src, stage=None, **kwargs):
        """Format temperature data from climate dataset.

        :param multi_data_src: Input multiple data source containing climate
          and calendar data.
        :param stage: Modeling stage: `'fit'` or `'predict'`.
          May be required if features differ in the prediction stage.
        :type multidata_src: :py:class:`..data_source.MultiDataSource`
        :type stage: str

        :returns: Merged dataset.
        :rtype: :py:class:`xarray.Dataset`
        """
        clim_data_src = multi_data_src.get_data_source(self.clim_var)
        cal_data_src = multi_data_src.get_data_source(self.cal_var)

        # Load climate data
        # Add regions domain cropping
        functions = [clim_data_src.crop_area]

        if hasattr(self.output_variable, 'modifier'):
            if (hasattr(self.output_variable.modifier.cfg, 'stage') and
                    (self.output_variable.modifier.cfg['stage'] != stage)):
                pass
            else:
                # Add modifier transformation
                functions.append(self.output_variable.modifier.apply)

        # Add get regional mean
        functions.append(clim_data_src.get_regional_mean)

        # Get temperature feature
        composer = Composer(*functions)

        ds_clim = clim_data_src.load(
            transform=composer, variables=self.clim_var)

        # Convert from Kelvin to Celsius
        ds_clim[self.clim_var] -= 273.15

        # Re-sample the climate data, if needed
        freq_data = ds_clim.indexes['time'].inferred_freq.upper()
        if ((freq_data in ['H', '1H']) and
                (self.med.cfg['frequency'] == 'day')):
            if not self.cfg.get('no_verbose'):
                log.info(
                    'Averaging the climate data from hourly to daily values.')
            ds_clim = ds_clim.resample(time='D').mean(
                'time', keep_attrs=True)
        elif ((freq_data in ['D', '1D']) and
              (self.med.cfg['frequency'] == 'hour')):
            if not self.cfg.get('no_verbose'):
                log.info(
                    'Upsampling climate data from daily to hourly values')
            end_time = ds_clim.indexes['time'][-1] + pd.Timedelta(23, unit='H')
            th = pd.date_range(
                start=ds_clim.indexes['time'][0], end=end_time, freq='H')
            ds_clim = ds_clim.reindex(time=th).ffill('time')

        # Load calendar consistent with climate dataset
        ds_cal = cal_data_src.load(ds_clim.indexes['time'])

        # Return datasets merge
        return xr.merge([ds_clim, ds_cal])

    def fit(self, data_src_in, data_src_out, **kwargs):
        """Learn statistical model of temperature-dependent demand
        and predict demand.

        :param data_src_in: Temperature and calendar dataset of training set.
        :param data_src_out: Demand dataset of training set.
        :type data_src_in: :py:class:`..data_source.DataSource`
        :type data_src_out: :py:class:`..data_source.DataSource`

        .. note::
          * This function uses grid search with k-fold cross validation to
            find the best heating/cooling temperature thresholds and
            regularization parameter.
          * These hyper-parameters are the same for all regions,
            so that the model has multiple outputs (one for each region)
            and the score for the cross valideation is given by the
            sum of the individual coefficients of determination for each region
            weighted by the fraction of the total variance explained by each
            region.
          * The feature matrix of the demand model is computed by calling the
            `fit` member function of the class
            :py:class:`DemandFeatureHeatCoolDays`, which itself calls
            the function :py:func:`get_demand_feature_heat_cool_days`.

        """
        # Get common time slice for demand and temperature data
        temp = data_src_in[self.clim_var]
        demand = data_src_out[self.output_variable.name]
        common_index = demand.indexes['time']
        common_index = common_index.intersection(temp.indexes['time'])
        time_slice = slice(common_index[0], common_index[-1])

        # Select time slice
        if not self.cfg.get('no_verbose'):
            log.info('Selecting data from {} to {}'.format(
                time_slice.start, time_slice.stop))
        temp = temp.sel(time=time_slice).expand_dims(
            'variable').assign_coords(variable=[self.clim_var])
        demand = demand.sel(time=time_slice).transpose('time', 'region')
        cal = data_src_in.data[self.cal_var].sel(time=time_slice)
        # Get daily cycle mean
        if self.med.cfg['frequency'] == 'hour':
            self.coef['daily_cycle_mean'] = get_daily_cycle(demand, cal)

        # Apply daily_cycle (pre-fit)
        daily_cycle_series = apply_daily_cycle(
            cal, self.coef.get('daily_cycle_mean'), self.med.cfg['frequency'])
        daytype_index = daily_cycle_series.indexes['variable']

        # Concatenate output_variables and make sure dimensions in right order
        _, daily_cycle_series = xr.broadcast(
            temp, daily_cycle_series, exclude=['time', 'variable'])
        des_mat_cycle = xr.concat(
            [temp, daily_cycle_series], dim='variable').transpose(
                'time', 'variable', 'region')

        # Cross-validation configuration
        if 'n_splits' in self.cfg:
            n_splits = self.cfg['n_splits']
        else:
            years = des_mat_cycle.indexes['time'].year
            n_splits = years[-1] - years[0] + 1
        # cv = TimeSeriesSplit(n_splits=self.cfg['n_splits'])
        cv = KFold(n_splits=n_splits)
        # scoring = 'neg_mean_squared_error'

        # Heating and cooling temperature grid
        t_heat_grid = np.arange(self.cfg['t_heat']['start'],
                                self.cfg['t_heat']['stop'],
                                self.cfg['t_heat']['step'])
        t_cool_grid = np.arange(self.cfg['t_cool']['start'],
                                self.cfg['t_cool']['stop'],
                                self.cfg['t_cool']['step'])

        # Estimator
        grid = {'feature__t_heat':  t_heat_grid,
                'feature__t_cool': t_cool_grid}
        params = {'fit_intercept': False, 'normalize': True}
        if 'max_iter' in self.cfg:
            params['max_iter'] = self.cfg['max_iter']
        if ((self.cfg['method'] == 'Ridge')
                | (self.cfg['method'] == 'Lasso')):
            alpha_grid = np.logspace(self.cfg['alpha']['start'],
                                     self.cfg['alpha']['stop'],
                                     self.cfg['alpha']['num'])
            grid.update({'regressor__estimator__alpha': alpha_grid})
            if self.cfg['method'] == 'Ridge':
                estimator = linear_model.Ridge(**params)
            elif self.cfg['method'] == 'Lasso':
                estimator = linear_model.Lasso(**params)
        elif self.cfg['method'] == 'BayesianRidge':
            estimator = linear_model.BayesianRidge(**params)

        # Make grid estimator
        feature = DemandFeatureHeatCoolDays(daytype_index=daytype_index,
                                            temp_label=self.clim_var)
        regressor = MultiInputRegressor(estimator)
        pipe = Pipeline(steps=[('feature', feature), ('regressor', regressor)])
        grid_cv = GridSearchCV(pipe, grid, cv=cv, verbose=0)

        # Fit model
        if not self.cfg.get('no_verbose'):
            log.info('Fitting model by {}'.format(self.cfg['method']))
        grid_cv.fit(des_mat_cycle, demand.values)
        self.coef['regressor'], self.coef['r2'] = (
            grid_cv.best_estimator_, grid_cv.best_score_)

        # Get parameters of best model
        params = self.coef['regressor'].get_params()
        self.coef['t_heat'], self.coef['t_cool'] = (
            params['feature__t_heat'], params['feature__t_cool'])
        if self.cfg['method'] != 'BayesianRidge':
            self.coef['alpha'] = params['regressor__estimator__alpha']

        # Print parameters and scores
        if not self.cfg.get('no_verbose'):
            log.info('Best overall score: {:.2f}'.format(self.coef['r2']))
            log.info('Heating temperature: {:.1f}'.format(
                self.coef['t_heat']))
            log.info('Cooling temperature: {:.1f}'.format(
                self.coef['t_cool']))
            if self.cfg['method'] != 'BayesianRidge':
                log.info('Regularization coefficient: {:.1f}'.format(
                    self.coef['alpha']))

    def predict(self, data_src_in, **kwargs):
        """Get regional demand prediction from fitted model.

        :param data_src_in: Input data-source for prediction.
        :type data_src_in: :py:class:`..data_source.DataSource`

        :returns: Prediction dataset.
        :rtype: :py:class:`xarray.Dataset`
        """
        if self.coef['r2'] is None:
            raise NotFittedError(
                'This demand estimator instance has not been fitted yet')

        # Apply daily_cycle
        daily_cycle_series = apply_daily_cycle(
            data_src_in[self.cal_var], self.coef.get('daily_cycle_mean'),
            self.med.cfg['frequency'])

        # Aggregate into an array of feature
        temp = data_src_in[self.clim_var].expand_dims(
            'variable').assign_coords(variable=[self.clim_var])
        _, daily_cycle_series = xr.broadcast(
            temp, daily_cycle_series, exclude=['time', 'variable'])
        des_mat_cycle = xr.concat(
            [temp, daily_cycle_series], dim='variable')

        # Predict
        kwargs = ({'return_std': True} if self.cfg['method'] == 'BayesianRidge'
                  else {})
        pred = self.coef['regressor'].predict(des_mat_cycle, **kwargs)

        # Collect regional demand prediction
        ds_pred = xr.Dataset()
        coords = dict(des_mat_cycle.coords)
        coord_reg = ('region', des_mat_cycle.coords['region'])
        coord_time = ('time', coords['time'])
        if self.cfg['method'] == 'BayesianRidge':
            y_mean, y_std = pred
            # Add random perturbations to prediction drawn from
            # posterior distribution
            if self.med.cfg['frequency'] == 'hour':
                # Constant perturbations throughout the day
                y_pert_day = np.random.normal(loc=0., scale=y_std[::24])
                y_pert = np.empty(y_mean.shape)
                for ih in range(24):
                    y_pert[ih::24] = y_pert_day
            elif self.med.cfg['frequency'] == 'day':
                y_pert = np.random.normal(loc=0., scale=y_std)
            prediction = y_mean + y_pert

            # Add mean, standard deviation, alpha and lambda
            # y_mean = xr.DataArray(y_mean, coords=[coord_time, coord_reg],
            #                       name='demand_mean')
            y_std = xr.DataArray(y_std, coords=[coord_time, coord_reg],
                                 name='demand_std')
        else:
            prediction = pred

        # Add prediction
        prediction = xr.DataArray(prediction, coords=[coord_time, coord_reg])
        prediction.attrs['r2_total'] = self.coef['r2']
        prediction.attrs['t_heat'] = self.coef['t_heat']
        prediction.attrs['t_cool'] = self.coef['t_cool']
        if self.cfg['method'] != 'BayesianRidge':
            prediction.attrs['alpha'] = self.coef['alpha']

        # Add units
        if self.med.cfg['frequency'] == 'day':
            prediction.attrs['units'] = 'MWh/d'
        elif self.med.cfg['frequency'] == 'hour':
            prediction.attrs['units'] = 'MWh/h'
        ds_pred[self.output_variable.name] = prediction

        np.set_printoptions(precision=1)
        temp = des_mat_cycle.loc[{'variable': self.clim_var}]
        val = prediction.mean('time').values * 365 / 1e6
        if not self.cfg.get('no_verbose'):
            log.info('Total fitted demand mean (TWh/y): {}'.format(val))
            if self.cfg['method'] == 'BayesianRidge':
                y_std *= 365 / 1e6
                val = np.sqrt((y_std**2).mean('time').values)
                log.info('Total fitted demand std (TWh/y): {}'.format(val))
            # Get number of heating and cooling days
            n_heating_days = (temp < self.coef['t_heat']).mean(
                'time').values * 365
            n_cooling_days = (temp > self.coef['t_cool']).mean(
                'time').values * 365
            log.info('Number of heating days per year: {}'.format(
                n_heating_days))
            log.info('Number of cooling days per year: {}'.format(
                n_cooling_days))

        return ds_pred

    def get_feature_extractor_postfix(self, **kwargs):
        """Get postfix corresponding to wind features.

        returns: Postfix.
        rtype: str
        """
        postfix = '{}_{}'.format(
            super(Actuator, self).get_feature_extractor_postfix(**kwargs),
            self.med.cfg['frequency'])

        if hasattr(self.output_variable, 'modifier'):
            postfix += (self.output_variable.modifier.
                        get_modifier_postfix(**kwargs))

        return postfix

    def get_estimator_postfix(self, **kwargs):
        """Get estimator postfix.

        returns: Postfix.
        rtype: str
        """
        return '{}_{}'.format(
            super(Actuator, self).get_estimator_postfix(**kwargs),
            self.cfg['method'])


def get_demand_feature_heat_cool_days(
        des_mat, daytype_index, t_heat, t_cool,
        temp_label='surface_temperature'):
    """Get feature matrix of demand model with as variables heating
    and cooling temperature ramps and as factors week-days types.

    :param des_mat: Array containing climatic variables, i.e.
        mean temperature(Celsius),
        and membership of days to types 'work', 'sat' and 'off'
        (possibly including a daily cycle).
    :param daytype_index: Daytype index.
    :param t_heat: Temperature threshold below which consumers
        turn on heating.
    :param t_cool: Temperature threshold above which consumers
        turn on air conditionning.
    :param temp_label: Label of surface temperature variable.
        Default is `surface_temperature`.
    :type des_mat: py:class:`xarray.DataArray`
    :type daytype_index: sequence
    :type t_heat: float
    :type t_cool: float
    :type temp_label: str

    :returns: Feature matrix.
    :rtype: :py:class:`xarray.DataArray`
    """
    # Get variable labels
    piece_name = ['one', 'heat', 'cool']
    variables = np.concatenate(
        [[['{}_{}'.format(v, day)] for v in piece_name]
         for day in daytype_index])[:, 0]

    # Build feature array
    coords = dict(des_mat.coords.items())  # Copy dictionary of coordinates
    # Update variable coordinate
    coords['variable'] = variables
    coords = [(dim, coords[dim]) for dim in des_mat.dims]
    shape = [len(coord[1]) for coord in coords]
    feature = xr.DataArray(np.zeros(shape), coords=coords,
                           name='demand_feature_heat_cool_days')

    # Select temperature
    z = des_mat.sel(variable=temp_label, drop=True)

    for day in daytype_index:
        # Day type mask
        id_day = des_mat.sel(variable=day, drop=True)

        # Intercept for each
        feature.loc[{'variable': 'one_{}'.format(day)}] = id_day

        # Heating temperature
        feature.loc[{'variable': 'heat_{}'.format(day)}] = (
            (t_heat - z) * np.heaviside(t_heat - z, 0.)) * id_day
        # (z < t_heat).astype(float))

        # Cooling temperature
        feature.loc[{'variable': 'cool_{}'.format(day)}] = (
            (z - t_cool) * np.heaviside(z - t_cool, 0.)) * id_day
        # (z > t_cool).astype(float)

    # Transpose with regions (outputs) as last dimension
    feature = feature.transpose('time', 'variable', 'region')

    return feature


class DemandFeatureHeatCoolDays(BaseEstimator, TransformerMixin):
    """Class given to a scikit-learn pipeline to extract feature
    of the piecewise-linear_model of demand as a function of
    temperature and type of days."""

    def __init__(self, daytype_index, t_heat=12., t_cool=18.,
                 temp_label='surface_temperature'):
        """Constructor.

        :param daytype_index: Day-type index.
        :param t_heat: Heating-temperature threshold. Default is `12.`.
        :param t_cool: Cooling-temperature threshold. Default is `12.`.
        :param temp_label: Temperature-variable name.
        :type daytype_index: sequence
        :type t_heat: float
        :type t_cool: float
        :type temp_label: str
        """
        #: Heating-temperature threshold.
        self.t_heat = t_heat

        #: Cooling-temperature threshold.
        self.t_cool = t_cool

        #: Temperature-variable name.
        self.temp_label = temp_label

        #: Day-type index.
        self.daytype_index = daytype_index

    def fit(self, des_mat, y=None):
        """Fit doing nothing."""
        return self

    def transform(self, des_mat):
        """Transform by calling :py:func:`get_demand_feature_heat_cool_days`.

        :param des_mat: Design matrix.
        :type des_mat: :py:class:`xarray.DataArray`

        :returns: Feature matrix.
        :rtype: :py:class:`xarray.DataArray`
        """
        return get_demand_feature_heat_cool_days(
            des_mat, self.daytype_index, self.t_heat, self.t_cool,
            temp_label=self.temp_label)


class MultiInputRegressor(BaseEstimator):
    """Multi input estimator.

    :param estimator: An estimator implementing `fit` and `predict`.
    :type estimator: estimator object
    """

    def __init__(self, estimator):
        #: Base estimator.
        self.estimator = estimator
        #: Multiple estimators.
        self.estimators = None
        #: Scores for each estimator.
        self.scores = None

    def fit(self, des_mat, out):
        """Fit model to data.
        Fit a separate model for each input and output variables.

        :param des_mat: Input array,
            shape(n_samples, n_feature, n_outputs).
        :param out: Output array, shape(n_samples, n_outputs)
        :type des_mat: array_like
        :type out: array_like

        :returns: :py:obj:self
        :rtype: :py:class:`RegionalEstimator`
        """
        # Loop over inputs and outputs
        self.estimators = []
        for ie in np.arange(des_mat.shape[2]):
            # Clone estimator
            e = clone(self.estimator)

            # Select data
            des_mat_l, out_l = des_mat[:, :, ie], out[:, ie]

            # Fit data
            e.fit(des_mat_l, out_l)

            # Save estimator
            self.estimators.append(e)

        # Save number of estimators
        self.n_estimators = len(self.estimators)

        return self

    def predict(self, des_mat, return_std=False):
        """Predict multi-output variable using a model
            trained for each target variable.

        :param des_mat: Input data, shape(n_samples, n_feature, n_outputs).
        :param return_std: If `True`, return standard deviation
           of posterior prediction(in the Bayesian case).
           Default is `False`.
        :type des_mat: array_like
        :type return_std: bool
        """
        y_pred = np.empty((des_mat.shape[0], des_mat.shape[2]))
        if return_std:
            y_std = np.empty((des_mat.shape[0], des_mat.shape[2]))
        for ie in range(des_mat.shape[2]):
            # Select data
            des_mat_l = des_mat[:, :, ie]

            # Manage return std for Bayesian case only
            kwargs = {'return_std': True} if return_std else {}

            # Predict
            pred = self.estimators[ie].predict(des_mat_l, **kwargs)

            # Manage prediction result
            if return_std:
                y_pred[:, ie] = pred[0]
                y_std[:, ie] = pred[1]
            else:
                y_pred[:, ie] = pred
        if return_std:
            return (y_pred, y_std)
        else:
            return y_pred

    def score(self, des_mat, out):
        """Compute individual scores and variance-weighted score
        of multiple-output prediction.
        :param des_mat: Input data, shape(n_samples, n_feature, n_outputs).
        :param out: True target data, shape(n_samples, n_outputs).
        :type des_mat: array_like
        :type out: array_like

        :returns: Variance-weighted score.
        :rtype: float

        .. note:: Individual scores are saved in :py:attr:`scores`.
        """
        # Predict
        out_pred = self.predict(des_mat)

        # Save raw scores
        self.scores = r2_score(out, out_pred, multioutput='raw_values')

        # Return variance weighted score
        score = (self.scores * out.var(0)).sum() / out.var(0).sum()

        return score


def get_daily_cycle(demand, calendar):
    """Build an array of complementary columns corresponding
    to each day type of the calendar.
    Non-zero values are given by a composite hourly cycle given by
    the average of demand over all samples of same day type and hour.

    :param demand: Demand array.
    :param calendar: Calendar array.
    :type demand: :py:class:`xarray.DataArray`
    :type calendar: :py:class:`xarray.DataArray`

    :returns: Array with each column corresponding to a day type.
    :rtype: :py:class:`xarray.DataArray`
    """
    # Group by day type, and hour if needed
    hours = calendar.indexes['time'].hour
    hours.name = 'hour'
    demand.coords['daytype_hour'] = (
        'time', pd.MultiIndex.from_arrays([calendar, hours]))
    gp_daily_cycle = demand.groupby('daytype_hour')

    # Get time-mean daily cycle per day type
    daily_cycle_mean = gp_daily_cycle.mean('time')

    return daily_cycle_mean


def apply_daily_cycle(calendar, daily_cycle_mean=None, frequency='day'):
    """Build an array of complementary columns corresponding
    to each day type of the calendar. If frequency is `'day'`,
    non-zero values are unitary, else, if frequency is `'hour'`,
    non-zero values are given by a composite hourly cycle given by
    the average of demand over all samples of same day type and hour.

    :param calendar: Calendar array.
    :param daily_cycle_mean: Mean daily cycle of output data.
      Default is `None`.
    :param frequency: Sampling frequency as either `'day'` or `'hour'`.
       Default is `'day'`.
    :type calendar: :py:class:`xarray.DataArray`
    :type daily_cycle_mean: :py:class:`xarray.DataArray`
    :type frequency: str

    :returns: An array with each column corresponding to a day type.
    :rtype: :py:class:`xarray.DataArray`
    """
    # Initialize cycle
    time = calendar.indexes['time']
    daytype_index = np.unique(calendar)
    coords = [('time', time), ('variable', daytype_index)]
    daily_cycle_series = xr.DataArray(
        np.zeros((len(time), len(daytype_index))), coords=coords)

    # Group by day type, and hour if needed
    if frequency == 'hour':
        hours = time.hour
        hours.name = 'hour'
        grouper = 'daytype_hour'
        group_index = pd.MultiIndex.from_arrays([calendar, hours])
        daily_cycle_series.coords[grouper] = ('time', group_index)

        # Group calendar by daytype and hours
        gp_out = daily_cycle_series.groupby(grouper)

        # Fill cycle with composite
        daily_cycle_series = gp_out + daily_cycle_mean

        # Drop group variable
        daily_cycle_series = daily_cycle_series.drop(grouper)
    elif frequency == 'day':
        # Group calendar by daytype
        gp_out = daily_cycle_series.groupby(calendar)
        for gp_key, gp_idx in gp_out.groups.items():
            daily_cycle_series.loc[{'variable': gp_key}][gp_idx] = 1

    return daily_cycle_series
