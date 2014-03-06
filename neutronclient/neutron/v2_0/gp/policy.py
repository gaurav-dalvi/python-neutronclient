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


class ListPolicy(neutronv20.ListCommand):
    """List policies."""

    resource = 'policy'
    log = logging.getLogger(__name__ + '.ListPolicy')
    list_columns = ['id', 'name', 'classifier', 'action_list']
    pagination_support = True
    sorting_support = True


class ShowPolicy(neutronv20.ShowCommand):
    """Show information of a given policy."""

    resource = 'policy'
    log = logging.getLogger(__name__ + '.ShowPolicy')


class CreatePolicy(neutronv20.CreateCommand):
    """Create a policy."""

    resource = 'policy'
    log = logging.getLogger(__name__ + '.CreatePolicy')

    #TODO(cgoncalves): add remaining arguments (srcs, dsts, rules)
    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help=_('Name for the policy'))
        parser.add_argument(
            '--bidirectional',
            action='store_true',
            help=_('Enable policy as bidirectional'))

    #TODO(cgoncalves): parse remaining arguments (srcs, dsts, rules)
    def args2body(self, parsed_args):
        body = {'policy': {}}
        if parsed_args.name:
            body['policy'].update({'name': parsed_args.name})
        if parsed_args.bidirectional:
            body['policy'].update({'bidirectional': True})

        return body


class DeletePolicy(neutronv20.DeleteCommand):
    """Delete a given policy."""

    resource = 'policy'
    log = logging.getLogger(__name__ + '.DeletePolicy')


class UpdatePolicy(neutronv20.UpdateCommand):
    """Update a policy."""

    resource = 'policy'
    log = logging.getLogger(__name__ + '.UpdatePolicy')

    #TODO(cgoncalves): add remaining arguments (rules)
    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help=_('Name for the policy'))

    #TODO(cgoncalves): parse remaining arguments (rules)
    def args2body(self, parsed_args):
        body = {'policy': {}}
        if parsed_args.name:
            body['policy'].update({'name': parsed_args.name})

        return body
