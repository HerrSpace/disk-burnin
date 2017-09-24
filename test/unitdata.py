
camcontrol_inquiry_whitespace = """
      17RTK1MOF57D    
"""

camcontrol_devlist_full = """<SUN Storage J4400 3R53>           at scbus6 target 88 lun 0 (pass0,ses0)\r
<ATA TOSHIBA HDWE150 FP2A>         at scbus6 target 89 lun 0 (pass1,da0)\r
<ATA TOSHIBA HDWE150 FP2A>         at scbus6 target 90 lun 0 (pass2,da1)\r
<ATA HGST HDN726050AL W7JH>        at scbus6 target 91 lun 0 (pass3,da2)\r
<ATA HGST HDN726050AL W7JH>        at scbus6 target 92 lun 0 (pass4,da3)\r
<ATA TOSHIBA HDWE150 FP2A>         at scbus6 target 93 lun 0 (pass5,da4)\r
<ATA TOSHIBA MD04ACA5 FS2A>        at scbus6 target 94 lun 0 (pass6,da5)\r
<ATA TOSHIBA MD04ACA5 FS2A>        at scbus6 target 95 lun 0 (pass7,da6)\r
<ATA TOSHIBA MD04ACA5 FS2A>        at scbus6 target 96 lun 0 (pass8,da7)\r
<ATA TOSHIBA MD04ACA5 FS2A>        at scbus6 target 97 lun 0 (pass9,da8)\r
<ATA TOSHIBA MD04ACA5 FS2A>        at scbus6 target 98 lun 0 (pass10,da9)\r
<ATA TOSHIBA MD04ACA5 FS2A>        at scbus6 target 99 lun 0 (pass11,da10)\r
<ATA TOSHIBA MD04ACA5 FS2A>        at scbus6 target 100 lun 0 (pass12,da11)\r
<ATA TOSHIBA MD04ACA5 FS2A>        at scbus6 target 101 lun 0 (pass13,da12)\r
<SUN Storage J4400 3R53>           at scbus6 target 102 lun 0 (pass14,ses1)\r
<STEC MACH8 IOPS 2103>             at scbus9 target 0 lun 0 (pass15,ada0)\r
<STEC MACH8 IOPS 2103>             at scbus10 target 0 lun 0 (pass16,ada1)"""

sas2ircu_kv = """\r
  Enclosure #                         : 2         \r
  Slot #                            : 8\r
"""

sas2ircu_sections = """Foo\r
bar\r
------------------------------------------------------------------------\r
Section One\r
------------------------------------------------------------------------\r
  blabla\r
------------------------------------------------------------------------\r
Section Two\r
------------------------------------------------------------------------\r
meh\r
------------------------------------------------------------------------\r
Sec3\r
------------------------------------------------------------------------\r
blub\r
  bla\r
------------------------------------------------------------------------\r
Trailing foo.\r
Blub"""


sas2ircu_section_controller_information = """\r
  Controller type                         : SAS2008\r
  BIOS version                            : 7.39.02.00\r
  Firmware version                        : 20.00.06.00\r
  Channel description                     : 1 Serial Attached SCSI\r
  Initiator ID                            : 0\r
  Maximum physical devices                : 511\r
  Concurrent commands supported           : 2040\r
  Slot                                    : 1\r
  Segment                                 : 0\r
  Bus                                     : 3\r
  Device                                  : 0\r
  Function                                : 0\r
  RAID Support                            : No\r
"""

sas2ircu_section_physical_device_information = """\r
Initiator at ID #0\r
\r
Device is a Hard disk\r
  Enclosure #                             : 3\r
  Slot #                                  : 22\r
  SAS Address                             : 5001636-0-0014-d416\r
  State                                   : Ready (RDY)\r
  Size (in MB)/(in sectors)               : 4769307/9767541167\r
  Manufacturer                            : ATA     \r
  Model Number                            : HGST HDN726050AL\r
  Firmware Revision                       : W7JH\r
  Serial No                               : NAHX8LDX\r
  GUID                                    : N/A\r
  Protocol                                : SATA\r
  Drive Type                              : SATA_HDD\r
\r
Device is a Hard disk\r
  Enclosure #                             : 3\r
  Slot #                                  : 23\r
  SAS Address                             : 5001636-0-0014-d417\r
  State                                   : Ready (RDY)\r
  Size (in MB)/(in sectors)               : 4769307/9767541167\r
  Manufacturer                            : ATA     \r
  Model Number                            : HGST HDN726050AL\r
  Firmware Revision                       : W7JH\r
  Serial No                               : NAHX8MMX\r
  GUID                                    : N/A\r
  Protocol                                : SATA\r
  Drive Type                              : SATA_HDD\r
\r
Device is a Enclosure services device\r
  Enclosure #                             : 3\r
  Slot #                                  : 24\r
  SAS Address                             : 5001636-0-0014-d43d\r
  State                                   : Standby (SBY)\r
  Manufacturer                            : SUN     \r
  Model Number                            : Storage J4400   \r
  Firmware Revision                       : 3R53\r
  Serial No                               : x3651825351\r
  GUID                                    : N/A\r
  Protocol                                : SAS\r
  Device Type                             : Enclosure services device\r
"""
