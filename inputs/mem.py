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
    # meminfo = get_meminfo()
    # zoneinfo = get_zoneinfo()

    global proc_meminfo
    if proc_meminfo is None:
        proc_meminfo = open('/proc/meminfo', 'r')
    proc_meminfo.seek(0)
    # mem_lines = {}
    # for line in proc_meminfo:
    #     split_line = line.strip().split()
    #     mem_lines[split_line[0].replace(':', '')] = split_line[1]
    
    mem_lines = {}
    for i in range(0,3):
        line = proc_meminfo.readline()
        if (i == 2):
            line = line.strip().split()
            return line[1]
        # mem_lines[line[0].replace(':', '')] = line[1]
    # # mem_lines = proc_meminfo.readlines()
    # print(mem_lines)
    # return mem_lines
    # # cpu_array = cpu_line.split(' ')
    # # cpu_sum = sum(#Get sum of cpu array ints 2:9
    # #     list(#Get list of cpu array ints 2:9
    # #         map(int,cpu_array[2:5] + cpu_array[6:9])#Convert all non-steal/non-guest CPU values to ints
    # #         )
    # #     )
    # # print(cpu_array)
    # # return cpu_sum

def get_zoneinfo():
    global proc_zoneinfo
    if proc_zoneinfo is None:
        proc_zoneinfo = open('/proc/zoneinfo', 'r')
    proc_zoneinfo.seek(0)

    zone_low_sum = 0
    for line in proc_zoneinfo:
        split_line = line.strip().split()
        if split_line[0] == 'low':
            # print(str(zone_low_sum) + '+=' + split_line[1])
            zone_low_sum += int(split_line[1])
        # print('=> ' + str(zone_low_sum))
    return zone_low_sum


def get_meminfo():
    global proc_meminfo
    if proc_meminfo is None:
        proc_meminfo = open('/proc/meminfo', 'r')
    proc_meminfo.seek(0)
    mem_lines = {}
    for line in proc_meminfo:
        split_line = line.strip().split()
        mem_lines[split_line[0].replace(':', '')] = split_line[1]

    # Keep only the fields used for available memory computation
    filtered_mem_lines = {n: int(mem_lines[n]) for n in mem_lines if n in meminfo_required_fields}

    print(filtered_mem_lines)

    return filtered_mem_lines

def init():
    global mem
    global last_measurement
    # print("Initializing mem")
    # mem = mem_now()
    # last_measurement = time_now()

def run():
    # return read_mem()
    return mem_now()
    # meminfo = get_meminfo()
    # zoneinfo = get_zoneinfo()

    # available_mem = sum(meminfo.values()) - zoneinfo*12

    # return available_mem

def info():
    return "Help for mem"

def test():
    init()
    print(run())
    # run()
    # get_meminfo()
    # get_zoneinfo()