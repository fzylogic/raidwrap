import base
import re
import subprocess


class Driver(base.Driver):
    def __init__(self):
        self.name = "megacli"
        return

    def disk_list(self):
        subprocess.call(["megacli", "-pdlist", "-aall"])

    def disk_info(self, disk):
        if (re.match("\d+:\d+", disk)):
            subprocess.call(["megacli", "-physdrv", disk, "-aall"])
        else:
            return "megacli wants disk definitions in the form of\
                    enclosure:device"

    def ctl_info(self):
        subprocess.call(["megacli", "-adpallinfo", "-aall"])

    def get_log(self):
        subprocess.call(["megacli", "-adpalilog", "-aall"])
