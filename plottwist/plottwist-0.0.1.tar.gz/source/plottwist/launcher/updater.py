#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains implementation for Plot Twist Artella updater
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os

from tpPyUtils import path as path_utils

from artellalauncher.core import defines, updater as core_updater

import plottwist


def get_updater_config_path():
    """
    Returns path where default Artella updater config is located
    :return: str
    """

    return path_utils.clean_path(os.path.join(plottwist.get_project_path(), defines.ARTELLA_UPDATER_CONFIG_FILE_NAME))


class PlotTwistUpdater(core_updater.ArtellaUpdater, object):

    UPDATER_CONFIG_PATH = get_updater_config_path()

    def __init__(self, launcher, parent=None):
        super(PlotTwistUpdater, self).__init__(launcher=launcher, parent=parent)