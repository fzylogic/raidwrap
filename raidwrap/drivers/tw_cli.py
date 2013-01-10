import base
import re
import subprocess


class Driver(base.Driver):
    def __init__(self):
        self.name = "tw_cli"
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

    def find_disks(self, wanted_statuses, except_statuses):
        output = subprocess.check_output(["tw_cli", "/c0", "show"])
        disks = []
        for line in output.splitlines:
            for line in output.splitlines():
                m = re.match("p(\d+)\s+(\S+)", line)
                if m:
                    device = m.group(1)
                    status = m.group(2)
                    print device + ' is ' + status
                    if (status not in except_statuses and
                        (status in wanted_statuses or not wanted_statuses)):
                        disks.append(device)
        return disks

    def identify_failed_disks(self):
        failed_disks = self.find_disks("", ["OK", "NOT-PRESENT"])
        if not failed_disks:
            print "No failed disks found to identify"
        else:
            for d in failed_disks:
                subprocess.call(["tw_cli", "/c0/p" + d, "set identify=on"])

    def identify_clear(self):
        disks = self.find_disks()
        for d in disks:
            subprocess.call(["tw_cli", "/c0/p" + d, "set identify=off"])

    def have_prereq(self):
        null = open("/dev/null", "w")
        print null
        try:
            ret = subprocess.call(["tw_cli", "help"],
                stdin=null,
                stdout=null)
        except:
            return False
        if ret == 0:
            return True
        else:
            return False
