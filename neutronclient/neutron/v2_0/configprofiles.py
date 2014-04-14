# vim: tabstop=4 shiftwidth=4 softtabstop=4
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
#
#@author Nader Lahouti, Cisco Systems Inc. March 2014

import logging
from neutronclient.neutron import v2_0 as neutronV20

RESOURCE = 'config_profile'

class ListConfigProfiles(neutronV20.ListCommand):
    """List configuration profiles that a network can use."""

    resource = RESOURCE
    log = logging.getLogger(__name__ + '.ListConfigProfiles')
    _formatters = {}
    list_columns = ['id', 'name']
