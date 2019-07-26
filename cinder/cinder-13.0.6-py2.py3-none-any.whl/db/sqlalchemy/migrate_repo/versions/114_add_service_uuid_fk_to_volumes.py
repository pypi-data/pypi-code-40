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

from sqlalchemy import Column
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy import ForeignKey
from sqlalchemy import Index
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table


def upgrade(migrate_engine):
    """Add service_uuid column to volumes."""
    meta = MetaData(bind=migrate_engine)

    Table('services', meta, autoload=True)
    volumes = Table('volumes', meta, autoload=True)
    if not hasattr(volumes.c, 'service_uuid'):
        volumes.create_column(Column('service_uuid', String(36),
                                     ForeignKey('services.uuid'),
                                     nullable=True))

    index_name = 'volumes_service_uuid_idx'
    indexes = Inspector(migrate_engine).get_indexes('volumes')
    if index_name not in (i['name'] for i in indexes):
        volumes = Table('volumes', meta, autoload=True)
        Index(index_name, volumes.c.service_uuid, volumes.c.deleted).create()
