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

from neutronclient.neutron import v2_0 as neutronv20
from neutronclient.openstack.common.gettextutils import _


class ListEndpoint(neutronv20.ListCommand):
    """List endpoints."""

    resource = 'endpoint'
    log = logging.getLogger(__name__ + '.ListEndpoint')
    list_columns = ['id', 'name', 'type', 'reference']
    pagination_support = True
    sorting_support = True


class ShowEndpoint(neutronv20.ShowCommand):
    """Show information of a given endpoint."""

    resource = 'endpoint'
    log = logging.getLogger(__name__ + '.ShowEndpoint')


class CreateEndpoint(neutronv20.CreateCommand):
    """Create an endpoint."""

    resource = 'endpoint'
    log = logging.getLogger(__name__ + '.CreateEndpoint')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help=_('Name for the endpoint'))
        parser.add_argument(
            '--type',
            default='network',
            choices=['network', 'port'],
            help=_('Type of this endpoint. Defaults to network'))
        parser.add_argument(
            'reference', metavar='REFERENCE',
            help=_('Network or port id'))

    def args2body(self, parsed_args):
        body = {'endpoints': {'reference': parsed_args.reference}}

        if parsed_args.name:
            body['endpoints'].update({'name': parsed_args.name})
        if parsed_args.type:
            body['endpoints'].update({'type': parsed_args.type})
        return body


class DeleteEndpoint(neutronv20.DeleteCommand):
    """Delete a given endpoint."""

    resource = 'endpoint'
    log = logging.getLogger(__name__ + '.DeleteEndpoint')


class UpdateEndpoint(neutronv20.UpdateCommand):
    """Update an endpoint."""

    resource = 'endpoint'
    log = logging.getLogger(__name__ + '.UpdateEndpoint')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help=_('Name for the endpoint'))
        parser.add_argument(
            '--reference', metavar='REFERENCE',
            help=_('Network or port id'))

    def args2body(self, parsed_args):
        body = {'endpoints': {}}

        if parsed_args.name:
            body['endpoints'].update({'name': parsed_args.name})
        if parsed_args.reference:
            body['endpoints'].update({'reference': parsed_args.reference})
        return body
