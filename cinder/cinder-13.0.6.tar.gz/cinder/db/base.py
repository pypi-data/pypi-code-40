# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Base class for classes that need modular database access."""


from oslo_config import cfg
from oslo_utils import importutils
import six


db_driver_opt = cfg.StrOpt('db_driver',
                           default='cinder.db',
                           help='Driver to use for database access')

CONF = cfg.CONF
CONF.register_opt(db_driver_opt)


class Base(object):
    """DB driver is injected in the init method."""

    def __init__(self, db_driver=None):
        # NOTE(mriedem): Without this call, multiple inheritance involving
        # the db Base class does not work correctly.
        super(Base, self).__init__()
        if not db_driver:
            db_driver = CONF.db_driver

        # pylint: disable=C0103
        if isinstance(db_driver, six.string_types):
            self.db = importutils.import_module(db_driver)
        else:
            self.db = db_driver
        self.db.dispose_engine()
