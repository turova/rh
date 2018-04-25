# rh
Resource Harvester - a tool to gather low-level system data and make it easy to use programmatically

## OVERVIEW

This tool allows a user to gather system data and output it in a way that's easy to process programmatically. It is extensible for both input modules and output modules, allowing a user to add new input data and to add new output formats. The motivation for this tool was the lack of consistent output in tools such as top and dstat. Some example use cases include saving a TSV log and plotting the time-series data or piping data into Fluentd.

## USAGE

```
$ git clone git@github.com:turova/rh.git
# ...
$ cd rh
$ ./rh -h
usage: rh [-h] [-l] [-i INPUTS [INPUTS ...]] [-o OUTPUTS] [-t INTERVAL]

Resource Harvester

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            List all available modules and their descriptions
  -i INPUTS [INPUTS ...], --inputs INPUTS [INPUTS ...]
                        Space-separated list of input modules to use
  -o OUTPUTS, --outputs OUTPUTS
                        Output module to use (default is JSON). Currently,
                        only 1 output is supported
  -t INTERVAL, --interval INTERVAL
                        Number of seconds between harvest/print cycles
```

## USAGE EXAMPLES
```bash
$ ./rh # Default output is timestamp, cpu, and mem in JSON output format
{ "timestamp": "1524689668260", "cpu": "10", "mem": "10997148"}
{ "timestamp": "1524689669262", "cpu": "18", "mem": "10998020"}
```

```bash
# Print tab-separated list of timestamp and cpu values every half a second
$ ./rh -t .5 -i timestamp cpu -o tsv
1524689587554	0
1524689588055	11
1524689588557	5
1524689589058	21
```

## AVAILABLE MODULES

* Input modules:
  * ```mem``` - Returns the available memory (in kB), as defined in the MemAvailable field in /proc/meminfo
  * ```cpu``` - Returns the percentage of all non-steal, non-guest, non-idle CPU cycles
  * ```timestamp``` - Timestamp in milliseconds since epoch


* Output modules:
  * ```tsv``` - Tab-separated output
  * ```json``` - JSON output

## WRITING NEW MODULES
Writing a new modules is as simple as creating three functions and placing them in the appropriate folder (```inputs/``` or ```outputs/```:
- ```init()``` - Called when module is initially imported. This can be used for initializing values, marking a start timestamp, etc.
- ```run()``` - Called every interval to gather resources and return a value that can be printed. Can be string or number (ends up going through a str() conversion), but should not include endlines or other whitespace characters for positioning
- ```info()``` - Called when ```rh --info``` is called. Should return a string with a summary of the data the module gathers
