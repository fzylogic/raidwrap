import base
import re
import subprocess


class Driver(base.Driver):
    def __init__(self):
        self.name = 'base'
        return

    def disk_list(self):
        subprocess.call(["cli64", "disk", "info"])
        return

    def disk_info(self, disk):
        if (re.match("^\d+$", disk)):
            subprocess.call(["cli64", "disk", "drv=" + disk])
            return
        else:
            print "for Areca cards, simply pass the disk ID as a number"
            return

    def ctl_info(self):
        subprocess.call(["cli64", "sys", "info"])
        return

    def get_log(self):
        subprocess.call(["cli64", "event", "info"])
        return

    def _find_disks(self, wanted_statuses, except_statuses):
        output = subprocess.check_output(["cli64", "disk", "info"])
        disks = []
        for line in output.splitlines():
            m = re.match("\s+(\d+)\s+(\d+)\s+slot#(\d+)")
            if m:
                device = m.group(1)
                #enclosure = m.group(2)
                #slot = m.group(3)
                if device:
                    disk_status = "OK"
                    dstatus = subprocess.check_output(["cli64",
                                                       "disk",
                                                       "smart",
                                                       "drv=" + device])
                    for sline in dstatus.splitlines():
                        sm = re.match(
                            "\s?\d+\s+.*0x\w+\s+\d+\s+\d+\s+\d+\s+(.*)")
                        status = sm.group(1)
                        if status != "OK":
                            disk_status = status
                    if (disk_status not in except_statuses and
                            (disk_status in wanted_statuses
                                or not wanted_statuses)):
                        disks.append(device)
        return disks

    def identify_failed_disks(self):
        disks = self._find_disks('', ['OK'])
        for d in disks:
            subprocess.call(['cli64', 'identify', 'drv' + d])

    def identify_clear(self):
        subprocess.call(['cli64', 'identify', 'drv=0'])

    def have_prereq(self):
        null = open("/dev/null", "w")
        print null
        try:
            ret = subprocess.call(["cli64", "help"],
                                  stdin=null,
                                  stdout=null)
        except:
            return False
        if ret == 0:
            return True
        else:
            return False
