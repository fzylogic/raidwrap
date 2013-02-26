import os
from raidwrap.drivers import tw_cli
from raidwrap.drivers import megacli
from raidwrap.drivers import cli64
from raidwrap.drivers import fallback

basedir = "/sys/bus/pci/devices"

#disabled the fallback driver for now
backend_drivers = {'pci:megaraid_sas': megacli.Driver(),
                   'pci:3w-9xxx': tw_cli.Driver(),
                   'pci:arcmsr': cli64.Driver(),
                   'xxxpci:ahci': fallback.Driver()
                   }


class Device:
    def __init__(self, path):
        self.path = path


def Driver():
    devices = find_supported_devices()
    for device in devices:
        # just supporting one device for now
        return backend_drivers[device.driver]


def AllDrivers():
    drivers = []
    for driver in backend_drivers.values():
        drivers.append(driver)
    return drivers


def find_supported_devices():
    devs = os.listdir(basedir)
    supported_devices = []
    for dev in devs:
        device = Device(dev)
        device.driver = get_kernel_driver(dev)
        if device.driver in backend_drivers:
            supported_devices.append(device)
    return supported_devices


def get_kernel_driver(device):
    driverfile = basedir + "/" + device + "/driver/module/drivers"
    driver = False
    if os.access(driverfile, os.R_OK):
        driver = os.listdir(driverfile)[0]
    return driver
