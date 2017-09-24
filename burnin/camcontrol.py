
import re
from burnin.utils import run


def camcontrol():
    return {
        _camcontrol_inquiry(device_id=device_ids[0]): device_ids
        for device_ids in _camcontrol_devlist()
    }


def _camcontrol_inquiry(inquiry_stdout=None, device_id=None):
    if not inquiry_stdout:
        inquiry_stdout = run('camcontrol inquiry {} -S'.format(device_id))

    camcontrol_inquiry_re = r'\s*(?P<serial>.*[^\s])\s*'
    for cam_match in re.finditer(camcontrol_inquiry_re, inquiry_stdout):
        return cam_match.group('serial')


def _camcontrol_devlist(devlist_stdout=None):
    if not devlist_stdout:
        devlist_stdout = run('camcontrol devlist')

    camcontrol_devlist_re = r'<.+>.*\((?P<device_ids>.*)\)'

    return [
        cam_match.group('device_ids').split(',')
        for cam_match in re.finditer(camcontrol_devlist_re, devlist_stdout)
    ]
