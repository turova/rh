import time
from datetime import datetime


proc_meminfo = None
proc_zoneinfo = None

mem = 0
last_measurement = None
proc_stat = None

meminfo_required_fields = [
    'MemFree',
    'Active(file)',
    'Inactive(file)',
    'SReclaimable'
]

def time_now():
    # from https://stackoverflow.com/questions/11743019/convert-python-datetime-to-epoch-with-strftime
    now = datetime.now()
    new_time = time.mktime(now.timetuple()) + now.microsecond * 1e-6
    return new_time

#https://unix.stackexchange.com/questions/261247/how-can-i-get-the-amount-of-available-memory-portably-across-distributions/261252
#https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=34e431b0a
def mem_now():
    global proc_meminfo
    if proc_meminfo is None:
        proc_meminfo = open('/proc/meminfo', 'r')
    proc_meminfo.seek(0)
    
    mem_lines = {}
    for i in range(0,3):
        line = proc_meminfo.readline()
        if (i == 2):
            line = line.strip().split()
            return line[1]

def init():
    global mem
    global last_measurement

def run():
    return mem_now()

def info():
        return "Returns the available memory (in kB), as defined in the MemAvailable field in /proc/meminfo"

def test():
    init()
    print(run())
