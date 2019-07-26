# Copyright (c) 2011 Zadara Storage Inc.
# Copyright (c) 2011 OpenStack Foundation
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

"""The volume type & volume types extra specs extension."""

import ast
from webob import exc

from oslo_log import log as logging
from oslo_utils import strutils

from cinder.api import common
from cinder.api import microversions as mv
from cinder.api.openstack import wsgi
from cinder.api.v2.views import types as views_types
from cinder import exception
from cinder.i18n import _
from cinder.policies import volume_type as type_policy
from cinder import utils
from cinder.volume import volume_types

LOG = logging.getLogger(__name__)


class VolumeTypesController(wsgi.Controller):
    """The volume types API controller for the OpenStack API."""

    _view_builder_class = views_types.ViewBuilder

    def index(self, req):
        """Returns the list of volume types."""
        context = req.environ['cinder.context']
        context.authorize(type_policy.GET_ALL_POLICY)
        limited_types = self._get_volume_types(req)

        req.cache_resource(limited_types, name='types')
        return self._view_builder.index(req, limited_types)

    def show(self, req, id):
        """Return a single volume type item."""
        context = req.environ['cinder.context']

        # get default volume type
        if id is not None and id == 'default':
            vol_type = volume_types.get_default_volume_type()
            if not vol_type:
                msg = _("Default volume type can not be found.")
                raise exception.VolumeTypeNotFound(message=msg)
            req.cache_resource(vol_type, name='types')
        else:
            # Not found  exception will be handled at wsgi level
            vol_type = volume_types.get_volume_type(context, id)
            req.cache_resource(vol_type, name='types')
        context.authorize(type_policy.GET_POLICY, target_obj=vol_type)
        return self._view_builder.show(req, vol_type)

    def _parse_is_public(self, is_public):
        """Parse is_public into something usable.

        * True: List public volume types only
        * False: List private volume types only
        * None: List both public and private volume types
        """

        if is_public is None:
            # preserve default value of showing only public types
            return True
        elif utils.is_none_string(is_public):
            return None
        else:
            try:
                return strutils.bool_from_string(is_public, strict=True)
            except ValueError:
                msg = _('Invalid is_public filter [%s]') % is_public
                raise exc.HTTPBadRequest(explanation=msg)

    @common.process_general_filtering('volume_type')
    def _process_volume_type_filtering(self, context=None, filters=None,
                                       req_version=None):
        utils.remove_invalid_filter_options(context,
                                            filters,
                                            self._get_vol_type_filter_options()
                                            )

    def _get_volume_types(self, req):
        """Helper function that returns a list of type dicts."""
        params = req.params.copy()
        marker, limit, offset = common.get_pagination_params(params)
        sort_keys, sort_dirs = common.get_sort_params(params)
        filters = params
        context = req.environ['cinder.context']
        req_version = req.api_version_request
        if req_version.matches(mv.SUPPORT_VOLUME_TYPE_FILTER):
            self._process_volume_type_filtering(context=context,
                                                filters=filters,
                                                req_version=req_version)
        else:
            utils.remove_invalid_filter_options(
                context, filters, self._get_vol_type_filter_options())
        if context.is_admin:
            # Only admin has query access to all volume types
            filters['is_public'] = self._parse_is_public(
                req.params.get('is_public', None))
        else:
            filters['is_public'] = True
        if 'extra_specs' in filters:
            try:
                filters['extra_specs'] = ast.literal_eval(
                    filters['extra_specs'])
            except (ValueError, SyntaxError):
                LOG.debug('Could not evaluate "extra_specs" %s, assuming '
                          'dictionary string.', filters['extra_specs'])
        limited_types = volume_types.get_all_types(context,
                                                   filters=filters,
                                                   marker=marker, limit=limit,
                                                   sort_keys=sort_keys,
                                                   sort_dirs=sort_dirs,
                                                   offset=offset,
                                                   list_result=True)
        return limited_types

    def _get_vol_type_filter_options(self):
        """Return volume type search options allowed by non-admin."""
        return ['is_public']


def create_resource():
    return wsgi.Resource(VolumeTypesController())
