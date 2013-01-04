import base
import subprocess


class Driver(base.Driver):
    def __init__(self):
        self.name = "fallback"

    def disk_list(self):
        subprocess.call(["lsblk"])
