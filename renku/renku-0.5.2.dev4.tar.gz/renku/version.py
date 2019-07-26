# -*- coding: utf-8 -*-
#
# Copyright 2017-%d - Swiss Data Science Center (SDSC)
# A partnership between École Polytechnique Fédérale de Lausanne (EPFL) and
# Eidgenössische Technische Hochschule Zürich (ETHZ).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Version information for Renku."""

__version__ = '0.5.2.dev4'


def _get_disribution_url():
    import pkg_resources
    d = pkg_resources.get_distribution('renku')
    metadata = d._get_metadata(d.PKG_INFO)
    home_page = [m for m in metadata if m.startswith('Home-page:')]
    return home_page[0].split(':', 1)[1].strip()


version_url = '{}/tree/{}'.format(_get_disribution_url(), 'v' + __version__)
