import base
import re
import subprocess


class Driver(base.Driver):
    def __init__(self):
        return

    def disk_list(self):
        subprocess.call(["tw_cli", "/c0", "show"])

    def disk_info(self, disk):
        if (re.match("^\d+$", disk)):
            subprocess.call(["tw_cli", "/c0/p" + disk, "show"])
        else:
            print "for 3ware cards, simply pass the disk ID as a number"
            return

    def ctl_info(self):
        subprocess.call(["tw_cli", "/c0", "show", "all"])

    def get_log(self):
        subprocess.call(["tw_cli", "/c0", "show", "alarms"])
