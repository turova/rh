import time
from datetime import datetime

def init():
    pass

def run():
    now = datetime.now()
    msec_since_epoch = int( datetime.timestamp( now ) * 1000 )
    return msec_since_epoch

def info():
    return "Timestamp in milliseconds since epoch"
