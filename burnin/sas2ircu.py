
import re
from burnin.utils import run


def sas2ircu(controller_id):
    sas2ircu_stdout = run('sas2ircu {} DISPLAY'.format(controller_id))

    # Get the global config sections to make it more parsable.
    sections = _sas2ircu_sections(sas2ircu_stdout)
    # The controller info section is only KVs, so we can use it directly.
    controller = _sas2ircu_key_values(
        sections['Controller information']
    )

    # Attach devices to the controller information.
    controller['Physical Device'] = _sas2ircu_physical_device_information(
        sections['Physical device information']
    )

    return controller


def _sas2ircu_sections(sas2ircu_stdout):
    sas2ircu_section_re = r'-+\r\n(?P<title>.+?)\r\n-+\r\n(?P<content>[\s\S]*?)(?=-{3,})'
    return {
        match.group('title'): match.group('content')
        for match in re.finditer(sas2ircu_section_re, sas2ircu_stdout)
    }


def _sas2ircu_key_values(kv_block):
    sas2ircu_key_value_re = r'\s+(?P<key>.+?)\s+: (?P<value>.+?)\s*\r\n'
    return {
        kv_match.group('key'): kv_match.group('value')
        for kv_match in re.finditer(sas2ircu_key_value_re, kv_block)
    }


def _sas2ircu_physical_device_information(devices_section):
    sas2ircu_device_block_re = r'Device is a (?P<type>.+)\r\n(?P<kvs>[\s\S]+?)(?=[\r\n]{4,}|\Z)'

    # Iterate over all devices
    devices = []
    for device_match in re.finditer(sas2ircu_device_block_re, devices_section):
        # Get all device kv attributes
        device_block = device_match.group('kvs')
        device = _sas2ircu_key_values(device_block)
        device['Type'] = device_match.group('type')
        devices.append(device)

    return devices
