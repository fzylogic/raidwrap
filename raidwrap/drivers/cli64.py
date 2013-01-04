import base
import re
import subprocess


class Driver(base.Driver):
    def __init__(self):
        self.name = 'base'
        return

    def disk_list(self):
        subprocess.call(["cli64", "disk", "info"])

    def disk_info(self, disk):
        if (re.match("^\d+$", disk)):
            subprocess.call(["cli64", "disk", "drv=" + disk])
        else:
            print "for 3ware cards, simply pass the disk ID as a number"
            return

    def ctl_info(self):
        subprocess.call(["cli64", "sys", "info"])

    def get_log(self):
        subprocess.call(["cli64", "event", "info"])
