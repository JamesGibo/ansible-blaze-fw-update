#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: blaze_firmware

short_description: Install firmware update to Basler Blaze.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: Install the specified firmware file to the Basler Blaze 3D camera.

options:
    fwfile:
        description: This is the firmware file to be loaded.
        required: true
        type: str
    ip:
        description: IP Address of the camera
        required: true
        type: str
    port:
        description: Port of the camera
        required: false
        type: int
        default: 8080
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - james.basler.blaze

author:
    - James (@jamesgibo)
'''

EXAMPLES = r'''
# Update Firmware
- name: Update Basler Blaze Firmware
  james.basler.blaze.blaze_firmware:
    fwfile: '/home/james/Downloads/blaze-firmware-4.6.2/blaze-image-fw-4.6.2-20221024150208.swu'
    ip: 10.30.0.177
    port: 8080
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
message:
    description: Reports if the update for successful.
    type: str
    returned: always
    sample: 'Update successful'
'''

from ansible.module_utils.basic import AnsibleModule
from swupdateclient import main as fwupdate



def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        fwfile=dict(type='str', required=True),
        ip=dict(type='str', required=True),
        port=dict(type='int', required=False, default=8080)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    updater = fwupdate.SWUpdater(module.params['fwfile'], module.params['ip'], port=module.params['port'])
    if updater.update():
        result['message'] = 'Update successful'
        # Set changed flag after update
        result['changed'] = True
    else:
        module.fail_json(msg='FW Update Failed!', **result)
        result['message'] = "Update failed!"

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
