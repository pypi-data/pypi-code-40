# -*- coding: utf-8 -*-
# Copyright (C) 2013-2019 Team tiramisu (see AUTHORS for all contributors)
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ____________________________________________________________
"""Sqlite3 plugin for storage. This storage is not made to be used in productive
environment. It was developing as proof of concept.

You should not configure differents Configs with same session_id.

"""
from .value import Values
from .setting import Properties, Permissives
from .storage import PERSISTENT, SETTING, Storage, list_sessions


__all__ = ('PERSISTENT',
           'SETTING',
           'Values',
           'Properties',
           'Permissives',
           'Storage',
           'list_sessions')
