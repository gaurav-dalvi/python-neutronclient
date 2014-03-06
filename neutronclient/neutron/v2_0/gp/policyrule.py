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


class ListPolicyRule(neutronv20.ListCommand):
    """List policy rules."""

    resource = 'policy_rules'
    log = logging.getLogger(__name__ + '.ListPolicyRule')
    list_columns = ['id', 'name', 'classifier', 'action_list']
    pagination_support = True
    sorting_support = True


class ShowPolicyRule(neutronv20.ShowCommand):
    """Show information of a given policy rule."""

    resource = 'policy_rule'
    log = logging.getLogger(__name__ + '.ShowPolicyRule')


class CreatePolicyRule(neutronv20.CreateCommand):
    """Create an policy rule."""

    resource = 'policy_rule'
    log = logging.getLogger(__name__ + '.CreatePolicyRule')

    #TODO(cgoncalves): add remaining arguments
    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help=_('Name for the policy rule'))

    #TODO(cgoncalves): parse remaining arguments
    def args2body(self, parsed_args):
        body = {self.resource: {}}
        if parsed_args.name:
            body[self.resource].update({'name': parsed_args.name})

        return body


class DeletePolicyRule(neutronv20.DeleteCommand):
    """Delete a given policy rule."""

    resource = 'policy_rule'
    log = logging.getLogger(__name__ + '.DeletePolicyRule')


class UpdatePolicyRule(neutronv20.UpdateCommand):
    """Update a policy rule."""

    resource = 'policy_rule'
    log = logging.getLogger(__name__ + '.UpdatePolicyRule')
