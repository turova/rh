import time
from datetime import datetime

proc_stat = None

cpu = 0
last_measurement = None
proc_stat = None

def time_now():
    # from https://stackoverflow.com/questions/11743019/convert-python-datetime-to-epoch-with-strftime
    now = datetime.now()
    new_time = time.mktime(now.timetuple()) + now.microsecond * 1e-6
    return new_time

def cpu_now():
    global proc_stat
    if proc_stat is None:
        proc_stat = open('/proc/stat', 'r')
    proc_stat.seek(0)
    cpu_line = proc_stat.readline().strip()
    cpu_array = cpu_line.split(' ')
    cpu_sum = sum(#Get sum of cpu array ints 2:9
        list(#Get list of cpu array ints 2:9
            map(int,cpu_array[2:5] + cpu_array[6:9])#Convert all non-steal/non-guest CPU values to ints
            )
        )
    return cpu_sum

def init():
    global cpu
    global last_measurement
    cpu = cpu_now()
    last_measurement = time_now()

def read_cpu():
    global cpu
    global last_measurement
    new_cpu = cpu_now()
    new_measurement = time_now()

    time_difference = new_measurement - last_measurement
    cpu_difference = new_cpu - cpu

    cpu_utilization = cpu_difference / time_difference

    cpu = new_cpu
    last_measurement = new_measurement

    return int(cpu_utilization)

def run():
    return read_cpu()

def info():
    return "Returns the percentage of all non-steal, non-guest, non-idle CPU cycles"
