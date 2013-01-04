~~~~~~~~
RAIDwrap
~~~~~~~~
A user-friendly wrapper for the most commonly-used functions of various vendor
RAID controller configurators (cli64, megacli, tw_cli, etc)


~~~~~~~~
Features
~~~~~~~~
* List attached disks
* Get detailed information about a specific disk
* Get general RAID controller status information
* Dump the controller event log


~~~~
TODO
~~~~
* Support multiple controllers in the same box
* Add parsers for the output so we can provide a unified view (will be toggleable)
* Add basic diagnostic features (find and optionally flag any bad disks, get general RAID health, etc)
* MAYBE add support for some limited write options (enable/disable caching, etc)
