#!/usr/bin/env python3

import unittest

from .unitdata import (
    sas2ircu_sections,
    sas2ircu_kv,
    sas2ircu_section_controller_information,
    sas2ircu_section_physical_device_information,
    camcontrol_devlist_full,
    camcontrol_inquiry_whitespace,
)

from burnin.sas2ircu import (
    _sas2ircu_key_values,
    _sas2ircu_sections,
    _sas2ircu_physical_device_information,
)

from burnin.camcontrol import (
    _camcontrol_devlist,
    _camcontrol_inquiry,
)


class Camcontrol(unittest.TestCase):

    def test_devlist(self):
        devlist_partial = '\n'.join(camcontrol_devlist_full.split('\n')[:3])
        disk_ids = _camcontrol_devlist(devlist_partial)
        self.assertEqual(
            disk_ids,
            [['pass0', 'ses0'], ['pass1', 'da0'], ['pass2', 'da1']]
        )
        _camcontrol_devlist(camcontrol_devlist_full)

    def test_inquiry(self):
        serial = _camcontrol_inquiry(camcontrol_inquiry_whitespace)
        self.assertEqual(serial, '17RTK1MOF57D')


class Lsi2sas(unittest.TestCase):

    def test_section_parsing(self):
        sections = _sas2ircu_sections(sas2ircu_sections)
        self.assertEqual(sections, {
                'Section One': '  blabla\r\n',
                'Section Two': 'meh\r\n',
                'Sec3': 'blub\r\n  bla\r\n',
            }
        )

    def test_kv_parsing(self):
        kv_parsed = _sas2ircu_key_values(sas2ircu_kv)
        self.assertEqual(kv_parsed, {
                'Enclosure #': '2',
                'Slot #': '8'
            }
        )

    def test_controller_information(self):
        section = sas2ircu_section_controller_information
        controller = _sas2ircu_key_values(section)
        self.assertTrue(controller['RAID Support'] == 'No')
        self.assertTrue(controller['Controller type'] == 'SAS2008')

    def test_physical_device_information(self):
        section = sas2ircu_section_physical_device_information
        devices = _sas2ircu_physical_device_information(section)
        # TODO Test some more stuff

if __name__ == '__main__':
    unittest.main()
