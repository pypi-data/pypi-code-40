# coding=utf-8
from __future__ import absolute_import, print_function

import importlib
import os


def _importModule(name):
    try:
        return importlib.import_module(name)
    except ModuleNotFoundError:
        return None


def _importAttr(name):
    module_name, component_name = name.replace(os.sep, ".").rsplit(".", 1)
    module = importlib.import_module(module_name)
    try:
        return getattr(module, component_name)
    except AttributeError:
        return None


def importModule(name):
    module = _importModule(name)
    if module is None:
        raise Exception("Module not found: {}".format(name))
    return module


def _importVariable(name):
    moduleName, componentName = name.replace(os.sep, ".").rsplit(".", 1)
    module = importModule(moduleName)
    return getattr(module, componentName, None)


def importVariable(name):
    variable = _importVariable(name)
    if variable is None:
        raise Exception("Variable not found: {}".format(name))
    return variable


def _imports(name):
    obj = _importModule(name) or _importVariable(name)
    if obj is None:
        raise Exception("Import Error: {}".format(name))
    return obj


def imports(*names):
    objs = tuple(_imports(name) for name in names)
    return objs[0] if len(objs) == 1 else objs
