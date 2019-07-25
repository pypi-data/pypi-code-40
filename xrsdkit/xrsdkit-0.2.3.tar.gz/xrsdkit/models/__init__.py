import os
from collections import OrderedDict
from distutils.dir_util import copy_tree
import shutil

import yaml

from .. import definitions as xrsdefs 
from .regressor import Regressor
from .classifier import Classifier

_regression_models = {}
_classification_models = {}
_reg_conf = {}
_cl_conf = {}

def get_regression_models():
    return _regression_models

def get_classification_models():
    return _classification_models

def get_reg_conf():
    return _reg_conf

def get_cl_conf():
    return _cl_conf

def load_models(models_dir):
    """load models and configs from provided directory"""
    global _regression_models
    global _classification_models
    global _reg_conf
    global _cl_conf
    cl_dir = os.path.join(models_dir,'classifiers')
    reg_dir = os.path.join(models_dir,'regressors')
    _classification_models, _cl_conf = load_classification_models(cl_dir)
    _regression_models, _reg_conf = load_regression_models(reg_dir)

def load_model_from_files(yml_file, pickle_file, model_type):
    """Build a xrsdkit.models.xrsd_model.XRSDModel from serialized model data.

    Parameters
    ----------
    yml_file : str
        absolute path to yml file generated by yaml.dump(XRSDModel.collect_model_data()) 
    pickle_file : str
        absolute path to pickle file generated by pickle.dump(XRSDModel.model) 
    model_type : str
        either 'classifier' or 'regressor'

    Returns
    -------
    modl : xrsdkit.models.xrsd_model.XRSDModel
        Either a xrsdkit Classifier or a xrsdkit Regressor,
        depending on the inputs provided
    """
    ymlf = open(yml_file,'rb')
    content = yaml.load(ymlf, Loader=yaml.Loader)
    ymlf.close()
    if model_type == 'classifier':
        modl = Classifier(content['model_type'], content['metric'], content['model_target'])
    elif model_type == 'regressor':
        modl = Regressor(content['model_type'], content['metric'], content['model_target'])
    else:
        raise ValueError('unrecognized model type: {}'.format(model_type))
    modl.load_model_data(content, pickle_file)
    return modl

def load_classification_models(model_root_dir):  
    model_dict = OrderedDict()
    conf = OrderedDict()
    if not os.path.exists(model_root_dir):
        msg = 'tried to load classifiers from nonexistent directory {}'.format(model_root_dir) 
        raise RuntimeError(msg)
    all_sys_cls = os.listdir(model_root_dir)
    # this next line filters out hidden files
    all_sys_cls = [i for i in all_sys_cls if not i[0]=='.']

    # the top-level classifier is a collection of classifiers;
    # their cumulative effect is to find the number of distinct populations
    # for each structure
    main_cls_path =  os.path.join(model_root_dir, 'main_classifiers')
    model_dict['main_classifiers'] = {}
    conf['main_classifiers'] = {}
    if os.path.exists(main_cls_path):
        all_main_cls = os.listdir(main_cls_path)
        # this next line filters out hidden files
        all_main_cls = [i for i in all_main_cls if not i[0]=='.']
        all_main_cls = [cl for cl in all_main_cls if cl.endswith('.yml')]
        for cl in all_main_cls:
            cl_name = os.path.splitext(cl)[0]
            yml_path = os.path.join(main_cls_path, cl)
            pickle_path =  os.path.join(main_cls_path, cl_name+'.pickle')
            model = load_model_from_files(yml_path, pickle_path, 'classifier')
            model_dict['main_classifiers'][cl_name] = model
            conf['main_classifiers'][cl_name] = dict(model_type=model.model_type, metric=model.metric)

    if 'main_classifiers' in all_sys_cls: all_sys_cls.remove('main_classifiers')
    for sys_cls in all_sys_cls:
        model_dict[sys_cls] = {}
        conf[sys_cls] = {}
        sys_cls_dir = os.path.join(model_root_dir,sys_cls)
        noise_yml_path = os.path.join(sys_cls_dir,'noise_model.yml')
        if os.path.exists(noise_yml_path):
            pickle_path = os.path.join(sys_cls_dir,'noise_model.pickle')
            model = load_model_from_files(noise_yml_path, pickle_path, 'classifier')
            model_dict[sys_cls]['noise_model'] = model
            conf[sys_cls]['noise_model'] = dict(model_type=model.model_type, metric=model.metric)

        for ipop,struct in enumerate(sys_cls.split('__')):
            pop_id = 'pop{}'.format(ipop)
            pop_dir = os.path.join(sys_cls_dir,pop_id)
            model_dict[sys_cls][pop_id] = {}
            conf[sys_cls][pop_id] = {}

            # each population must have a form classifier
            form_yml_path = os.path.join(pop_dir,'form.yml')
            if os.path.exists(form_yml_path):
                pickle_path = os.path.join(pop_dir,'form.pickle')
                model = load_model_from_files(form_yml_path, pickle_path, 'classifier')
                model_dict[sys_cls][pop_id]['form'] = model
                conf[sys_cls][pop_id]['form'] = dict(model_type=model.model_type, metric=model.metric)

            # other classifiers in this directory are for structure settings
            for stg_nm in xrsdefs.modelable_structure_settings[struct]:
                stg_yml_path = os.path.join(pop_dir,stg_nm+'.yml')
                if os.path.exists(stg_yml_path):
                    pickle_path = os.path.join(pop_dir,stg_nm+'.pickle')
                    model = load_model_from_files(stg_yml_path, pickle_path, 'classifier')
                    model_dict[sys_cls][pop_id][stg_nm] = model
                    conf[sys_cls][pop_id][stg_nm] = dict(model_type=model.model_type, metric=model.metric)

            # some additional directories may exist for form factor settings-
            # these would be named according to their form factors
            for ffnm in xrsdefs.form_factor_names:
                ff_dir = os.path.join(pop_dir,ffnm)
                if os.path.exists(ff_dir):
                    model_dict[sys_cls][pop_id][ffnm] = {}
                    conf[sys_cls][pop_id][ffnm] = {}
                    for stg_nm in xrsdefs.modelable_form_factor_settings[ffnm]:
                        stg_yml_path = os.path.join(ff_dir,stg_nm+'.yml')
                        if os.path.exists(stg_yml_path):
                            pickle_path = os.path.join(ff_dir,stg_nm+'.pickle')
                            model = load_model_from_files(stg_yml_path, pickle_path, 'classifier')
                            model_dict[sys_cls][pop_id][ffnm][stg_nm] = model
                            conf[sys_cls][pop_id][ffnm][stg_nm] = dict(model_type=model.model_type, metric=model.metric)
    return model_dict, conf

def load_regression_models(model_root_dir):
    model_dict = OrderedDict()
    conf = OrderedDict()
    if not os.path.exists(model_root_dir):
        msg = 'tried to load regressors from nonexistent directory {}'.format(model_root_dir) 
        raise RuntimeError(msg)

    all_sys_cls = os.listdir(model_root_dir)
    # this next line filters out hidden files
    all_sys_cls = [i for i in all_sys_cls if not i[0]=='.']
    for sys_cls in all_sys_cls:
        model_dict[sys_cls] = {}
        conf[sys_cls] = {}
        sys_cls_dir = os.path.join(model_root_dir,sys_cls)

        # every system class must have some noise parameters
        noise_dir = os.path.join(sys_cls_dir,'noise')
        model_dict[sys_cls]['noise'] = {}
        conf[sys_cls]['noise'] = {}
        for modnm in xrsdefs.noise_model_names:
            noise_model_dir = os.path.join(noise_dir,modnm)
            if os.path.exists(noise_model_dir):
                model_dict[sys_cls]['noise'][modnm] = {}
                conf[sys_cls]['noise'][modnm] = {}
                for pnm in list(xrsdefs.noise_params[modnm].keys())+['I0_fraction']:
                    param_yml_file = os.path.join(noise_model_dir,pnm+'.yml')
                    if os.path.exists(param_yml_file):
                        pickle_path = os.path.join(noise_model_dir,pnm+'.pickle')
                        model = load_model_from_files(param_yml_file, pickle_path, 'regressor')
                        model_dict[sys_cls]['noise'][modnm][pnm] = model
                        conf[sys_cls]['noise'][modnm][pnm] = dict(model_type=model.model_type, metric=model.metric)

        for ipop,struct in enumerate(sys_cls.split('__')):
            pop_id = 'pop{}'.format(ipop)
            model_dict[sys_cls][pop_id] = {}
            conf[sys_cls][pop_id] = {}
            pop_dir = os.path.join(sys_cls_dir,pop_id)

            # each population must have a model for its I0_fraction 
            I0_fraction_yml = os.path.join(pop_dir,'I0_fraction.yml')
            if os.path.exists(I0_fraction_yml):
                pickle_path = os.path.join(pop_dir,'I0_fraction.pickle')
                model = load_model_from_files(I0_fraction_yml, pickle_path, 'regressor')
                model_dict[sys_cls][pop_id]['I0_fraction'] = model
                conf[sys_cls][pop_id]['I0_fraction'] = dict(model_type=model.model_type, metric=model.metric)

            # each population may have additional parameters,
            # depending on settings
            for stg_nm in xrsdefs.modelable_structure_settings[struct]:
                stg_dir = os.path.join(pop_dir,stg_nm)
                if os.path.exists(stg_dir):
                    model_dict[sys_cls][pop_id][stg_nm] = {}
                    conf[sys_cls][pop_id][stg_nm] = {}
                    all_stg_labels = os.listdir(stg_dir)
                    # this next line filters out hidden files
                    all_stg_labels = [i for i in all_stg_labels if not i[0]=='.']
                    for stg_label in all_stg_labels:
                        stg_label_dir = os.path.join(stg_dir,stg_label)
                        if os.path.exists(stg_label_dir):
                            model_dict[sys_cls][pop_id][stg_nm][stg_label] = {}
                            conf[sys_cls][pop_id][stg_nm][stg_label] = {}
                            for pnm in xrsdefs.structure_params(struct,{stg_nm:stg_label}):
                                param_yml = os.path.join(stg_label_dir,pnm+'.yml')
                                pickle_path = os.path.join(stg_label_dir,pnm+'.pickle')
                                model = load_model_from_files(param_yml, pickle_path, 'regressor')
                                model_dict[sys_cls][pop_id][stg_nm][stg_label][pnm] = model
                                conf[sys_cls][pop_id][stg_nm][stg_label][pnm] = dict(model_type=model.model_type, metric=model.metric)

            # each population may have still more parameters,
            # depending on the form factor selection
            for ff_nm in xrsdefs.form_factor_names:
                ff_dir = os.path.join(pop_dir,ff_nm)
                if os.path.exists(ff_dir):
                    model_dict[sys_cls][pop_id][ff_nm] = {}
                    conf[sys_cls][pop_id][ff_nm] = {}
                    for pnm in xrsdefs.form_factor_params[ff_nm]:
                        param_yml = os.path.join(ff_dir,pnm+'.yml')
                        pickle_path = os.path.join(ff_dir,pnm+'.pickle')
                        model = load_model_from_files(param_yml, pickle_path, 'regressor')
                        model_dict[sys_cls][pop_id][ff_nm][pnm] = model
                        conf[sys_cls][pop_id][ff_nm][pnm] = dict(model_type=model.model_type, metric=model.metric)

                # the final layer of parameters depends on form factor settings
                for stg_nm in xrsdefs.modelable_form_factor_settings[ff_nm]:
                    stg_dir = os.path.join(ff_dir,stg_nm)
                    if os.path.exists(stg_dir): 
                        model_dict[sys_cls][pop_id][ff_nm][stg_nm] = {}
                        conf[sys_cls][pop_id][ff_nm][stg_nm] = {}
                        all_stg_labels = os.listdir(stg_dir)
                        # this next line filters out hidden files
                        all_stg_labels = [i for i in all_stg_labels if not i[0]=='.']
                        for stg_label in all_stg_labels:
                            stg_label_dir = os.path.join(stg_dir,stg_label)
                            if os.path.exists(stg_label_dir):
                                model_dict[sys_cls][pop_id][ff_nm][stg_nm][stg_label] = {}
                                conf[sys_cls][pop_id][ff_nm][stg_nm][stg_label] = {}
                                for pnm in xrsdefs.additional_form_factor_params(ff_nm,{stg_nm:stg_label}):
                                    param_yml = os.path.join(stg_label_dir,pnm+'.yml')
                                    pickle_path = os.path.join(stg_label_dir,pnm+'.pickle')
                                    model = load_model_from_files(param_yml, pickle_path, 'regressor')
                                    model_dict[sys_cls][pop_id][ff_nm][stg_nm][stg_label][pnm] = model
                                    conf[sys_cls][pop_id][ff_nm][stg_nm][stg_label][pnm] = dict(model_type=model.model_type, metric=model.metric)
    return model_dict, conf

