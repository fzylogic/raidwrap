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

    def _find_disks(self, wanted_statuses, except_statuses):
        output = subprocess.check_output(["megacli", "-pdlist", "-aall"])
        disks = []
        status = "ok"
        for line in output.splitlines():
            (key, val) = re.split(":", line)
            if (key == "Enclosure Device ID"):
                enc = val
            elif (key == "Slot Number"):
                slot = val
            if (enc and slot):
                disk = enc + ':' + slot
            if (key == "Drive has flagged a S.M.A.R.T alert"):
                failed = val
                if (failed == 1):
                    status = "failed"
                if (status not in except_statuses and
                       (status in wanted_statuses or not wanted_statuses)):
                    disks.append(disk)
        return disks

    def identify_failed_disks(self):
        #pdlocate
        failed_disks = self._find_disks('failed')
        if not failed_disks:
            print "No failed disks found to identify"
        else:
            for d in failed_disks:
                subprocess.call(["megacli", "-pdlocate", "-start",
                    "-physdrv[" + d + "]", "-aall"])

    def identify_cleared(self):
        disks = self._find_disks()
        for d in disks:
            subprocess.call(["megacli", "-pdlocate", "-stop",
                "-physdrv[" + d + "]", "-aall"])
