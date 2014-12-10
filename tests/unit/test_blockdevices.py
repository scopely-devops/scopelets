# Copyright (c) 2014 Scopely, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from scopelets.blockdevices import (
    block_device_to_boto,
    block_device_to_cf
)


def mapping_fixture():
    return [{
        "device_name": "/dev/sda1",
        "no_device": False,
        "ebs": {
            "delete_on_termination": True,
            "volume_size": 60,
            "volume_type": "gp2"
        }
    }]


def test_block_device_boto():
    device = block_device_to_boto(mapping_fixture())
    assert device['/dev/sda1'].size == 60
    assert device['/dev/sda1'].delete_on_termination
    assert not device['/dev/sda1'].no_device
    assert device['/dev/sda1'].volume_type == 'gp2'
    params = {}
    device.ec2_build_list_params(params)
    assert params == {
        'BlockDeviceMapping.1.DeviceName': '/dev/sda1',
        'BlockDeviceMapping.1.Ebs.DeleteOnTermination': 'true',
        'BlockDeviceMapping.1.Ebs.VolumeSize': 60,
        'BlockDeviceMapping.1.Ebs.VolumeType': 'gp2',
    }


def test_block_device_cf():
    result = block_device_to_cf(mapping_fixture())
    assert result == [{
        "DeviceName": "/dev/sda1",
        "NoDevice": False,
        "Ebs": {
            "DeleteOnTermination": True,
            "VolumeSize": 60,
            "VolumeType": "standard"
        }
    }]
