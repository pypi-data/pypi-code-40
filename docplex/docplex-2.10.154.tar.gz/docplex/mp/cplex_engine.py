# --------------------------------------------------------------------------
# Source file provided under Apache License, Version 2.0, January 2004,
# http://www.apache.org/licenses/
# (c) Copyright IBM Corp. 2015, 2016
# --------------------------------------------------------------------------

import sys

from collections import defaultdict

from docplex.mp.engine import DummyEngine
from docplex.mp.utils import DOcplexException, str_holo, iter_one
from docplex.mp.compat23 import izip

from docplex.mp.constants import ConflictStatus
from docplex.mp.constr import IndicatorConstraint, QuadraticConstraint, LinearConstraint, RangeConstraint, BinaryConstraint, \
    EquivalenceConstraint
from docplex.mp.progress import ProgressData
from docplex.mp.solution import SolveSolution
from docplex.mp.sdetails import SolveDetails
from docplex.mp.conflict_refiner import TConflictConstraint, VarLbConstraintWrapper, VarUbConstraintWrapper
import cplex

import six
from contextlib import contextmanager

import numbers
from enum import Enum
import re

# CHECK THIS
# noinspection PyProtectedMember
from cplex._internal import _subinterfaces
from cplex.callbacks import MIPInfoCallback

# noinspection PyProtectedMember
import cplex._internal._constants as cpx_cst
from cplex._internal._procedural import chgcoeflist, chgobj, chgrhs, chgqpcoef, newcols, setintparam, \
    addindconstr, addrows, chgrngval, addpwl, getnumpwl, chgcolname, getx
from cplex._internal._subinterfaces import IndicatorConstraintInterface
from cplex.exceptions import CplexError, CplexSolverError
try:
    # from 12.9 up
    from cplex._internal._procedural import multiobjsetobj
    DEFAULT_CPX_NO_WEIGHT_CHANGE = cpx_cst.CPX_NO_WEIGHT_CHANGE
    DEFAULT_CPX_NO_PRIORITY_CHANGE = cpx_cst.CPX_NO_PRIORITY_CHANGE
    DEFAULT_CPX_NO_ABSTOL_CHANGE = cpx_cst.CPX_NO_ABSTOL_CHANGE
    DEFAULT_CPX_NO_RELTOL_CHANGE = cpx_cst.CPX_NO_RELTOL_CHANGE

    DEFAULT_CPX_STAT_MULTIOBJ_OPTIMAL = cpx_cst.CPX_STAT_MULTIOBJ_OPTIMAL
    DEFAULT_CPX_STAT_MULTIOBJ_INForUNBD = cpx_cst.CPX_STAT_MULTIOBJ_INForUNBD
    DEFAULT_CPX_STAT_MULTIOBJ_UNBOUNDED = cpx_cst.CPX_STAT_MULTIOBJ_UNBOUNDED
    DEFAULT_CPX_STAT_MULTIOBJ_INFEASIBLE = cpx_cst.CPX_STAT_MULTIOBJ_INFEASIBLE
    DEFAULT_CPX_STAT_MULTIOBJ_NON_OPTIMAL = cpx_cst.CPX_STAT_MULTIOBJ_NON_OPTIMAL
    DEFAULT_CPX_STAT_MULTIOBJ_STOPPED = cpx_cst.CPX_STAT_MULTIOBJ_STOPPED

except ImportError:
    multiobjsetobj = None
    DEFAULT_CPX_NO_WEIGHT_CHANGE = None
    DEFAULT_CPX_NO_PRIORITY_CHANGE = None
    DEFAULT_CPX_NO_ABSTOL_CHANGE = None
    DEFAULT_CPX_NO_RELTOL_CHANGE = None

    DEFAULT_CPX_STAT_MULTIOBJ_OPTIMAL = None
    DEFAULT_CPX_STAT_MULTIOBJ_INForUNBD = None
    DEFAULT_CPX_STAT_MULTIOBJ_UNBOUNDED = None
    DEFAULT_CPX_STAT_MULTIOBJ_INFEASIBLE = None
    DEFAULT_CPX_STAT_MULTIOBJ_NON_OPTIMAL = None
    DEFAULT_CPX_STAT_MULTIOBJ_STOPPED = None

try:
    # from 12.7.1 up
    from cplex._internal._procedural import chbmatrix
except ImportError:  # pragma: no cover
    # up to 12.7.0
    try:
        from cplex._internal._matrices import chbmatrix
    except ImportError:
        chbmatrix = None


from docplex.mp.compat23 import fast_range, copyreg
# noinspection PyPep8Namingc
from docplex.mp.constants import QualityMetric, UpdateEvent as upd

from docplex.mp.environment import Environment
from docplex.mp.engine import NoSolveEngine

try:
    from cplex._internal._pwl import PWLConstraintInterface
except ImportError:  # pragma: no cover
    PWLConstraintInterface = None

try:
    cpx_indicator_type_ifthen = cpx_cst.CPX_INDICATOR_IF
    cpx_indicator_type_equiv = cpx_cst.CPX_INDICATOR_IFANDONLYIF
except AttributeError:  # pragma: no cover
    # handle previous versions without indicator type
    cpx_indicator_type_ifthen = None
    cpx_indicator_type_equiv = None

# -- build annotation map if possible

from docplex.mp.constants import CplexScope

try:
    from cplex._internal._procedural import setlonganno
    from cplex._internal._anno import LongAnnotationInterface

    annotation_map = {CplexScope.VAR_SCOPE: cpx_cst.CPX_ANNOTATIONOBJ_COL,
                      CplexScope.LINEAR_CT_SCOPE: cpx_cst.CPX_ANNOTATIONOBJ_ROW,
                      CplexScope.IND_CT_SCOPE: cpx_cst.CPX_ANNOTATIONOBJ_IND,
                      CplexScope.QUAD_CT_SCOPE: cpx_cst.CPX_ANNOTATIONOBJ_QC,
                      CplexScope.SOS_SCOPE: cpx_cst.CPX_ANNOTATIONOBJ_SOS}

except (ImportError, AttributeError):  # pragma: no cover
    LongAnnotationInterface = None
    setlonganno = None
    annotation_map = {}


# gendoc: ignore
def fast_add_linear(cpx, lin_expr, cpx_senses, rhs, names, ranges=None):
    if chbmatrix:
        # BEWARE: expects a string for senses, not a list
        cpx_linearcts = cpx.linear_constraints
        num_old_rows = cpx_linearcts.get_num()
        num_new_rows = len(rhs)
        cpxenv = cpx._env
        with chbmatrix(lin_expr, cpx._env_lp_ptr, 0,
                       cpxenv._apienc) as (rmat, nnz):
            addrows(cpxenv._e, cpx._lp, 0,
                    len(rhs), nnz, rhs, cpx_senses,
                    rmat, [], names, cpxenv._apienc)
        if ranges:
            chgrngval(
                cpxenv._e, cpx._lp,
                list(range(num_old_rows, num_old_rows + num_new_rows)),
                ranges)

        return six.moves.range(num_old_rows, cpx_linearcts.get_num())
    else:  # pragma: no cover
        return cpx.linear_constraints.add(lin_expr=lin_expr, senses=cpx_senses, rhs=rhs, names=names,
                                          range_values=ranges)


def _is_defined_multiobjsetobj():
    if multiobjsetobj is None:
        return False
    return True


def static_fast_set_linear_obj(cpx, indices, obj_coefs):
    chgobj(cpx._env._e, cpx._lp, indices, obj_coefs)

def fast_get_solution(cpx, nb_vars):
    return getx(cpx._env._e, cpx._lp, 0, nb_vars-1)


class ConnectListenersCallback(MIPInfoCallback):
    RELATIVE_EPS = 1e-5
    ABS_EPS = 1e-4

    def make_solution_from_incumbents(self, obj, incumbents):
        # INTERNAL
        mdl = self._model
        assert mdl is not None

        sol = SolveSolution(mdl, obj=obj, solved_by='cplex')
        for v in mdl.iter_variables():
            # incumbent values are provided as a list with indices as positions.
            incumbent_value = incumbents[v._index]
            if incumbent_value:
                # silently round discrete values, just as with engine solutions.
                sol._set_var_value_internal(v, incumbent_value, rounding=True)
        return sol

    # noinspection PyAttributeOutsideInit
    def initialize(self, listeners, model):
        self._count = 0
        self._model = model
        assert model is not None
        self._listeners = listeners
        self._start_time = -1
        self._start_dettime = -1
        for l in listeners:
            l._connect_cb(self)
            # precompute the set of those listeners which listen to solutions.
        self._solution_listeners = set(l for l in listeners if l.requires_solution() and hasattr(l, 'notify_solution'))

    BIGNUM=1e+20

    def __call__(self):
        self._count += 1

        has_incumbent = self.has_incumbent()

        if self._start_time < 0:
            self._start_time = self.get_start_time()
        if self._start_dettime < 0:
            self._start_dettime = self.get_start_dettime()


        obj = self.get_incumbent_objective_value() if has_incumbent else None
        time = self.get_time() - self._start_time
        det_time = self.get_dettime() - self._start_dettime

        pdata = ProgressData(self._count, has_incumbent,
                             obj, self.get_best_objective_value(),
                             self.get_MIP_relative_gap(),
                             self.get_num_iterations(),
                             self.get_num_nodes(),
                             self.get_num_remaining_nodes(),
                             time, det_time
                             )

        solution_listeners = self._solution_listeners
        for l in self._listeners:
            try:
                if l.accept(pdata):
                    # listener has accepted event
                    l.notify_progress(pdata)
                    l._set_current_progress_data(pdata)
                    if has_incumbent and l in solution_listeners:
                        # build a solution from incumbent values as a list of values (value[v] at position index[v])
                        cpx_incumbent_sol = self.make_solution_from_incumbents\
                            (pdata.current_objective, self.get_incumbent_values())
                        l.notify_solution(cpx_incumbent_sol)
                # else:
                #     print("-- rejected: #{0}, listener={1!r}".format(pdata.id, l))
            except Exception as e:
                print('Exception raised in listener {0!r}: {1}, id={2}'.format(type(l).__name__, str(e), pdata.id))


# internal
class _CplexSyncMode(Enum):
    InSync, InResync, OutOfSync = [1, 2, 3]


class CplexIndexMode(Enum):
    # enumerated value for different ways to handle cplex indices.
    # Guess means compute guessed indices, do not query
    #   UseReturn is new API: assume "add" returns a range and use it.
    Guess, UseReturn = 1, 2

    _mode2string = {"guess": Guess, "return": UseReturn}

    @staticmethod
    def parse(text, default_mode):
        return CplexIndexMode._mode2string.get(text.lower(), default_mode) if text else default_mode

    @classmethod
    def get_default(cls, cpx_version):
        if cpx_version >= '12.7.':
            return cls.UseReturn
        else:  # pragma: no cover
            return cls.Guess


class _CplexOverwriteParametersCtx(object):
    # internal context manager to handle forcing parameters during relaxation.

    def __init__(self, cplex_to_overwrite, overwrite_param_dict):
        assert isinstance(overwrite_param_dict, dict)
        self._cplex = cplex_to_overwrite
        self._overwrite_param_dict = overwrite_param_dict
        # store current values
        cplex_params = self._cplex._env.parameters
        self._saved_param_values = {p.cpx_id: cplex_params._get(p.cpx_id) for p in overwrite_param_dict}

    def __enter__(self):
        # force overwrite values.
        cplex_params = self._cplex._env.parameters
        for p, v in six.iteritems(self._overwrite_param_dict):
            cplex_params._set(p.cpx_id, v)
        # return the Cplex instance with the overwritten parameters.
        return self._cplex

    # noinspection PyUnusedLocal
    def __exit__(self, exc_type, exc_val, exc_tb):
        # whatever happened, restore saved parameter values.
        cplex_params = self._cplex._env.parameters
        for pid, saved_v in six.iteritems(self._saved_param_values):
            cplex_params._set(pid, saved_v)


class SilencedCplexContext(object):
    def __init__(self, cplex_instance, error_handler=None):
        self.cplex = cplex_instance
        self.saved_streams = None
        self.error_handler = error_handler

    def __enter__(self):
        self.saved_streams = CplexEngine.cpx_get_all_streams(self.cplex)
        CplexEngine._cpx_set_all_streams(self.cplex, None)
        return self.cplex

    def __exit__(self, exc_type, exc_val, exc_tb):
        CplexEngine.cpx_set_all_streams(self.cplex,
                                        self.saved_streams,
                                        self.error_handler)


class IndexScope(object):  # pragma: no cover
    def __init__(self, name):
        self._name = name
        self._index = -1

    def clear(self):
        self._index = -1

    def new_index(self):
        self._index += 1
        return self._index

    def new_index_range(self, size):
        first = self._index + 1
        last = first + size
        self._index += size
        return fast_range(first, last)

    def notify_deleted(self, deleted_index):
        if deleted_index >= 0:
            self._index -= 1

    def notify_deleted_block(self, deleted_indices):
        self._index -= len(deleted_indices)

    def __str__(self):  # pragma: no cover
        return 'IndexScope({0}}[{1}]'.format(self._name, self._index)


class _SafeCplexWrapper(cplex.Cplex):  # pragma: no cover
    # INTERNAL
    # safe wrapping for pwl issue (cf RTC 31149, 31154, 31155)
    # to be removed in 12.7.1
    # noinspection PyArgumentList
    def __init__(self, *args):
        cplex.Cplex.__init__(self, *args)
        if PWLConstraintInterface:
            self.pwl_constraints = PWLConstraintInterface()
            self.pwl_constraints._setup(self)
        if LongAnnotationInterface:
            self.long_annotations = LongAnnotationInterface()
            self.long_annotations._setup(self)


def _safe_cplex():
    try:
        cpxv = cplex.__version__
        cpx = cplex.Cplex()
    except AttributeError:  # pragma: no cover
        # older version: use an instance
        cpx = cplex.Cplex()
        cpxv = cpx.get_version()

    if cpxv.startswith('12.7.0'):  # pragma: no cover
        if cpx:
            del cpx
        # create a safe wrapper for RTC-31555
        return _SafeCplexWrapper()
    else:
        return cpx


# noinspection PyProtectedMember
class CplexEngine(DummyEngine):
    """
        CPLEX engine wrapper.
    """
    CPX_RANGE_SYMBOL = 'R'

    procedural = True

    cplex_error_re = re.compile(r'CPLEX Error\s+(\d+)')

    if cpx_indicator_type_equiv is None:
        supports_typed_indicators = False  # pragma: no cover
    else:
        try:
            # noinspection PyStatementEffect
            IndicatorConstraintInterface.type_
            supports_typed_indicators = True
        except AttributeError:  # pragma: no cover
            supports_typed_indicators = False

    def supports_logical_constraints(self):
        ok = self._cplex.get_version() >= '12.8.0' and self.supports_typed_indicators
        msg = 'Logical constraints require CPLEX version 12.8 or above, this is CPLEX version: {0}'.format(
            self._cplex.get_version()) if not ok else None
        return ok, msg

    def supports_multi_objective(self):
        ok = (multiobjsetobj is not None)
        msg = 'Multi-objectives require CPLEX version 12.9 or above, this is CPLEX version: {0}'.format(
            self._cplex.get_version()) if not ok else None
        return ok, msg

    def solved_as_mip(self):
        return self._cplex.get_problem_type() not in\
               {cpx_cst.CPXPROB_LP, cpx_cst.CPXPROB_QP, cpx_cst.CPXPROB_QCP}

    def __init__(self, mdl, **kwargs):
        """
        INTERNAL
        :param mdl: the model
        :param index_mode: a string describing how cplex indices are to be managed
        :return:
        """
        DummyEngine.__init__(self)
        cpx = cplex.Cplex()
        if cpx.get_version().startswith('12.7.0'):  # pragma: no cover
            del cpx
            # create a safe wrapper for RTC-31555
            cpx = _SafeCplexWrapper()

        # resetting DATACHECK to 0 has no measurable effect
        # cpx.parameters._set(1056, 0)

        index_mode = None
        if 'index_mode' in kwargs:  # pragma: no cover
            index_mode = kwargs['index_mode']

        self._model = mdl
        self._saved_log_output = True  # initialization from model is deferred (pickle)

        self._index_mode = CplexIndexMode.parse(index_mode, CplexIndexMode.get_default(cpx.get_version()))

        # deferred bounds changes, as dicts {var: num}
        self._var_lb_changed = {}
        self._var_ub_changed = {}

        self._cplex = cpx

        self._solve_count = 0
        self._last_solve_status = False
        self._last_solve_details = None

        # for unpickling, remember to resync with model
        self._resync = _CplexSyncMode.InSync

        # remember truly allocated indices
        self._lincts_scope = IndexScope(name='lincts')
        self._indcst_scope = IndexScope(name='indicators')
        self._quadcst_scope = IndexScope(name='quadcts')
        self._pwlcst_scope = IndexScope(name='piecewises')
        self._vars_scope = IndexScope(name='vars')

        # index of benders long annotation
        self._benders_anno_idx = -1

        # callback connector
        self._ccb = None

    def _mark_as_out_of_sync(self):
        self._resync = _CplexSyncMode.OutOfSync

    def _allocate_one_index(self, ret_value, scope, expect_range):
        self_index_mode = self._index_mode
        if self_index_mode is CplexIndexMode.UseReturn:
            # return value is always a range
            return ret_value[-1] if expect_range else ret_value
        elif self_index_mode is CplexIndexMode.Guess:
            return scope.new_index()  # pragma: no cover
        else:  # pragma: no cover
            raise ValueError

    def _allocate_range_index(self, size, ret_value, scope):
        self_index_mode = self._index_mode
        if self_index_mode is CplexIndexMode.UseReturn:
            return ret_value
        elif self_index_mode is CplexIndexMode.Guess:  # pragma: no cover
            return scope.new_index_range(size)
        else:  # pragma: no cover
            raise ValueError

    @classmethod
    def _cpx_set_all_streams(cls, cpx, ofs):
        cpx.set_log_stream(ofs)
        cpx.set_results_stream(ofs)
        cpx.set_error_stream(ofs)
        cpx.set_warning_stream(ofs)

    @classmethod
    def cpx_get_all_streams(cls, cpx):
        # returns an array of streams in the order: log, result, error, warning
        streams = [cpx._env._get_log_stream(),
                   cpx._env._get_results_stream(),
                   cpx._env._get_error_stream(),
                   cpx._env._get_warning_stream()]
        return [x._file if hasattr(x, '_file') else None for x in streams]

    @classmethod
    def cpx_set_all_streams(cls, cpx, streams, error_handler):
        if len(streams) != 4:
            error_handler.fatal("Wrong number of streams, should be 4: {0!s}", len(streams))
        else:
            cpx.set_log_stream(streams[0])
            cpx.set_results_stream(streams[1])
            cpx.set_error_stream(streams[2])
            cpx.set_warning_stream(streams[3])

    def set_streams(self, out):
        self_log_output = self._saved_log_output
        if self_log_output != out:
            self._cpx_set_all_streams(self._cplex, out)
            self._saved_log_output = out

    def get_var_index(self, dvar):  # pragma: no cover
        self._resync_if_needed()
        dvar_name = dvar.name
        if not dvar_name:
            self.error_handler.fatal("cannot query index for anonymous object: {0!s}", (dvar,))
        else:
            return self._cplex.variables.get_indices(dvar_name)

    def get_ct_index(self, ct):  # pragma: no cover
        self._resync_if_needed()
        ctname = ct.name
        if not ctname:
            self.error_handler.fatal("cannot query index for anonymous constraint: {0!s}", (ct,))
        self_cplex = self._cplex
        ctscope = ct.cplex_scope
        if ctscope is CplexScope.LINEAR_CT_SCOPE:
            return self_cplex.linear_constraints.get_indices(ctname)
        elif ctscope is CplexScope.IND_CT_SCOPE:
            return self_cplex.indicator_constraints.get_indices(ctname)
        elif ctscope is CplexScope.QUAD_CT_SCOPE:
            return self_cplex.quadratic_constraints.get_indices(ctname)
        elif ctscope is CplexScope.PWL_CT_SCOPE:
            return self_cplex.pwl_constraints.get_indices(ctname)

        else:
            self.error_handler.fatal("unrecognized constraint to query index: {0!s}", ct)

    def check_constraint_indices(self, cts):
        for ct in cts:
            if ct.name is None:
                # TODO: for anonymous constraints, check identity between cplex constraint with same index.
                continue
            else:
                model_index = ct.get_index()
                if model_index >= 0:
                    cpx_index = self.get_ct_index(ct)
                    if model_index != cpx_index:  # pragma: no cover
                        self._model.error("indices differ, obj: {0!s}, docplex={1}, CPLEX={2}", ct, model_index,
                                          cpx_index)

    def check_var_indices(self, dvars):  # pragma: no cover
        for dvar in dvars:
            # assuming dvar has a name
            model_index = dvar.get_index()
            cpx_index = self.get_var_index(dvar)
            if model_index != cpx_index:  # pragma: nocover
                self._model.error("indices differ, obj: {0!s}, docplex={1}, CPLEX={2}", dvar, model_index,
                                  cpx_index)

    @property
    def error_handler(self):
        return self._model.error_handler

    def get_cplex(self):
        """
        Returns the underlying CPLEX object
        :return:
        """
        return self._cplex

    def get_infinity(self):
        return cplex.infinity

    def _create_cpx_multitype_vartype_list(self, vartypes):
        # vartypes is a list of model variable types
        # if all continuous return []
        if all(mvt.get_cplex_typecode() == 'C' for mvt in vartypes):
            return ""
        else:
            # return a list of 'B', 'C', 'I' symbols
            return "".join(mvt.get_cplex_typecode() for mvt in vartypes)

    @classmethod
    def compute_cpx_vartype(cls, vartype, size):
        if vartype == 'C':
            return ''
        else:
            return vartype * size

    def create_one_variable(self, vartype, lb, ub, name):
        self._resync_if_needed()
        alltypes = self.compute_cpx_vartype(vartype.get_cplex_typecode(), size=1)
        names1 = [name] if name is not None else []
        lbs1 = [float(lb)] if lb is not None else []
        ubs1 = [float(ub)] if ub is not None else []
        ret_val = self.fast_add_cols(alltypes, lbs1, ubs1, names1)
        return self._allocate_one_index(ret_value=ret_val, scope=self._vars_scope, expect_range=True)

    def create_variables(self, keys, vartype, lbs, ubs, names):
        self._resync_if_needed()
        nb_vars = len(keys)
        cpx_types = self.compute_cpx_vartype(vartype.get_cplex_typecode(), nb_vars)
        if not cpx_types:
            if not (lbs or ubs):
                # force at least one list with correct size.
                lbs = [0] * nb_vars
        return self._create_cpx_variables(nb_vars, cpx_types, lbs, ubs, names)

    def create_multitype_variables(self, nb_vars, vartypes, lbs, ubs, names):
        self._resync_if_needed()
        cpx_types = self._create_cpx_multitype_vartype_list(vartypes)
        return self._create_cpx_variables(nb_vars, cpx_types, lbs, ubs, names)

    def _create_cpx_variables(self, nb_vars, cpx_vartypes, lbs, ubs, names):
        ret_add = self.fast_add_cols(cpx_vartypes, lbs, ubs, names)
        return self._allocate_range_index(size=nb_vars, ret_value=ret_add, scope=self._vars_scope)

    def _apply_var_fn(self, dvars, args, setter_fn, getter_fn=None):
        cpxvars = self._cplex.variables

        indices = [_v.get_index() for _v in dvars]
        setter_fn(cpxvars, izip(indices, args))
        if getter_fn:
            return getter_fn(cpxvars, indices)
        else:
            return None

    _getset_map = {"lb": (cplex._internal._subinterfaces.VariablesInterface.set_lower_bounds,
                          cplex._internal._subinterfaces.VariablesInterface.get_lower_bounds),
                   "ub": (cplex._internal._subinterfaces.VariablesInterface.set_upper_bounds,
                          cplex._internal._subinterfaces.VariablesInterface.get_upper_bounds),
                   "name": (cplex._internal._subinterfaces.VariablesInterface.set_names,
                            cplex._internal._subinterfaces.VariablesInterface.get_names)}

    def rename_var(self, dvar, new_name):
        #self._cplex.variables.set_names([(dvar.get_index(), new_name or "")])
        self._fast_set_col_name(dvar._index, new_name)

    def set_var_type(self, dvar, newtype):  # pragma: no cover
        var_index = dvar.get_index()
        cpxvars = self._cplex.variables
        cpx_newtype = newtype.get_cplex_typecode()
        cpxvars.set_types([(var_index, cpx_newtype)])

    def set_var_lb(self, dvar, lb):
        self._resync_if_needed()
        self_var_lbs = self._var_lb_changed
        self_var_lbs[dvar] = float(lb)

    def set_var_ub(self, dvar, ub):
        self._resync_if_needed()
        self_var_ubs = self._var_ub_changed
        self_var_ubs[dvar] = float(ub)  # force float here: numpy types will crash

    def make_attribute_map_from_scope_fn(self, mdl, cplexfn, scope):
        # transforms an array of cplex values into a map
        # using the scope object as a mapper
        all_values = cplexfn()
        return self.make_attribute_map_from_scope_list(mdl, all_values, scope)

    @classmethod
    def make_attribute_map_from_scope_list(cls, mdl, values, scope, keep_zeros=False):
        value_map = {}
        for ix, cplex_value in enumerate(values):
            mobj = scope(ix)
            if mobj is None:
                mdl.error("No {0} with index: {1} - caution".format(scope.qualifier, ix))
            elif keep_zeros or cplex_value:
                value_map[mobj] = cplex_value

        return value_map

    def get_all_reduced_costs(self, mdl):
        return self.make_attribute_map_from_scope_fn(mdl, self._cplex.solution.get_reduced_costs, mdl._var_scope)

    def get_all_dual_values(self, mdl):
        return self.make_attribute_map_from_scope_fn(mdl, self._cplex.solution.get_dual_values, mdl._linct_scope)

    def get_all_slack_values(self, mdl):
        lin_slacks  = self.make_attribute_map_from_scope_fn(mdl, self._cplex.solution.get_linear_slacks,    mdl._linct_scope)
        quad_slacks = self.make_attribute_map_from_scope_fn(mdl, self._cplex.solution.get_quadratic_slacks, mdl._quadct_scope)
        ind_slacks  = self.make_attribute_map_from_scope_fn(mdl, self._cplex.solution.get_indicator_slacks, mdl._logical_scope)
        # dict : cplex_scope -> dict from obj to slack
        return {CplexScope.LINEAR_CT_SCOPE: lin_slacks,
                CplexScope.QUAD_CT_SCOPE: quad_slacks,
                CplexScope.IND_CT_SCOPE: ind_slacks}

    def get_basis(self, mdl):
        try:
            status_vars, status_licnts = self._cplex.solution.basis.get_basis()
            var_statuses_map = self.make_attribute_map_from_scope_list(mdl, status_vars, mdl._var_scope, keep_zeros=True)
            status_linearct_map = self.make_attribute_map_from_scope_list(mdl, status_licnts, mdl._linct_scope, keep_zeros=True)
            return var_statuses_map, status_linearct_map
        except CplexError as cpxe:
            if cpxe.args[2] == 1262:  # code 1262 is "no basis exists"
                return {}, {}
            else:
                raise

    # the returned list MUST be of size 2 otherwise the wrapper will crash.
    _trivial_linexpr = [[], []]

    @classmethod
    def linear_ct_to_cplex(cls, linear_ct):
        # INTERNAL
        return cls.make_cpx_linear_from_exprs(linear_ct.get_left_expr(), linear_ct.get_right_expr())

    def make_cpx_linear_from_one_expr(self, expr):
        return self.make_cpx_linear_from_exprs(left_expr=expr, right_expr=None)

    @classmethod
    def make_cpx_linear_from_exprs(cls, left_expr, right_expr):
        indices = []
        coefs = []
        if right_expr is None or right_expr.is_constant():
            nb_terms = left_expr.number_of_terms()
            if nb_terms:
                indices = [-1] * nb_terms
                coefs = [0] * nb_terms
                for i, (dv, k) in enumerate(left_expr.iter_terms()):
                    indices[i] = dv._index
                    coefs[i] = float(k)

        elif left_expr.is_constant():
            nb_terms = right_expr.number_of_terms()
            if nb_terms:
                indices = [-1] * nb_terms
                coefs = [0] * nb_terms
                for i, (dv, k) in enumerate(right_expr.iter_terms()):
                    indices[i] = dv._index
                    coefs[i] = -float(k)

        else:
            # hard to guess array size here:
            # we could allocate size(left) + size(right) and truncate, but??
            for dv, k in BinaryConstraint._generate_net_linear_coefs2_unsorted(left_expr, right_expr):
                indices.append(dv._index)
                coefs.append(float(k))

        # all_indices_coefs is a list of  (index, coef) 2-tuples
        if indices:
            # CPLEX requires two lists: one for indices, one for coefs
            # we use zip to unzip the tuples
            return [indices, coefs]
        else:
            # the returned list MUST be of size 2 otherwise the wrapper will crash.
            return cls._trivial_linexpr

    @staticmethod
    def make_cpx_ct_rhs_from_exprs(left_expr, right_expr):
        return right_expr.get_constant() - left_expr.get_constant()

    def __index_problem_stop_here(self):
        #  put a breakpoint here if index problems occur
        pass  # pragma: no cover

    def _make_cplex_linear_ct(self, cpx_lin_expr, cpx_sense, rhs, name):
        # INTERNAL
        cpx_rhs = [float(rhs)]  # if not a float, cplex crashes baaaadly
        cpxnames = [name] if name else []

        ret_add = fast_add_linear(self._cplex, cpx_lin_expr, cpx_sense, cpx_rhs, cpxnames)
        return self._allocate_one_index(ret_value=ret_add, scope=self._lincts_scope, expect_range=True)

    def create_linear_constraint(self, binaryct):
        self._resync_if_needed()
        cpx_linexp1 = self.linear_ct_to_cplex(binaryct)
        # wrap one more time
        cpx_linexp = [cpx_linexp1] if cpx_linexp1 else []
        # returns a number
        num_rhs = binaryct.cplex_num_rhs()
        return self._make_cplex_linear_ct(cpx_lin_expr=cpx_linexp,
                                          cpx_sense=binaryct.cplex_code(),
                                          rhs=num_rhs, name=binaryct.get_name())

    def create_block_linear_constraints(self, linct_seq):
        self._resync_if_needed()
        block_size = len(linct_seq)
        # noinspection PyPep8
        cpx_rhss = [ct.cplex_num_rhs() for ct in linct_seq]
        cpx_sense_string = "".join(ct.cplex_code() for ct in linct_seq)
        if self._model.ignore_names:
            cpx_names = []
        else:
            cpx_names = [ct._get_safe_name() for ct in linct_seq]
        cpx_convert_fn = self.linear_ct_to_cplex
        cpx_linexprs = [cpx_convert_fn(ct) for ct in linct_seq]
        # peek for ranges?
        has_ranges = False
        for ct in linct_seq:
            if ct.cplex_range_value():
                has_ranges = True
                break

        range_values = [ct.cplex_range_value() for ct in linct_seq] if has_ranges else None
        ret_add = fast_add_linear(self._cplex, cpx_linexprs, cpx_sense_string, cpx_rhss, cpx_names, ranges=range_values)
        return self._allocate_range_index(size=block_size, ret_value=ret_add, scope=self._lincts_scope)

    def create_range_constraint(self, range_ct):
        self._resync_if_needed()

        expr = range_ct.expr

        cpx_linexpr = self.make_cpx_linear_from_one_expr(expr)
        cpx_linexpr2 = [cpx_linexpr] if cpx_linexpr else []

        cpx_rhs = [float(range_ct.cplex_num_rhs())]
        cpx_range_values = [float(range_ct.cplex_range_value())]
        cpx_names = [range_ct._get_safe_name()]

        ret_add = fast_add_linear(self._cplex, cpx_linexpr2,
                                  range_ct.cplex_code(),
                                  cpx_rhs, cpx_names,
                                  ranges=cpx_range_values)

        # linearcts = self._cplex.linear_constraints
        # ret_add = linearcts.add(lin_expr=cpx_linexpr2,
        #                         senses=range_ct.cplex_code(),
        #                         rhs=cpx_rhs,
        #                         range_values=cpx_range_values,
        #                         names=cpx_names)
        return self._allocate_one_index(ret_value=ret_add, scope=self._lincts_scope, expect_range=True)

    def rename_linear_constraint(self, linct, new_name):
        safe_new_name = new_name or ""
        linct_index = linct.get_index()
        cpxlinears = self._cplex.linear_constraints
        cpxlinears.set_names([(linct_index, safe_new_name)])

    def create_indicator_constraint(self, indicator):
        ret = self.create_batch_indicator_constraints(iter_one(indicator))
        return ret[0]
        # self._resync_if_needed()
        # linear_ct = indicator.linear_constraint
        # ct_name = indicator.get_name()
        # active_value = indicator._active_value
        # binary_var = indicator.indicator_var
        # binary_index = binary_var.get_index()
        #
        # # the linear ct is n
        # ot posted to CPLEX,
        # # but we need to convert it to linexpr
        # cpx_linexpr = self.linear_ct_to_cplex(linear_ct)
        # rhs = linear_ct.cplex_num_rhs()
        # cpx_name = ct_name or ''
        # cpx_sense = linear_ct.cplex_code()
        #
        # cpx_indicators = self._cplex.indicator_constraints
        # #  BEWARE: cplex's complemented is 1 - active_value
        # cpx_complemented = 1 - active_value
        # ret_add = cpx_indicators.add(cpx_linexpr, cpx_sense, rhs, binary_index, cpx_complemented, cpx_name)
        # return self._allocate_one_index(ret_value=ret_add, scope=self._indcst_scope, expect_range=False)

    def create_equivalence_constraint(self, eqct):
        return self._create_typed_indicator_internal(self._cplex.indicator_constraints,
                                                     self._indcst_scope,
                                                     eqct.binary_var, eqct.linear_constraint,
                                                     complemented=eqct.cpx_complemented,
                                                     equivalence=True, name=eqct.name)

    def create_batch_equivalence_constraints(self, eqcts):
        self._resync_if_needed()
        cpx_indicators = self._cplex.indicator_constraints
        indct_scope = self._indcst_scope
        # TODO: create batch with one call...
        rets = [self._create_typed_indicator_internal(cpx_indicators, indct_scope, eqct.binary_var,
                                                      eqct.linear_constraint, equivalence=True,
                                                      complemented=eqct.cpx_complemented)
                for eqct in eqcts]
        return rets

    def _create_typed_indicator_internal(self, cpx_ind, ind_scope, indvar, linct,
                                         equivalence=False,
                                         complemented=0,
                                         name=None):
        cpx_linexpr = self.linear_ct_to_cplex(linct)
        cpx_name = name or ''
        cpx_sense = linct.cplex_code()
        indvar_index = indvar.safe_index
        cpx_rhs = linct.cplex_num_rhs()
        if equivalence:
            ret_add = cpx_ind.add(cpx_linexpr, cpx_sense, cpx_rhs, indvar_index, complemented, cpx_name, indtype=3)
        else:
            ret_add = cpx_ind.add(cpx_linexpr, cpx_sense, cpx_rhs, indvar_index, complemented, cpx_name)
        return self._allocate_one_index(ret_value=ret_add, scope=ind_scope, expect_range=False)

    def create_batch_indicator_constraints(self, inds):
        self._resync_if_needed()
        cpx_indicators = self._cplex.indicator_constraints
        indct_scope = self._indcst_scope
        rets = []
        # temporary: waiting for CPLEX block API to pass arrays.
        for ind in inds:
            ret = self._create_typed_indicator_internal(cpx_indicators, indct_scope, ind.binary_var,
                                                        ind.get_linear_constraint(),
                                                        equivalence=False,
                                                        complemented=ind.cpx_complemented,
                                                        name=ind._get_safe_name())
            rets.append(ret)
        return rets

    def create_quadratic_constraint(self, qct):
        self._resync_if_needed()
        # ---
        self_cplex = self._cplex
        float_rhs = qct.cplex_num_rhs()
        cpx_sense = qct.cplex_code()
        # see RTC-31772, None is accepted from 12.6.3.R0 onward. use get_name() when dropping compat for 12.6.2
        qctname = qct._get_safe_name()

        # linear part
        net_linears = [(lv._index, float(lk)) for lv, lk in qct.iter_net_linear_coefs()]
        list_linears = list(izip(*net_linears))
        if not list_linears:
            list_linears = [(0,), (0.0,)]  # always non empty
        # build a list of three lists: [qv1.index], [qv2.index], [qk..]

        net_quad_triplets = [(qvp[0]._index, qvp[1]._index, float(qk)) for qvp, qk in qct.iter_net_quads()]
        if net_quad_triplets:
            list_quad_triplets = list(izip(*net_quad_triplets))
            ret_add = self_cplex.quadratic_constraints.add(lin_expr=list_linears,
                                                           quad_expr=list_quad_triplets,
                                                           sense=cpx_sense,
                                                           rhs=float_rhs,
                                                           name=qctname)
            return self._allocate_one_index(ret_value=ret_add, scope=self._quadcst_scope, expect_range=False)
        else:
            # actually a linear constraint
            return self._make_cplex_linear_ct(cpx_lin_expr=[list_linears],
                                              cpx_sense=qct.cplex_code(),
                                              rhs=float_rhs, name=qctname)

    def create_pwl_constraint(self, pwl_ct):
        """
        Post a Piecewise Linear Constraint to CPLEX
        :param pwl_ct: the PWL constraint
        :return:
        """
        self._resync_if_needed()
        try:

            pwl_func = pwl_ct.pwl_func
            pwl_def = pwl_func.pwl_def_as_breaks
            pwlctname = pwl_ct._get_safe_name()
            x_var = pwl_ct.expr
            f_var = pwl_ct.y
            cpx_breaksx = [float(breakx) for breakx, _ in pwl_def.breaksxy]
            cpx_breaksy = [float(breaky) for _, breaky in pwl_def.breaksxy]
            n_breaks = len(cpx_breaksx)
            assert n_breaks == len(cpx_breaksy)
            ret_add = self._fast_add_piecewise_constraint(f_var._index, x_var._index,
                                                          float(pwl_def.preslope),

                                                          n_breaks,
                                                          cpx_breaksx, cpx_breaksy,
                                                          float(pwl_def.postslope),
                                                          name=pwlctname)
            return self._allocate_one_index(ret_value=ret_add, scope=self._pwlcst_scope, expect_range=False)

        except AttributeError:  # pragma: no cover
            self._model.fatal("Please update Cplex to version 12.7+ to benefit from Piecewise Linear constraints.")

    def remove_constraint(self, ct):
        self._resync_if_needed()
        doomed_index = ct.safe_index
        # we have a safe index
        ctscope = ct.cplex_scope
        if ctscope is CplexScope.QUAD_CT_SCOPE:
            self._cplex.quadratic_constraints.delete(doomed_index)
            self._quadcst_scope.notify_deleted(doomed_index)
        elif ctscope is CplexScope.IND_CT_SCOPE:
            self._cplex.indicator_constraints.delete(doomed_index)
            self._indcst_scope.notify_deleted(doomed_index)
        elif ctscope is CplexScope.LINEAR_CT_SCOPE:
            self._cplex.linear_constraints.delete(doomed_index)
            self._lincts_scope.notify_deleted(doomed_index)
        elif ctscope is CplexScope.PWL_CT_SCOPE:
            self._cplex.pwl_constraints.delete(doomed_index)
            self._pwlcst_scope.notify_deleted(doomed_index)
        else:  # pragma: no cover
            raise TypeError

    def remove_constraints(self, cts):
        self._resync_if_needed()
        if cts is None:
            self._cplex.linear_constraints.delete()
            self._lincts_scope.clear()
            self._cplex.quadratic_constraints.delete()
            self._quadcst_scope.clear()
            self._cplex.indicator_constraints.delete()
            self._indcst_scope.clear()
        else:
            doomed_linears = [c.safe_index for c in cts if c.cplex_scope is CplexScope.LINEAR_CT_SCOPE]
            doomed_quadcts = [c.safe_index for c in cts if c.cplex_scope is CplexScope.QUAD_CT_SCOPE]
            dooomed_indcts = [c.safe_index for c in cts if c.cplex_scope is CplexScope.IND_CT_SCOPE]
            if doomed_linears:
                self._cplex.linear_constraints.delete(doomed_linears)
                self._lincts_scope.notify_deleted_block(doomed_linears)
            if doomed_quadcts:
                self._cplex.quadratic_constraints.delete(doomed_quadcts)
                self._quadcst_scope.notify_deleted_block(doomed_quadcts)
            if dooomed_indcts:
                self._cplex.indicator_constraints.delete(dooomed_indcts)
                self._indcst_scope.notify_deleted_block(dooomed_indcts)

    # update
    def _unexpected_event(self, event, msg=''):  # pragma: no cover
        self.error_handler.warning('{0} Unexpected event: {1} - ignored', msg, event.name)

    # -- fast 'procedural' api

    def fast_add_cols(self, cpx_vartype, lbs, ubs, names):
        # assume lbs, ubs, names are list that are either [] or have len size
        cpx = self._cplex
        cpx_e = cpx._env._e
        cpx_lp = cpx._lp
        old = cpx.variables.get_num()
        size = max(len(cpx_vartype), len(lbs), len(ubs), len(names))
        newcols(cpx_e, cpx_lp, obj=[], lb=lbs, ub=ubs, xctype=cpx_vartype, colname=names)
        return six.moves.range(old, old + size)

    def _fast_set_longanno(self, anno_idx, anno_objtype, indices, groups):
        if setlonganno:
            cpx = self._cplex
            cpx_e = cpx._env._e
            cpx_lp = cpx._lp
            setlonganno(cpx_e, cpx_lp, anno_idx, anno_objtype, indices, groups)

    def _fast_set_quadratic_objective(self, quad_expr):
        cpx = self._cplex
        cpx_e = cpx._env._e
        cpx_lp = cpx._lp
        for qvp, qk in quad_expr.iter_quads():
            qv1x = qvp[0]._index
            qv2x = qvp[1]._index
            obj_qk = 2 * qk if qvp.is_square() else qk
            chgqpcoef(cpx_e, cpx_lp, qv1x, qv2x, float(obj_qk))

    def _fast_set_linear_objective(self, linexpr):
        indices = []
        koefs = []

        for dv, k in linexpr.iter_terms():
            indices.append(dv._index)
            koefs.append(float(k))
        if indices:
            static_fast_set_linear_obj(self._cplex, indices, koefs)

    def _fast_set_linear_objective2(self, linexpr):
        nterms = linexpr.number_of_terms()
        if nterms:
            indices = [-1] * nterms
            koefs = [0] * nterms
            i = 0
            for dv, k in linexpr.iter_terms():
                indices[i] = dv._index
                koefs[i] = float(k)
                i += 1

            cpx = self._cplex
            chgobj(cpx._env._e, cpx._lp, indices, koefs)

    def _fast_set_linear_multiobj(self, objidx, linexpr,
                                  weight=DEFAULT_CPX_NO_WEIGHT_CHANGE,
                                  priority=DEFAULT_CPX_NO_PRIORITY_CHANGE,
                                  abstol=DEFAULT_CPX_NO_ABSTOL_CHANGE,
                                  reltol=DEFAULT_CPX_NO_RELTOL_CHANGE,
                                  objname=None):
        nterms = linexpr.number_of_terms()
        indices = [-1] * nterms
        koefs = [0] * nterms
        if nterms:
            i = 0
            for dv, k in linexpr.iter_terms():
                indices[i] = dv._index
                koefs[i] = float(k)
                i += 1

        cpx = self._cplex
        multiobjsetobj(cpx._env._e, cpx._lp, objidx, objind=indices, objval=koefs,
                       priority=priority, weight=weight, abstol=abstol, reltol=reltol, objname=objname)

    def _fast_update_linearct_coefs(self, ct_index, var_indices, coefs):
        assert len(var_indices) == len(coefs)

        num_coefs = len(coefs)
        cpx = self._cplex
        chgcoeflist(cpx._env._e, cpx._lp, [ct_index] * num_coefs, var_indices, coefs)

    def _fast_set_rhs(self, ct_index, new_rhs):
        cpx = self._cplex
        chgrhs(cpx._env._e, cpx._lp, (ct_index,), (new_rhs,))

    def _fast_set_col_name(self, col_index, new_name):
        cpx = self._cplex
        chgcolname(cpx._env._e, cpx._lp, (col_index,), (new_name or "",))

    def _fast_add_piecewise_constraint(self, vary, varx, preslope, nbreaks, breaksx, breaksy, postslope, name):
        cpx = self._cplex
        cpx_env = cpx._env
        addpwl(cpx_env._e, cpx._lp,
               vary, varx,
               preslope, postslope,
               nbreaks, breaksx, breaksy,
               name, cpx_env._apienc)
        # fetch number of pwls, return it -1
        pw_index = getnumpwl(cpx_env._e, cpx._lp) - 1
        return pw_index

    # ---

    def switch_linear_expr(self, index, old_expr, new_expr):
        # INTERNAL
        # clears all linear coefs from an old expr, then set the new coefs
        old_indices = [dv._index for dv in old_expr.iter_variables()]
        old_zeros = [0] * len(old_indices)
        self._fast_update_linearct_coefs(index, old_indices, old_zeros)
        # now set new expr coefs
        cpxlin = self.make_cpx_linear_from_one_expr(expr=new_expr)
        self._fast_update_linearct_coefs(index, cpxlin[0], cpxlin[1])

    def _switch_linear_exprs2(self, ct_index, old_left, old_right, new_left, new_right):
        if old_left and old_right:
            # step 1 zap old coefs to zero (with repeats?)
            zap_indices = [dv._index for dv in old_left.iter_variables()]
            zap_indices += [dv._index for dv in old_right.iter_variables()]
        else:
            zap_indices = None  # self._fast_get_row_vars(ct_index)
        if zap_indices:
            self._fast_update_linearct_coefs(ct_index, zap_indices, [0] * len(zap_indices))
        # step 2: install new coefs
        new_ct_lin = self.make_cpx_linear_from_exprs(new_left, new_right)
        self._fast_update_linearct_coefs(ct_index, new_ct_lin[0], new_ct_lin[1])

    def update_linear_constraint(self, ct, event, *args):
        ct_index = ct.get_index()
        assert ct_index >= 0
        assert event
        updated = False

        if event is upd.LinearConstraintType:
            new_ct_cpxtype = args[0]._cplex_code
            self._cplex.linear_constraints.set_senses(ct_index, new_ct_cpxtype)
            updated = True
        else:
            if event in (upd.LinearConstraintCoef, upd.LinearConstraintGlobal):
                if args:
                    self._switch_linear_exprs2(ct_index,
                                               old_left=ct._left_expr, old_right=ct._right_expr,
                                               new_left=args[0], new_right=args[1])
                else:
                    self._switch_linear_exprs2(ct_index,
                                               old_left=None, old_right=None,
                                               new_left=ct._left_expr, new_right=ct._right_expr)
                updated = True
            if event in (upd.LinearConstraintRhs, upd.LinearConstraintGlobal):
                if args:
                    new_ct_rhs = self.make_cpx_ct_rhs_from_exprs(left_expr=args[0], right_expr=args[1])
                else:
                    new_ct_rhs = ct.cplex_num_rhs()
                self._fast_set_rhs(ct_index, new_rhs=new_ct_rhs)
                updated = True

        if not updated:  # pragma: no cover
            self._unexpected_event(event, msg='update_linear-constraint')

    def update_range_constraint(self, rngct, event, *args):
        rng_index = rngct.get_index()
        assert rng_index >= 0
        cpx_linear = self._cplex.linear_constraints
        if event == upd.RangeConstraintBounds:
            new_lb, new_ub = args
            offset = rngct.expr.get_constant()
            cpx_rhs_value = new_ub - offset
            msg = lambda: "Cannot update range values of {0!s} to [{1}..{2}]: domain is infeasible".format(rngct, new_lb, new_ub)
            cpx_range_value = RangeConstraint.static_cplex_range_value(self._model, new_lb, new_ub, msg)
            cpx_linear.set_rhs(rng_index, cpx_rhs_value)
            cpx_linear.set_range_values(rng_index, cpx_range_value)

        elif event == upd.RangeConstraintExpr:
            old_expr = rngct.expr
            new_expr = args[0]
            if old_expr.get_constant() != new_expr.get_constant():
                # need to change rhs but *not* range (ub-lb)
                cpx_rhs_value = rngct.ub - new_expr.get_constant()
                # TODO: check positive??
                cpx_linear.set_rhs(rng_index, cpx_rhs_value)
            # change expr linear components anyway
            self.switch_linear_expr(rng_index, old_expr, new_expr)

        else:  # pragma: no cover
            self._unexpected_event(event, msg='update_range_constraints')

    def update_quadratic_constraint(self, qct, event, *args):
        self._model.fatal('CPLEX cannot modify quadratic constraint: {0!s}', qct)

    def update_logical_constraint(self, lgct, event, *args):
        if isinstance(lgct, IndicatorConstraint):
            self._model.fatal('CPLEX cannot modify a linear constraint used in an indicator: ({0!s})', lgct)
        elif isinstance(lgct, EquivalenceConstraint):
            if not lgct.is_generated():
                self._model.fatal('CPLEX cannot modify a linear constraint used in an equivalence: ({0!s})', lgct)
            else:
                self._model.fatal('Using the truth value of the constraint: ({0!s}) makes the constraint immutable',
                                  lgct.linear_constraint)
        else:  # pragma: no cover
            self._model.fatal('Unexpected type for logical constraint: {0!r}', lgct)

    def update_constraint(self, ct, event, *args):
        if event and ct.index >= 0:
            scope = ct.cplex_scope
            if scope == CplexScope.LINEAR_CT_SCOPE:
                self.update_linear_constraint(ct, event, *args)
            elif scope == CplexScope.IND_CT_SCOPE:
                self.update_logical_constraint(ct, event, *args)
            elif scope == CplexScope.QUAD_CT_SCOPE:
                self.update_quadratic_constraint(ct, event, *args)
            else:
                self._model.fatal('Unexpected scope in update_constraint: {0!r}', scope)

    def set_objective_sense(self, sense):
        self._resync_if_needed()
        # --- set sense
        self._cplex.objective.set_sense(sense.cplex_coef)

    def _clear_objective_from_cplex(self, cpxobj):
        self._clear_linear_objective_from_cplex(cpxobj)
        self._clear_quad_objective_from_cplex(cpxobj)

    def _clear_multiobj_from_cplex(self, cpx_multiobj):
        numobj = cpx_multiobj.get_num()
        for objidx in range(numobj):
            cpx_linear = cpx_multiobj.get_linear(objidx)
            zap_linear = [(idx, 0) for idx, k in enumerate(cpx_linear) if k]
            if zap_linear:
                cpx_multiobj.set_linear(objidx, zap_linear)

    def _clear_linear_objective_from_cplex(self, cpxobj):
        # clear linear part
        cpx_linear = cpxobj.get_linear()
        zap_linear = [(idx, 0) for idx, k in enumerate(cpx_linear) if k]
        if zap_linear:
            cpxobj.set_linear(zap_linear)

    def _clear_quad_objective_from_cplex(self, cpxobj):
        # quadratic
        if cpxobj.get_num_quadratic_variables():
            # need to check before calling get_quadratic() on non-qp -> crash
            cpx_quads = cpxobj.get_quadratic()
            if cpx_quads:
                # reset all vars to zero
                nb_vars = self._model.number_of_variables
                zap_quads = [0.0] * nb_vars  # needs a 0.0 as cplex explicitly tests for double...
                cpxobj.set_quadratic(zap_quads)

    def update_objective(self, expr, event, *args):
        cpxobj = self._cplex.objective
        if event is upd.ExprConstant:
            # update the constant
            self._cplex.objective.set_offset(expr.constant)
        elif event in frozenset([upd.LinExprCoef, upd.LinExprGlobal]):
            self._clear_linear_objective_from_cplex(cpxobj)
            self._set_linear_objective_coefs(cpxobj, linexpr=expr.get_linear_part())
            if event is upd.LinExprGlobal:
                cpxobj.set_offset(expr.constant)
        elif event is upd.QuadExprQuadCoef:
            # clear quad, set quad
            self._clear_quad_objective_from_cplex(cpxobj)
            self._set_quadratic_objective_coefs(cpxobj, expr)
        elif event is upd.QuadExprGlobal:
            # clear all
            self._clear_linear_objective_from_cplex(cpxobj)
            # set all
            self._set_linear_objective_coefs(cpxobj, linexpr=expr.get_linear_part())
            self._clear_quad_objective_from_cplex(cpxobj)
            self._set_quadratic_objective_coefs(cpxobj, expr)
            cpxobj.set_offset(expr.constant)

        else:  # pragma: no cover
            self._unexpected_event(event, msg='update_objective')

    def set_objective_expr(self, new_objexpr, old_objexpr):
        cpx_objective = self._cplex.objective
        # old objective
        if old_objexpr is new_objexpr:
            # cannot use the old expression for clearing, it has been modified
            self._clear_objective_from_cplex(cpxobj=cpx_objective)
        elif old_objexpr is not None:
            self._clear_objective(old_objexpr)
        else:
            # no clearing
            pass
        # # if a multi-objective has been defined, clear it
        # cpx_multiobj = self._cplex.multiobj
        # if cpx_multiobj is not None:
        #     self._clear_multiobj_from_cplex(cpx_multiobj=cpx_multiobj)

        # --- set offset
        cpx_objective.set_offset(float(new_objexpr.get_constant()))
        # --- set coefficients
        if new_objexpr.is_quad_expr():
            self._fast_set_quadratic_objective(quad_expr=new_objexpr)
            self._fast_set_linear_objective(new_objexpr.linear_part)
        else:
            self._fast_set_linear_objective2(linexpr=new_objexpr)

    def set_multi_objective_exprs(self, new_multiobjexprs, old_multiobjexprs, multiobj_params=None,
                                  priorities=None, weights=None, abstols=None, reltols=None, objnames=None):
        self._check_multi_objective_support()

        cpx_multiobj = self._cplex.multiobj
        if old_multiobjexprs is not None:
            # Not safe to use the old expressions for clearing, in case they have been modified for the new expressions
            self._clear_multiobj_from_cplex(cpx_multiobj=cpx_multiobj)

        # # if a regular single objective has been defined, clear it
        # cpx_objective = self._cplex.objective
        # if cpx_objective is not None:
        #     self._clear_objective_from_cplex(cpxobj=cpx_objective)

        # --- set number of objectives
        cpx_multiobj.set_num(len(new_multiobjexprs))
        for objidx, new_objexpr in enumerate(new_multiobjexprs):
            # --- set offset
            cpx_multiobj.set_offset(objidx, float(new_objexpr.get_constant()))
            # --- set coefficients
            weight = DEFAULT_CPX_NO_WEIGHT_CHANGE
            priority = DEFAULT_CPX_NO_PRIORITY_CHANGE
            abstol = DEFAULT_CPX_NO_ABSTOL_CHANGE
            reltol = DEFAULT_CPX_NO_RELTOL_CHANGE
            objname = None
            if priorities is not None and len(priorities) >= objidx + 1:
                priority = priorities[objidx]
            if weights is not None and len(weights) >= objidx + 1:
                weight = weights[objidx]
            if abstols is not None and len(abstols) >= objidx + 1:
                abstol = abstols[objidx]
            if reltols is not None and len(reltols) >= objidx + 1:
                reltol = reltols[objidx]
            if objnames is not None and len(objnames) >= objidx + 1:
                objname = objnames[objidx]
            self._fast_set_linear_multiobj(objidx, linexpr=new_objexpr,
                                           weight=weight, priority=priority,
                                           abstol=abstol, reltol=reltol,
                                           objname=objname)

    def _set_linear_objective_coefs(self, cpx_objective, linexpr):
        # NOTE: convert to float as numpy doubles will crash cplex....
        #     index_coef_seq = [(dv._index, float(k)) for dv, k in linexpr.iter_terms()]
        #     if index_coef_seq:
        #         # if list is empty, cplex will crash.
        #         cpx_objective.set_linear(index_coef_seq)
        self._fast_set_linear_objective(linexpr)

    def _set_quadratic_objective_coefs(self, cpx_objective, quad_expr):
        quad_obj_triplets = [(qv1._index, qv2._index, 2 * qk if qv1 is qv2 else qk) for qv1, qv2, qk in
                             quad_expr.iter_quad_triplets()]
        if quad_obj_triplets:
            # if list is empty, cplex will crash.
            cpx_objective.set_quadratic_coefficients(quad_obj_triplets)

    def _clear_objective(self, expr):
        # INTERNAL
        self._resync_if_needed()
        if expr.is_constant():
            pass  # resetting offset will do.
        elif expr.is_quad_expr():
            # 1. reset quad part
            cpx_objective = self._cplex.objective
            # -- set quad coeff to 0 for all quad variable pairs
            quad_reset_triplets = [(qvp.first._index, qvp.second._index, 0) for qvp, qk in expr.iter_quads()]
            if quad_reset_triplets:
                cpx_objective.set_quadratic_coefficients(quad_reset_triplets)
            # 2. reset linear part
            self._clear_linear_objective(expr.linear_part)
        else:
            self._clear_linear_objective(expr)

    def _clear_multiobj(self, exprs):
        # INTERNAL
        self._resync_if_needed()
        for objidx, expr in enumerate(exprs):
            if expr.is_constant():
                pass  # resetting offset will do.
            else:
                self._clear_linear_multiobj(objidx, expr)

    def _clear_linear_objective(self, linexpr):
        # compute the sequence of  var indices, then an array of zeroes
        size = linexpr.number_of_terms()
        if size:
            indices = [-1] * size
            i = 0
            for dv, _ in linexpr.iter_terms():
                indices[i] = dv._index
                i += 1
            zeros = [0] * size
            cpx = self._cplex
            chgobj(cpx._env._e, cpx._lp, indices, zeros)

    def _clear_linear_multiobj(self, objidx, linexpr):
        # compute the sequence of var indices, then an array of zeroes
        size = linexpr.number_of_terms()
        if size:
            indices = [-1] * size
            i = 0
            for dv, _ in linexpr.iter_terms():
                indices[i] = dv._index
                i += 1
            zeros = [0] * size
            cpx = self._cplex
            multiobjsetobj(cpx._env._e, cpx._lp, objidx, objind=indices, objval=zeros)

    @staticmethod
    def status2string(cpx_status):  # pragma: no cover
        ''' Converts a CPLEX integer status value to a string'''
        return _subinterfaces.SolutionInterface.status.__getitem__(cpx_status)

    _CPLEX_SOLVE_OK_STATUSES = frozenset({1,  # CPX_STAT_OPTIMAL
                                          6,  # CPX_STAT_NUM_BEST: solution exists but numerical issues
                                          24,  # CPX_STAT_FIRSTORDER: stting optimlaitytarget to 2
                                          101,  # CPXMIP_OPTIMAL
                                          102,  # CPXMIP_OPTIMAL_TOL
                                          104,  # CPXMIP_SOL_LIM
                                          105,  # CPXMPI_NODE_LIM_FEAS
                                          107,  # CPXMIP_TIME_LIM_FEAS
                                          109,  # CPXMIP_FAIL_FEAS : what is this ??
                                          111,  # CPXMIP_MEM_LIM_FEAS
                                          113,  # CPXMIP_ABORT_FEAS
                                          116,  # CPXMIP_FAIL_FEAS_NO_TREE : integer sol exists (????)
                                          129,  # CPXMIP_OPTIMAL_POPULATED
                                          130,  # CPXMIP_OPTIMAL_POPULATED_TOL
                                          301,  # CPX_STAT_MULTIOBJ_OPTIMAL
                                          305  # CPX_STAT_MULTIOBJ_NON_OPTIMAL
                                          })

    @classmethod
    def _is_solve_status_ok(cls, status):
        # Converts a raw CPLEX status to a boolean
        return status in cls._CPLEX_SOLVE_OK_STATUSES

    _CPLEX_RELAX_OK_STATUSES = frozenset({cpx_cst.CPX_STAT_FEASIBLE,
                                          cpx_cst.CPXMIP_OPTIMAL_RELAXED_INF,
                                          cpx_cst.CPXMIP_OPTIMAL_RELAXED_SUM,
                                          cpx_cst.CPXMIP_OPTIMAL_RELAXED_QUAD,
                                          cpx_cst.CPXMIP_FEASIBLE_RELAXED_INF,
                                          cpx_cst.CPXMIP_FEASIBLE_RELAXED_QUAD,
                                          cpx_cst.CPXMIP_FEASIBLE_RELAXED_SUM,
                                          cpx_cst.CPX_STAT_FEASIBLE_RELAXED_SUM,
                                          cpx_cst.CPX_STAT_FEASIBLE_RELAXED_INF,
                                          cpx_cst.CPX_STAT_FEASIBLE_RELAXED_QUAD,
                                          cpx_cst.CPX_STAT_OPTIMAL_RELAXED_INF,
                                          cpx_cst.CPX_STAT_OPTIMAL_RELAXED_SUM,
                                          cpx_cst.CPXMIP_ABORT_RELAXED
                                          }).union(_CPLEX_SOLVE_OK_STATUSES)

    @classmethod
    def _is_relaxed_status_ok(cls, status):
        # list all status values for which there is a relaxed solution.
        # also consider solve statuses in case  the model is indeed feasible
        return status in cls._CPLEX_RELAX_OK_STATUSES

    def can_solve(self):
        return True

    @property
    def name(self):
        return self.get_name()

    def get_name(self):
        return 'cplex_local'

    @staticmethod
    def sol_to_cpx_mipstart(model, mipstart, completion=False):
        if completion:
            tl = [(dv.get_index(), mipstart[dv]) for dv in model.generate_user_variables()]
        else:
            tl = [(dv.get_index(), dvv) for dv, dvv in mipstart.iter_var_values()]
        ul = zip(*tl)
        # py3 zip() returns a generator, not a list, and CPLEX needs a list!
        return list(ul)

    def _sync_var_bounds(self, verbose=False):
        self_var_lbs = self._var_lb_changed
        if self_var_lbs:
            lb_vars, lb_values = zip(*six.iteritems(self_var_lbs))
            self._apply_var_fn(dvars=lb_vars, args=lb_values,
                               setter_fn=cplex._internal._subinterfaces.VariablesInterface.set_lower_bounds)
            if verbose:  # pragma: no cover
                print("* synced {} var lower bounds".format(len(self._var_lb_changed)))

        self_var_ubs = self._var_ub_changed
        if self_var_ubs:
            ub_vars, ub_values = zip(*six.iteritems(self_var_ubs))
            self._apply_var_fn(dvars=ub_vars, args=ub_values,
                               setter_fn=cplex._internal._subinterfaces.VariablesInterface.set_upper_bounds)
            if verbose:  # pragma: no cover
                print("* synced {} var upper bounds".format(len(self._var_ub_changed)))

    def _sync_annotations(self, model):
        cpx = self._cplex
        annotated_by_scope = []
        try:
            # separate go to the model and get all annotations
            annotated_by_scope = model.get_annotations_by_scope()

            cpx_anno = cpx.long_annotations
            # du passe faison table rase....
            cpx_anno.delete()
            if annotated_by_scope:
                benders_idx = self._benders_anno_idx
                if benders_idx < 0:
                    # create benders annotation
                    benders_idx = cpx_anno.add(cpx_cst.CPX_BENDERS_ANNOTATION, 0)  # quid of defval?
                    assert benders_idx >= 0
                    self._benders_anno_idx = benders_idx
                # ---

                # at this stage we have a valid annotation index
                # and a dict of scope -> list of (idx, anno) tuples
                for cpx_scope, annotated in six.iteritems(annotated_by_scope):
                    cpx_anno_objtype = annotation_map.get(cpx_scope)
                    if cpx_anno_objtype:
                        annotated_indices = []
                        long_annotations = []
                        for obj, group in annotated:
                            annotated_indices.append(obj.index)
                            long_annotations.append(group)
                        self._fast_set_longanno(benders_idx, cpx_anno_objtype, annotated_indices, long_annotations)
                    else:
                        self._model.error('Cannot map to CPLEX annotation type: {0!r}. ignored', cpx_scope)
            elif cpx_anno.get_num():
                cpx_anno.delete()

        except AttributeError:  # pragma: no cover
            if annotated_by_scope:
                self._model.fatal('Annotations require CPLEX 12.7.1 or higher')

    def create_sos(self, sos_set):
        cpx_sos_type = sos_set.sos_type._cpx_sos_type()
        indices = [dv.index for dv in sos_set.iter_variables()]
        weights = sos_set.get_ranks()
        # do NOT pass None to cplex/swig here --> crash
        cpx_sos_name = sos_set._get_safe_name()
        # call cplex...
        sos_index = self._cplex.SOS.add(type=cpx_sos_type,
                                        SOS=cplex.SparsePair(ind=indices, val=weights),
                                        name=cpx_sos_name)
        return sos_index

    def clear_all_sos(self):
        self._cplex.SOS.delete()

    def add_lazy_constraints(self, lazy_cts):
        if lazy_cts:
            # lazy_cts is a sequence of linear constraints
            cpx_rhss = [ct.cplex_num_rhs() for ct in lazy_cts]
            cpx_senses = "".join(ct.cplex_code() for ct in lazy_cts)
            if self._model.ignore_names:
                cpx_names = []
            else:
                cpx_names = [ct._get_safe_name() for ct in lazy_cts]
            cpx_convert_fn = self.linear_ct_to_cplex
            cpx_linexprs = [cpx_convert_fn(ct) for ct in lazy_cts]
            # TODO: switch to procedural API at some point...
            self._cplex.linear_constraints.advanced.add_lazy_constraints(cpx_linexprs, cpx_senses, cpx_rhss, cpx_names)

    def clear_lazy_constraints(self):
        self._cplex.linear_constraints.advanced.free_lazy_constraints()

    def add_user_cuts(self, cut_cts):
        if cut_cts:
            # cut_cts is a sequence of linear constraints
            cpx_rhss = [ct.cplex_num_rhs() for ct in cut_cts]
            cpx_senses = "".join(ct.cplex_code() for ct in cut_cts)
            if self._model.ignore_names:
                cpx_names = []
            else:
                cpx_names = [ct._get_safe_name() for ct in cut_cts]
            cpx_convert_fn = self.linear_ct_to_cplex
            cpx_linexprs = [cpx_convert_fn(ct) for ct in cut_cts]
            # TODO: switch to procedural API at some point...
            self._cplex.linear_constraints.advanced.add_user_cuts(cpx_linexprs, cpx_senses, cpx_rhss, cpx_names)

    def clear_user_cuts(self):
        self._cplex.linear_constraints.advanced.free_user_cuts()

    def sync_extra_cts(self, mdl):
        adv = self._cplex.linear_constraints.advanced
        adv.free_user_cuts()
        self.add_user_cuts(mdl._user_cuts)
        adv.free_lazy_constraints()
        self.add_lazy_constraints(mdl._lazy_constraints)

    def sync_equivalence_cts(self, mdl):
        if self.supports_typed_indicators:
            posted_eqcts = []
            for eqct in mdl.iter_implicit_equivalence_cts():
                if eqct._index < 0:
                    posted_eqcts.append(eqct)
            if posted_eqcts:
                eq_indices = self.create_batch_equivalence_constraints(posted_eqcts)
                for eqct, eqx in izip(posted_eqcts, eq_indices):
                    eqct.set_index(eqx)

                # nb_equivs = len(posted_eqcts)
                # if nb_equivs:
                #     print('-- posted: {0} equivalence cts'.format(nb_equivs))

    def _format_cplex_message(self, cpx_msg):
        if 'CPLEX' not in cpx_msg:
            cpx_msg = 'CPLEX: %s' % cpx_msg
        return cpx_msg.rstrip(' .\n')

    def _parse_cplex_exception_as_status(self, cpx_ex):
        cpx_ex_s = str(cpx_ex)
        msg = cpx_ex_s
        for extype in ['CplexSolverError', 'CplexError']:
            prefix = 'cplex.exceptions.errors.{0}: '.format(extype)
            if cpx_ex_s.startswith(prefix):
                msg = cpx_ex_s[len(prefix):]

        cpx_code_match = self.cplex_error_re.match(msg)
        code = -1
        if cpx_code_match:
            try:
                code = int(cpx_code_match.group(1))
            except ValueError:
                pass

        return code, msg

    def clean_before_solve(self):
        # INTERNAL
        # delete all infos that were left by the previous solve
        # from DJ- RTC34054
        cpx = self._cplex
        cpx.MIP_starts.delete()
        cpx.presolve.free()
        cpx.solution.pool.delete()
        # dummy change
        if cpx.variables.get_num() > 0:
            cpx.variables.set_lower_bounds(0, cpx.variables.get_lower_bounds(0))
        elif cpx.linear_constraints.get_num() > 0:
            cpx.linear_constraints.set_senses(0, cpx.linear_constraints.get_senses(0))
        else:
            pass

    def _get_priorities_list_in_decreasing_order(self):
        # Compute list of priorities in decreasing order
        prio_list = [self._cplex.multiobj.get_priority(oidx) for oidx in range(self._cplex.multiobj.get_num())]
        prio_set = set(prio_list)
        inversed_ordered_prio = sorted(list(prio_set))
        inversed_ordered_prio.reverse()
        return inversed_ordered_prio

    def _check_multi_objective_support(self):
        ok, msg = self.supports_multi_objective()
        if not ok:
            self._model.fatal(msg)

    def set_lp_starts(self, dvar_stats, lct_stats):
        cpx = self._cplex
        dvar_int_stats = [stat.value for stat in dvar_stats]
        lct_int_stats = [stat.value for stat in lct_stats]
        cpx.start.set_start(dvar_int_stats, lct_int_stats, col_primal=[], col_dual=[], row_primal=[], row_dual=[])

    def solve(self, mdl, parameters=None, lex_mipstart=None, lex_timelimits=None, lex_mipgaps=None):
        self._resync_if_needed()

        cpx = self._cplex
        # keep this line until RTC28217 is solved and closed !!! ----------------
        # see RTC 28217 item #18 for details
        cpx.get_problem_name()  # workaround from Ryan

        # ------ !!! see RTC34123 ---
        setintparam(cpx._env._e, 1047, -1)
        # ---------------------------
        self._solve_count += 1
        solve_time_start = cpx.get_time()
        cpx_status = -1
        cpx_miprelgap = None
        cpx_bestbound = None
        linear_nonzeros = -1
        nb_columns = 0
        cpx_probtype = None
        # print("--> starting CPLEX solve #", self.__solveCount)
        cpx_status_string = None
        try:
            # keep this in the protected  block...
            self._sync_var_bounds()
            self._sync_annotations(mdl)
            self.sync_equivalence_cts(mdl)
            self.sync_extra_cts(mdl)

            if mdl.clean_before_solve:
                self.clean_before_solve()

            # --- mipstart block ---
            cpx_mip_starts = cpx.MIP_starts
            if not lex_mipstart:
                # ignore mip starts if within lexicographic
                for (mps, effort_level) in mdl.iter_mip_starts():
                    if not mps.number_of_var_values:
                        self._model.warning("Empty MIP start solution ignored")
                    else:
                        cpx_sol = self.sol_to_cpx_mipstart(mdl, mps)
                        cpx_mip_starts.add(cpx_sol, effort_level.value)
            elif mdl.number_of_mip_starts:
                self._model.warning("Lexicographic solve ignored {0} mipstarts".format(mdl.number_of_mip_starts))

            # --- end of mipstart block ---

            linear_nonzeros = cpx.linear_constraints.get_num_nonzeros()
            nb_columns = cpx.variables.get_num()
            cpx_probtype = cpx.problem_type[cpx.get_problem_type()]

            # # FOR TEST PURPOSE ---- TEMPORARY **************************************************************************
            # cpx.write("/temp/cplex_model.lp", filetype="lp")

            #Handle lex_timelimits list
            if lex_timelimits is not None or lex_mipgaps is not None:
                self._check_multi_objective_support()

                # Get list of priorities in decreasing order
                decreasing_ordered_prio = self._get_priorities_list_in_decreasing_order()

                if lex_timelimits is not None and len(lex_timelimits) != len(decreasing_ordered_prio):
                    mdl.fatal("lex_timelimits list length does not match number of priorities for multiobjective solve")
                if lex_mipgaps is not None and len(lex_mipgaps) != len(decreasing_ordered_prio):
                    mdl.fatal("lex_mipgaps list length does not match number of priorities for multiobjective solve")
                paramsets = []
                for _ in decreasing_ordered_prio:
                    paramset = cpx.create_parameter_set()
                    paramsets.append(paramset)
                if lex_timelimits is not None:
                    for paramIdx, timelimit in enumerate(lex_timelimits):
                        paramsets[paramIdx].add(cpx_cst.CPX_PARAM_TILIM, timelimit)
                if lex_mipgaps is not None:
                    for paramIdx, mipgap in enumerate(lex_mipgaps):
                        paramsets[paramIdx].add(cpx_cst.CPX_PARAM_EPGAP, mipgap)
                # If there is a single priority level, timelimit and mipgaps are handled at the cplex_parameters level
                paramsets = paramsets if len(paramsets) > 1 else None

                cpx.solve(paramsets=paramsets)

            else:
                cpx.solve()

            cpx_status = cpx.solution.get_status()
            cpx_status_string = self._cplex.solution.get_status_string(cpx_status)
            is_mip = cpx._is_MIP()

            solve_ok = self._is_solve_status_ok(cpx_status)
            if solve_ok:
                if is_mip:
                    cpx_miprelgap = cpx.solution.MIP.get_mip_relative_gap()
                    cpx_bestbound = cpx.solution.MIP.get_best_objective()

        except cplex.exceptions.CplexSolverError as cpx_se:  # pragma: no cover
            cpx_code = cpx_se.args[2]
            if 5002 == cpx_code:
                # we are in the notorious "non convex" case.
                # provide a meaningful status string for the solve details
                cpx_status = 5002  # famous error code...

                if self._model.has_quadratic_constraint():
                    cpx_status_string = "Non-convex QCP"
                    self._model.error('Model is non-convex')
                else:
                    cpx_status_string = "QP with non-convex objective"
                    self._model.error('Model has non-convex objective: {0!s}', str_holo(self._model.objective_expr, 60))
            elif 1016 == cpx_code:
                # this is the: CPXERR_RESTRICTED_VERSION - " Promotional version. Problem size limits exceeded." case
                cpx_status = 1016
                cpx_status_string = "Promotional version. Problem size limits exceeded., CPLEX code=1016."
                self._model.fatal_ce_limits()
            else:
                cpx_status, cpx_status_string = self._parse_cplex_exception_as_status(cpx_se)
            solve_ok = False

        except cplex.exceptions.CplexError as cpx_e:  # pragma: no cover
            self.error_handler.error("CPLEX error: {0!s}", self._format_cplex_message(cpx_e))
            cpx_status, cpx_status_string = self._parse_cplex_exception_as_status(cpx_e)
            solve_ok = False

        except Exception as pe:  # pragma: no cover
            solve_ok = False
            self.error_handler.error('Internal error in CPLEX solve: {0!s}'.format(pe))
            cpx_status_string = 'Internal error: {0!s}'.format(pe)
            cpx_status = -2

        finally:

            solve_time = cpx.get_time() - solve_time_start
            nb_iterations = cpx.solution.progress.get_num_iterations()
            if cpx._is_MIP():
                # cplex complains on non-MIPs
                nb_nodes_processed = cpx.solution.progress.get_num_nodes_processed()
            else:
                nb_nodes_processed = 0

            details = SolveDetails(solve_time,
                                   cpx_status, cpx_status_string,
                                   cpx_probtype,
                                   nb_columns, linear_nonzeros,
                                   cpx_miprelgap, cpx_bestbound,
                                   nb_iterations,
                                   nb_nodes_processed)
            if self._model.quality_metrics:
                details._quality_metrics = self._compute_quality_metrics()
            self._last_solve_details = details

        # clear bound change requests
        self._var_lb_changed = {}
        self._var_ub_changed = {}

        self._last_solve_status = solve_ok
        new_solution = None
        if solve_ok:
            new_solution = self._make_solution(mdl, self.get_solve_status())
            # cache attributes?
        else:
            mdl.notify_solve_failed()
        if cpx_status_string:
            mdl.error_handler.trace("CPLEX solve returns with status: {0}", (cpx_status_string,))
        return new_solution

    def _make_solution(self, mdl, job_solve_status):
        cpx = self._cplex
        full_obj = cpx.solution.get_objective_value()
        if _is_defined_multiobjsetobj() and cpx.multiobj.get_num() > 1:
            full_obj = [cpx.solution.multiobj.get_objective_value(objidx) for objidx in range(cpx.multiobj.get_num())]
        rounded_obj = mdl.round_objective_if_discrete(full_obj)

        # Build list of objectives value by priority level (ie: each priority level corresponds to blended objectives
        # with same priority)
        full_obj_by_prio = [full_obj]
        if _is_defined_multiobjsetobj() and cpx.multiobj.get_num() > 1:
            decreasing_ordered_prio = self._get_priorities_list_in_decreasing_order()
            full_obj_by_prio = [cpx.solution.multiobj.get_objval_by_priority(prio) for prio in decreasing_ordered_prio]
        rounded_obj_by_prio = mdl.round_objective_if_discrete(full_obj_by_prio)

        nb_vars = mdl.number_of_variables
        if nb_vars > 0:
            if self.procedural:
                all_var_values = fast_get_solution(cpx, nb_vars)
            else:
                all_var_indices = [dvar.get_index() for dvar in mdl.iter_variables()]
                # do not query values on an empty model...
                all_var_values = cpx.solution.get_values(all_var_indices)
                #all_var_values = fast_get_solution(cpx, mdl.number_of_variables)
            vmap = {}
            for dv in mdl.iter_variables():
                dvv = all_var_values[dv._index]
                if dvv:
                    vmap[dv] = dvv
            var_value_map = vmap
            #var_value_map = dict(izip(mdl.iter_variables(), all_var_values))
        else:
            var_value_map = {}

        solve_details = self._last_solve_details
        assert solve_details is not None
        solution = SolveSolution.make_engine_solution(model=mdl,
                                                      var_value_map=var_value_map,
                                                      obj=rounded_obj,
                                                      blended_obj_by_priority=rounded_obj_by_prio,
                                                      solved_by=self.get_name(),
                                                      solve_details=solve_details,
                                                      job_solve_status=job_solve_status)
        return solution

    def _run_cpx_op_with_details(self, cpx_fn, *args):
        cpx = self._cplex
        cpx_time_start = cpx.get_time()
        cpx_status = -1
        cpx_status_string = "*unknown*"
        cpx_miprelgap = None
        cpx_bestbound = None
        linear_nonzeros = -1
        nb_columns = 0
        cpx_probtype = None
        # noinspection PyPep8
        try:
            linear_nonzeros = cpx.linear_constraints.get_num_nonzeros()
            nb_columns = cpx.variables.get_num()
            if args:
                cpx_fn(*args)
            cpx_status = cpx.solution.get_status()
            cpx_probtype = cpx.problem_type[cpx.get_problem_type()]
            cpx_status_string = self._cplex.solution.get_status_string(cpx_status)
            solve_ok = self._is_relaxed_status_ok(cpx_status)
            if solve_ok:
                if cpx._is_MIP():
                    cpx_miprelgap = cpx.solution.MIP.get_mip_relative_gap()
                    cpx_bestbound = cpx.solution.MIP.get_best_objective()

        except cplex.exceptions.CplexSolverError as cpx_s:  # pragma: no cover
            cpx_code = cpx_s.args[2]
            if 5002 == cpx_code:
                # we are in the notorious "non convex" case.
                # provide a meaningful status string for the solve details
                cpx_status = 5002  # famous error code...

                if self._model.has_quadratic_constraint():
                    cpx_status_string = "Non-convex QCP"
                    self._model.error('Model is non-convex')
                else:
                    cpx_status_string = "QP with non-convex objective"
                    self._model.error('Model has non-convex objective: {0!s}', str_holo(self._model.objective_expr, 60))
            elif 1016 == cpx_code:
                # this is the: CPXERR_RESTRICTED_VERSION - " Promotional version. Problem size limits exceeded." case
                cpx_status = 1016
                cpx_status_string = "Promotional version. Problem size limits exceeded., CPLEX code=1016."
                self._model.fatal(cpx_status_string)
            else:
                self.error_handler.error("CPLEX Solver Error: {0!s}", cpx_s)

        except cplex.exceptions.CplexError as cpx_e:  # pragma: no cover
            self.error_handler.error("CPLEX Error: {0!s}", cpx_e)


        finally:
            cpx_time = cpx.get_time() - cpx_time_start

        details = SolveDetails(cpx_time,
                               cpx_status, cpx_status_string,
                               cpx_probtype,
                               nb_columns, linear_nonzeros,
                               cpx_miprelgap,
                               cpx_bestbound)
        return details

    def _check_is_solved_ok(self):
        """
        INTERNAL: checks the engine has recently been solved ok.
        Either raise an exception or returns None.
        :return:
        """
        if 0 == self._solve_count:
            self._model.fatal("Model {0} is not solved yet", self._model.name)
        if not self._last_solve_status:
            self._model.fatal("Last solve failed")

    def get_solve_details(self):
        # must be solved but not necessarily ok
        return self._last_solve_details

    def _make_groups(self, relaxable_groups):
        cpx_feasopt = self._cplex.feasopt
        all_groups = []
        for (pref, group_cts) in relaxable_groups:
            if pref > 0 and group_cts:
                linears = []
                quads = []
                inds = []
                for ct in group_cts:
                    ctindex = ct.index
                    cpx_scope = ct.cplex_scope
                    if cpx_scope is CplexScope.LINEAR_CT_SCOPE:
                        linears.append(ctindex)
                    elif cpx_scope is CplexScope.IND_CT_SCOPE:
                        inds.append(ctindex)
                    elif cpx_scope is CplexScope.QUAD_CT_SCOPE:
                        quads.append(ctindex)
                    else:
                        self.error_handler.error('cannot relax this: {0!s}'.format(ct))

                if linears:
                    all_groups.append(cpx_feasopt.linear_constraints(pref, linears))
                if quads:
                    all_groups.append(cpx_feasopt.quadratic_constraints(pref, quads))
                if inds:
                    all_groups.append(cpx_feasopt.indicator_constraints(pref, inds))
        return all_groups

    ct_linear = cplex._internal._subinterfaces.FeasoptConstraintType.linear
    ct_quadratic = cplex._internal._subinterfaces.FeasoptConstraintType.quadratic
    ct_indicator = cplex._internal._subinterfaces.FeasoptConstraintType.indicator

    _scope_resolver_map = {ct_linear: lambda m_: m_._linct_scope,
                           ct_quadratic: lambda m_: m_._quadct_scope,
                           ct_indicator: lambda m_: m_._logical_scope
                           }

    def _decode_infeasibilities(self, cpx, model, cpx_relax_groups, model_scope_resolver=_scope_resolver_map):
        resolver_map = {self.ct_linear: cpx.solution.infeasibility.linear_constraints,
                        self.ct_quadratic: cpx.solution.infeasibility.quadratic_constraints,
                        self.ct_indicator: cpx.solution.infeasibility.indicator_constraints
                        }
        cpx_sol_values = cpx.solution.get_values()
        cts_by_type = defaultdict(list)
        # split and group indices by sense
        for g in cpx_relax_groups:
            # gp is a list of tuples (pref, ctsense, index)
            for t in g._gp:
                ct_sense, ct_index = t[1][0]
                cts_by_type[ct_sense].append(ct_index)

        infeas_map = {}
        for ct_sense, indices in six.iteritems(cts_by_type):
            if indices:
                resolver_fn = resolver_map[ct_sense]
                ctype_infeas = resolver_fn(cpx_sol_values, indices)
                mscope = model_scope_resolver[ct_sense](model)
                assert mscope
                for ct_index, ct_infeas in izip(indices, ctype_infeas):
                    ct = mscope.get_object_by_index(ct_index)
                    if ct is not None:
                        infeas_map[ct] = ct_infeas
        return infeas_map

    def solve_relaxed(self, mdl, prio_name, relaxable_groups, relax_mode, parameters=None):
        # INTERNAL
        self._resync_if_needed()
        self._sync_var_bounds()

        self_cplex = self._cplex
        cpx_relax_groups = self._make_groups(relaxable_groups)

        feasopt_parameters = parameters or mdl.parameters
        feasopt_override_params = {feasopt_parameters.feasopt.mode: relax_mode.value}
        with _CplexOverwriteParametersCtx(self_cplex, feasopt_override_params) as cpx:
            # at this stage, we have a list of groups
            # each group is itself a list
            # the first item is a number, the preference
            # the second item is a list of constraint indices.
            self._last_solve_details = self._run_cpx_op_with_details(cpx.feasopt, *cpx_relax_groups)


        # feasopt state is restored by now
        cpx_solution = self_cplex.solution
        feas_status = cpx_solution.get_status()
        if self._is_relaxed_status_ok(feas_status):
            infeas_map = self._decode_infeasibilities(self_cplex, mdl, cpx_relax_groups)

            # all_ct_indices = []
            # index_extend = all_ct_indices.extend
            # for _, g in relaxable_groups:
            #     index_extend(ct.safe_index for ct in g)
            # raw_infeasibilities = cpx_solution.infeasibility.linear_constraints([], all_ct_indices)
            # infeas_map = {mdl.get_constraint_by_index(ctx): raw_infeasibilities[c] for c, ctx in enumerate(all_ct_indices)}
            relaxed_sol = self._make_solution(mdl, self.get_solve_status())
            relaxed_sol.store_infeasibilities(infeas_map)
            return relaxed_sol
        else:
            # print('>>>> non-OK status: {0}'.format(feas_status))
            return None

    # def get_infeasibilities(self, cts):
    #     indices = [ct.index for ct in cts]
    #     # PCO: Daniel Junglas confirms using [] uses the last solution vector
    #     return self.__cplex.solution.infeasibility.linear_constraints([], indices)

    def _sync_parameter_defaults_from_cplex(self, parameters):
        # used when a more recent CPLEX DLL is present
        resets = []
        for param in parameters:
            cpx_value = self.get_parameter(param)
            if cpx_value != param.default_value:
                resets.append((param, param.default_value, cpx_value))
                param.reset_default_value(cpx_value)
        return resets

    def refine_conflict(self, mdl, preferences=None, groups=None, parameters=None):
        """ Starts conflict refiner on the model.

        Args:
            mdl: The model for which conflict refinement is performed.
            preferences: a dictionary defining constraints preferences.
            groups: a list of ConstraintsGroup.
            parameters: unused.

        Returns:
            A list of "TConflictConstraint" namedtuples, each tuple corresponding to a constraint that is
            involved in the conflict.
            The fields of the "TConflictConstraint" namedtuple are:
                - the name of the constraint or None if the constraint corresponds to a variable lower or upper bound
                - a reference to the constraint or to a wrapper representing a Var upper or lower bound
                - an :enum:'docplex.mp.constants.ConflictStatus' object that indicates the
                conflict status type (Excluded, Possible_member, Member...)
            This list is empty if no conflict is found by the conflict refiner.
        """

        try:
            # sync parameters
            mdl._apply_parameters_to_engine(parameters)

            cpx = self._cplex

            if groups is None or groups == []:
                all_constraints = cpx.conflict.all_constraints()
                weighted_groups = self._build_weighted_constraints(mdl, all_constraints._gp, preferences)
                cpx.conflict.refine(*weighted_groups)
            else:
                groups_def = [self._build_group_definition_with_index(grp) for grp in groups]
                cpx.conflict.refine(*groups_def)

            return self._get_conflicts_local(mdl, cpx)

        except DOcplexException as docpx_e:  # pragma: no cover
            mdl._set_solution(None)
            raise docpx_e

    def _build_group_definition_with_index(self, cts_group):
        return cts_group.preference, tuple([(self._get_constraint_type(ct), ct.index)
                                            for ct in cts_group.get_group_constraints()])

    @staticmethod
    def _get_constraint_type(ct):
        if isinstance(ct, LinearConstraint):
            return cpx_cst.CPX_CON_LINEAR
        if isinstance(ct, IndicatorConstraint):
            return cpx_cst.CPX_CON_INDICATOR
        if isinstance(ct, QuadraticConstraint):
            return cpx_cst.CPX_CON_QUADRATIC
        if isinstance(ct, VarLbConstraintWrapper):
            return cpx_cst.CPX_CON_LOWER_BOUND
        if isinstance(ct, VarUbConstraintWrapper):
            return cpx_cst.CPX_CON_UPPER_BOUND
        ct.model.fatal("Type unknown (or not supported yet) for constraint: " + repr(ct))

    def _build_weighted_constraints(self, mdl, groups, preferences=None):
        weighted_groups = []
        for (pref, seq) in groups:
            for (_type, _id) in seq:
                if _type == cpx_cst.CPX_CON_LOWER_BOUND or _type == cpx_cst.CPX_CON_UPPER_BOUND:
                    # Keep default preference
                    weighted_groups.append((pref, ((_type, _id),)))
                else:
                    ct = mdl.get_constraint_by_index(_id)
                    if preferences is not None:
                        new_pref = preferences.get(ct, None)
                        if new_pref is not None and isinstance(new_pref, numbers.Number):
                            pref = new_pref
                    weighted_groups.append((pref, ((_type, _id),)))
        return weighted_groups

    def _get_conflicts_local(self, mdl, cpx):
        # Build var by idx dict
        vars_by_index = mdl._build_index_dict(mdl._Model__allvars)

        try:
            conflicts = cpx.conflict.get()
            groups = cpx.conflict.get_groups()
        except CplexSolverError:
            # Return an empty list if no conflict is available
            return []

        result = []
        for (pref, seq), status in zip(groups, conflicts):
            if status == cpx_cst.CPX_CONFLICT_EXCLUDED:
                continue
            c_status = ConflictStatus(status)
            for (_type, _id) in seq:
                """
                Possible values for elements of grptype:
                    CPX_CON_LOWER_BOUND 	1 	variable lower bound
                    CPX_CON_UPPER_BOUND 	2 	variable upper bound
                    CPX_CON_LINEAR 	        3 	linear constraint
                    CPX_CON_QUADRATIC 	    4 	quadratic constraint
                    CPX_CON_SOS 	        5 	special ordered set
                    CPX_CON_INDICATOR 	    6 	indicator constraint
                """
                if _type == cpx_cst.CPX_CON_LOWER_BOUND:
                    result.append(TConflictConstraint(None, VarLbConstraintWrapper(vars_by_index[_id]), c_status))

                if _type == cpx_cst.CPX_CON_UPPER_BOUND:
                    result.append(TConflictConstraint(None, VarUbConstraintWrapper(vars_by_index[_id]), c_status))

                if _type == cpx_cst.CPX_CON_LINEAR:
                    ct = mdl.get_constraint_by_index(_id)
                    result.append(TConflictConstraint(ct.name, ct, c_status))

                if _type == cpx_cst.CPX_CON_QUADRATIC:
                    ct = mdl.get_quadratic_by_index(_id)
                    result.append(TConflictConstraint(ct.name, ct, c_status))

                if _type == cpx_cst.CPX_CON_SOS:
                    # TODO: DO NOT CREATE A FATAL ERROR: return a counter with a warning
                    mdl.fatal("Special Ordered Set constraints are not implemented (yet)")

                if _type == cpx_cst.CPX_CON_INDICATOR:
                    ct = mdl.get_indicator_by_index(_id)
                    result.append(TConflictConstraint(ct.name, ct, c_status))

        return result

    def dump(self, path):
        self._resync_if_needed()
        try:
            if '.' in path:
                self._cplex.write(path)
            else:
                self._cplex.write(path, filetype="lp")

        except CplexSolverError as cpx_se:  # pragma: no cover
            if cpx_se.args[2] == 1422:
                raise IOError("SAV export cannot open file: {}".format(path))
            else:
                raise DOcplexException("CPLEX error in SAV export: {0!s}", cpx_se)

    def end(self):
        """ terminate the engine, cannot find this in the doc.
        """
        del self._cplex
        self._cplex = None

    _all_mip_problems = frozenset({'MIP', 'MILP', 'fixedMILP', 'MIQP', 'fixedMIQP'})
    # noinspection PyProtectedMember
    def is_mip(self):
        cpx = self._cplex
        cpx_problem_type = cpx.problem_type[cpx.get_problem_type()]
        return cpx_problem_type in self._all_mip_problems

    def register_callback(self, cb):
        return self._cplex.register_callback(cb)

    def unregister_callback(self, cb):
        return self._cplex.unregister_callback(cb)

    def connect_progress_listeners(self, progress_listeners, model):
        if self.is_mip():
            self_ccb = self._ccb
            if progress_listeners or self_ccb:
                if self_ccb is None:
                    self._ccb = self.register_callback(ConnectListenersCallback)
                    self_ccb = self._ccb
                self_ccb.initialize(progress_listeners, model)
        elif progress_listeners:
            m = self._model
            m.warning("Model: \"{}\" is not a MIP problem, progress listeners are disabled", m.name)

    def _compute_quality_metrics(self):
        qm_dict = {}

        if self._solve_count:
            with SilencedCplexContext(self._cplex, self.error_handler) as silent_cplex:
                cpxs = silent_cplex.solution
                for qm in QualityMetric:
                    qmcode = qm.code
                    try:
                        qmf = cpxs.get_float_quality(qmcode)
                        qm_dict[qm.key] = qmf

                    except (CplexError, CplexSolverError):
                        pass
                    if qm.has_int:
                        try:
                            qmi = cpxs.get_integer_quality(qmcode)
                            if qmi >= 0:
                                # do something with int parameter?
                                qm_dict[qm.int_key] = qmi
                        except (CplexError, CplexSolverError):
                            pass
        else:
            self._model.error('Model has not been solved: no quality metrics available.')
        return qm_dict

    def set_parameters(self, parameters):
        # INTERNAL
        # parameters is a root parameter group from DOcplex
        cpx_params = self.__cplex._env.parameters
        for param in parameters:
            try:
                cpx_params.set(param.cpx_id, param.current_value)

            except CplexError as cpxe:
                cpx_msg = str(cpxe)
                if cpx_msg.startswith("Bad parameter identifier"):
                    self.error_handler.warning("Parameter \"{0}\" is not recognized",
                                               (param.qualified_name,))
                else:
                    self.error_handler.error("Error setting parameter {0} to value {1}"
                                             .format(param.short_name, param.current_value))

    def set_parameter(self, parameter, value):
        # value check is up to the caller.
        # parameter is a DOcplex parameter object
        try:
            self._cplex._env.parameters._set(parameter.cpx_id, value)
        except CplexError as cpx_e:
            cpx_msg = str(cpx_e)
            if cpx_msg.startswith("Bad parameter identifier"):
                self.error_handler.warning("Parameter \"{0}\" is not recognized", (parameter.qualified_name,))
            else:  # pragma: no cover
                self.error_handler.error("Error setting parameter {0} (id: {1}) to value {2}"
                                         .format(parameter.short_name,
                                                 parameter.cpx_id,
                                                 value))

    def get_parameter(self, parameter):
        try:
            return self._cplex._env.parameters._get(parameter.cpx_id)
        except CplexError:  # pragma: no cover
            return parameter.default_value

    def get_solve_status(self):  # pragma: no cover
        from docplex.util.status import JobSolveStatus
        # In this function we try to do the exact same mappings as the IloCplex C++ and Java classes.
        # However, this is not always possible since the C++ and Java implementations are not consistent
        # and sometimes they are even in error (see RTC-21923).

        cpx_status = self._cplex.solution.get_status()
        # what status for relaxed solutions??
        relaxed_solution_status = JobSolveStatus.INFEASIBLE_SOLUTION
        #
        if cpx_status in {cpx_cst.CPXMIP_ABORT_FEAS,
                          cpx_cst.CPXMIP_DETTIME_LIM_FEAS,
                          cpx_cst.CPXMIP_FAIL_FEAS,
                          cpx_cst.CPXMIP_FAIL_FEAS_NO_TREE,
                          cpx_cst.CPXMIP_MEM_LIM_FEAS,
                          cpx_cst.CPXMIP_NODE_LIM_FEAS,
                          cpx_cst.CPXMIP_TIME_LIM_FEAS
                          }:
            return JobSolveStatus.FEASIBLE_SOLUTION

        elif cpx_status in {cpx_cst.CPXMIP_ABORT_INFEAS,
                            cpx_cst.CPXMIP_DETTIME_LIM_INFEAS,
                            cpx_cst.CPXMIP_FAIL_INFEAS,
                            cpx_cst.CPXMIP_FAIL_INFEAS_NO_TREE,
                            cpx_cst.CPXMIP_MEM_LIM_INFEAS,
                            cpx_cst.CPXMIP_NODE_LIM_INFEAS,
                            cpx_cst.CPXMIP_TIME_LIM_INFEAS
                            }:
            # Hit a limit without a feasible solution: We don't know anything about the solution.
            return JobSolveStatus.UNKNOWN
        elif cpx_status in {cpx_cst.CPXMIP_OPTIMAL,
                            cpx_cst.CPXMIP_OPTIMAL_TOL,
                            DEFAULT_CPX_STAT_MULTIOBJ_OPTIMAL}:
            return JobSolveStatus.OPTIMAL_SOLUTION
        elif cpx_status is cpx_cst.CPXMIP_SOL_LIM:
            #  return hasSolution(env, lp) ? JobSolveStatus.FEASIBLE_SOLUTION : JobSolveStatus.UNKNOWN;
            return JobSolveStatus.FEASIBLE_SOLUTION
        elif cpx_status in {cpx_cst.CPXMIP_INForUNBD,
                            DEFAULT_CPX_STAT_MULTIOBJ_INForUNBD}:
            return JobSolveStatus.INFEASIBLE_OR_UNBOUNDED_SOLUTION
        elif cpx_status in {cpx_cst.CPXMIP_UNBOUNDED,
                            cpx_cst.CPXMIP_ABORT_RELAXATION_UNBOUNDED,
                            DEFAULT_CPX_STAT_MULTIOBJ_UNBOUNDED}:
            return JobSolveStatus.UNBOUNDED_SOLUTION
        elif cpx_status in {cpx_cst.CPXMIP_INFEASIBLE,
                            DEFAULT_CPX_STAT_MULTIOBJ_INFEASIBLE}:  # proven infeasible
            return JobSolveStatus.INFEASIBLE_SOLUTION
        elif cpx_status == cpx_cst.CPXMIP_OPTIMAL_INFEAS:  # optimal with unscaled infeasibilities
            # DANIEL: What exactly do we return here? There is an optimal solution but that solution is
            # infeasible after unscaling.
            return JobSolveStatus.OPTIMAL_SOLUTION

        # feasopt status values
        elif cpx_status in frozenset({
            cpx_cst.CPXMIP_ABORT_RELAXED,  # relaxed solution is available and can be queried
            cpx_cst.CPXMIP_FEASIBLE  # problem feasible after phase I and solution available
        }):
            return JobSolveStatus.FEASIBLE_SOLUTION
        ## -----------------
        ## relaxation (feasopt) there is a relaxed (but infeasible) solution
        ## for now we choose to return INFEASIBLE_SOLUTION
        ##
        elif cpx_status in {cpx_cst.CPXMIP_FEASIBLE_RELAXED_INF,
                            cpx_cst.CPXMIP_FEASIBLE_RELAXED_QUAD,
                            cpx_cst.CPXMIP_FEASIBLE_RELAXED_SUM
                            }:
            return relaxed_solution_status
        elif cpx_status in {cpx_cst.CPXMIP_OPTIMAL_RELAXED_INF,
                            cpx_cst.CPXMIP_OPTIMAL_RELAXED_QUAD,
                            cpx_cst.CPXMIP_OPTIMAL_RELAXED_SUM
                            }:
            return relaxed_solution_status
        elif cpx_status in {cpx_cst.CPX_STAT_FEASIBLE_RELAXED_INF,
                            cpx_cst.CPX_STAT_FEASIBLE_RELAXED_QUAD,
                            cpx_cst.CPX_STAT_FEASIBLE_RELAXED_SUM,
                            }:
            return relaxed_solution_status
        elif cpx_status in {cpx_cst.CPX_STAT_OPTIMAL_RELAXED_INF,
                            cpx_cst.CPX_STAT_OPTIMAL_RELAXED_QUAD,
                            cpx_cst.CPX_STAT_OPTIMAL_RELAXED_SUM}:
            return relaxed_solution_status

        ## -------------------

        # populate status values
        elif cpx_status in {cpx_cst.CPXMIP_OPTIMAL_POPULATED
                            # ,cpx_cst.CPXMIP_OPTIMAL_POPULATED_TO
                            }:
            return JobSolveStatus.OPTIMAL_SOLUTION
        elif cpx_status == cpx_cst.CPXMIP_POPULATESOL_LIM:
            # minimal value for CPX_PARAM_POPULATE_LIM is 1! So there must be a solution
            return JobSolveStatus.FEASIBLE_SOLUTION

        elif cpx_status == cpx_cst.CPX_STAT_OPTIMAL:
            return JobSolveStatus.OPTIMAL_SOLUTION

        elif cpx_status == cpx_cst.CPX_STAT_INFEASIBLE:
            return JobSolveStatus.INFEASIBLE_SOLUTION

        # cpx_cst.CPX_STAT_ABORT_USER:
        # cpx_cst.CPX_STAT_ABORT_DETTIME_LIM:
        # cpx_cst.CPX_STAT_ABORT_DUAL_OBJ_LIM:
        # cpx_cst.CPX_STAT_ABORT_IT_LIM:
        # cpx_cst.CPX_STAT_ABORT_PRIM_OBJ_LIM:
        # cpx_cst.CPX_STAT_ABORT_TIME_LIM:
        #   switch (primalDualFeasible(env, lp)) {
        #   case PRIMAL_FEASIBLE: return JobSolveStatus.FEASIBLE_SOLUTION
        #   case PRIMAL_DUAL_FEASIBLE: return JobSolveStatus.OPTIMAL_SOLUTION
        #   case DUAL_FEASIBLE: return JobSolveStatus.UNKNOWN;
        #   default: return JobSolveStatus.UNKNOWN;
        #   }
        #
        # cpx_cst.CPX_STAT_ABORT_OBJ_LIM:
        #   /** DANIEL: Our Java API returns ERROR here while the C++ API returns Feasible if primal feasible
        #    *         and Unknown otherwise. Since we don't have ERROR in IloSolveStatus we emulate the
        #    *         C++ behavior (this is more meaningful anyway). In the long run we should make sure
        #    *         all the APIs behave in the same way.
        #    */
        #   switch (primalDualFeasible(env, lp)) {
        #   case PRIMAL_FEASIBLE: return JobSolveStatus.FEASIBLE_SOLUTION
        #   case PRIMAL_DUAL_FEASIBLE: return JobSolveStatus.FEASIBLE_SOLUTION
        #   default: return JobSolveStatus.UNKNOWN;
        #   }
        #
        # cpx_cst.CPX_STAT_FIRSTORDER:
        #   // See IloCplexI::CplexToAlgorithmStatus()
        #   return primalFeasible(env, lp) ? JobSolveStatus.FEASIBLE_SOLUTION : JobSolveStatus.UNKNOWN;

        elif cpx_status == cpx_cst.CPX_STAT_CONFLICT_ABORT_CONTRADICTION:
            # Numerical trouble in conflict refiner.
            #  DANIEL: C++ and Java both return Error here although a conflict is
            #          available (but nor proven to be minimal). This looks like a bug
            #          since no exception is thrown there. In IloSolveStatus we don't
            #          have ERROR, so we return UNKNOWN instead. This is fine for now
            #          since we do not support the conflict refiner anyway.
            #
            return JobSolveStatus.UNKNOWN

        elif cpx_status in {

            cpx_cst.CPX_STAT_CONFLICT_ABORT_DETTIME_LIM,
            cpx_cst.CPX_STAT_CONFLICT_ABORT_IT_LIM,
            cpx_cst.CPX_STAT_CONFLICT_ABORT_MEM_LIM,
            cpx_cst.CPX_STAT_CONFLICT_ABORT_NODE_LIM,
            cpx_cst.CPX_STAT_CONFLICT_ABORT_OBJ_LIM,
            cpx_cst.CPX_STAT_CONFLICT_ABORT_TIME_LIM,
            cpx_cst.CPX_STAT_CONFLICT_ABORT_USER
        }:
            # /** DANIEL: C++ and Java return Error here. This is almost certainly wrong.
            # *         Docs say "a conflict is available but not minimal".
            #  *         This is particularly erroneous if no exception gets thrown.
            #  *         See RTC-21923.
            #  *         In IloSolveStatus we don't have ERROR, so we return UNKNOWN instead.
            #  *         This should not be a problem since right now we don't support the
            #  *         conflict refiner anyway.
            #  */
            return JobSolveStatus.UNKNOWN
        elif cpx_status == cpx_cst.CPX_STAT_CONFLICT_FEASIBLE:
            return JobSolveStatus.FEASIBLE_SOLUTION
        elif cpx_status == cpx_cst.CPX_STAT_CONFLICT_MINIMAL:
            return JobSolveStatus.INFEASIBLE_SOLUTION

        elif cpx_status == cpx_cst.CPX_STAT_FEASIBLE:
            return JobSolveStatus.FEASIBLE_SOLUTION

        elif cpx_status == cpx_cst.CPX_STAT_NUM_BEST:
            #  Solution available but not proved optimal (due to numeric difficulties)
            # assert(hasSolution(env, lp));
            return JobSolveStatus.UNKNOWN

        elif cpx_status == cpx_cst.CPX_STAT_OPTIMAL_INFEAS:  # infeasibilities after unscaling
            # assert(hasSolution(env, lp));
            return JobSolveStatus.OPTIMAL_SOLUTION

        elif cpx_status == cpx_cst.CPX_STAT_INForUNBD:  # Infeasible or unbounded in presolve.
            return JobSolveStatus.INFEASIBLE_OR_UNBOUNDED_SOLUTION
        elif cpx_status == cpx_cst.CPX_STAT_OPTIMAL_FACE_UNBOUNDED:
            #    unbounded optimal face (barrier only)
            # // CPX_STAT_OPTIMAL_FACE_UNBOUNDED is explicitly an error in Java and implicitly (fallthrough)
            # // an error in C++. So it should be fine to produce an error here as well.
            # // In IloSolveStatus we don't have ERROR, so we return UNKNOWN instead.
            # // In case of ERROR we should have seen a non-zero status anyway and the
            # // user should not care too much about the returned status.
            return JobSolveStatus.UNKNOWN
        elif cpx_status == cpx_cst.CPX_STAT_UNBOUNDED:
            # definitely unbounded
            return JobSolveStatus.UNBOUNDED_SOLUTION
        elif cpx_status == DEFAULT_CPX_STAT_MULTIOBJ_NON_OPTIMAL:
            # Solution available but not proved optimal
            return JobSolveStatus.FEASIBLE_SOLUTION
        elif cpx_status == DEFAULT_CPX_STAT_MULTIOBJ_STOPPED:
            # The solve of a multi-objective problem was interrupted (a global work limit was hit or solution process
            # was aborted)
            return JobSolveStatus.UNKNOWN
        else:
            return JobSolveStatus.UNBOUNDED_SOLUTION

    def _resync_if_needed(self):
        if self._resync is _CplexSyncMode.OutOfSync:
            # print("-- resync cplex from model...")
            # send whole model to engine.
            try:
                self._resync = _CplexSyncMode.InResync
                self._model._resync()
            finally:
                self._resync = _CplexSyncMode.InSync


@contextmanager
def overload_cplex_parameter_values(cpx_engine, overload_dict):
    old_values = {p: p.get() for p in overload_dict}
    try:
        yield cpx_engine
    finally:
        # restore params
        for p, saved_value in six.iteritems(old_values):
            p.set(saved_value)


def unpickle_cplex_engine(mdl, is_traced):
    #  INTERNAL
    unpicking_env = Environment()
    if unpicking_env.has_cplex:
        cplex_engine = CplexEngine(mdl)
        cplex_engine.set_streams(sys.stdout if is_traced else None)  # what to do if file??
        # mark to be resync'ed
        cplex_engine._mark_as_out_of_sync()
        return cplex_engine
    else:
        return NoSolveEngine.make_from_model(mdl)


unpickle_cplex_engine.__safe_for_unpickling__ = True


def pickle_cplex_engine(cplex_engine):
    model = cplex_engine._model
    return unpickle_cplex_engine, (model, model.is_logged())


copyreg.pickle(CplexEngine, pickle_cplex_engine)
