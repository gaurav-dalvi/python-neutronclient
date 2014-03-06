# Copyright 2014 OpenStack Foundation.
# All Rights Reserved
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import logging
import string

from neutronclient.common import utils
from neutronclient.neutron import v2_0 as neutronv20
from neutronclient.openstack.common.gettextutils import _


def _format_members(connectivitygroup):
    try:
        return '\n'.join([utils.dumps(member) for member in
                          connectivitygroup['members']])
    except Exception:
        return ''


class ListConnectivityGroup(neutronv20.ListCommand):
    """List connectivity groups."""

    resource = 'connectivity_group'
    log = logging.getLogger(__name__ + '.ListConnectivityGroup')
    _formatters = {'members': _format_members, }
    list_columns = ['id', 'name', 'members']
    pagination_support = True
    sorting_support = True


class ShowConnectivityGroup(neutronv20.ShowCommand):
    """Show information of a given connectivity group."""

    resource = 'connectivity_group'
    log = logging.getLogger(__name__ + '.ShowConnectivityGroup')


class CreateConnectivityGroup(neutronv20.CreateCommand):
    """Create an connectivity group."""

    resource = 'connectivity_group'
    log = logging.getLogger(__name__ + '.CreateConnectivityGroup')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help=_('Name for the connectivity group'))
        parser.add_argument(
            'endpoints', type=string.split, metavar='ENDPOINTS',
            help=_('Ordered list of whitespace-delimited endpoint '
                   'names or IDs; e.g., --endpoints \"endpoint1 endpoint2\"'))

    def args2body(self, parsed_args):
        body = {'connectivitygroup': {}}
        if parsed_args.endpoints:
            _endpoints = []
            for e in parsed_args.endpoints:
                _endpoints.append(
                    neutronv20.find_resourceid_by_name_or_id(
                        self.get_client(), 'endpoint', e))
                body[self.resource].update({'members': _endpoints})
        if parsed_args.name:
            body[self.resource].update({'name': parsed_args.name})

        return body


class DeleteConnectivityGroup(neutronv20.DeleteCommand):
    """Delete a given connectivity group."""

    resource = 'connectivity_group'
    log = logging.getLogger(__name__ + '.DeleteConnectivityGroup')


class UpdateConnectivityGroup(neutronv20.UpdateCommand):
    """Update an connectivity group."""

    resource = 'connectivity_group'
    log = logging.getLogger(__name__ + '.UpdateConnectivityGroup')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help=_('Name for the connectivity group'))
        parser.add_argument(
            '--endpoints', type=string.split, metavar='ENDPOINTS',
            help=_('Ordered list of whitespace-delimited endpoint '
                   'names or IDs; e.g., --endpoints \"endpoint1 endpoint2\"'))

    def args2body(self, parsed_args):
        body = {self.resource: {}}
        if parsed_args.endpoints:
            _endpoints = []
            for e in parsed_args.endpoints:
                _endpoints.append(
                    neutronv20.find_resourceid_by_name_or_id(
                        self.get_client(), 'endpoint', e))
                body[self.resource].update({'members': _endpoints})
        if parsed_args.name:
            body[self.resource].update({'name': parsed_args.name})

        return body
