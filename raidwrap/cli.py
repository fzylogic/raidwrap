import argparse
from raidwrap import detect


def main():
    parser = argparse.ArgumentParser('RAIDwrap')
    parser.add_argument('--controllerlist',
                        '--ctllist',
                        action='store_true',
                        dest='ctllist'
                        )
    parser.add_argument('--controllerinfo',
                        '--ctlinfo',
                        action='append',
                        dest='ctlinfo'
                        )
    parser.add_argument('--disklist',
                        '--dlist',
                        action='store_true',
                        dest='disklist'
                        )
    parser.add_argument('--diskinfo',
                        '--dinfo',
                        action='append',
                        dest='diskinfo'
                        )
    parser.add_argument('--log',
                        action='store_true',
                        dest='log'
                        )
    parser.add_argument('--controller',
                        action='append',
                        dest='controllers'
                        )
    parser.add_argument('--prereq',
                        action='store_true',
                        dest='prereq',
                        help='show which backend plugins have their necessary\
                        prerequisites installed'
                        )
    args = parser.parse_args()
    controllers = args.controllers
    if (args.prereq):
        for Driver in detect.AllDrivers():
            if Driver.have_prereq():
                print Driver.name + " READY"
            else:
                print Driver.name + " MISSING DEPENDENCY"
        return

    if (controllers):
        print controllers
    Driver = detect.Driver()
    if (Driver):
        print Driver.name
    else:
        print "no supported devices found"

    if (args.diskinfo):
        result = Driver.disk_info()
        print result
    if (args.disklist):
        result = Driver.disk_list()
        print result


if __name__ == '__main__':
    main()
