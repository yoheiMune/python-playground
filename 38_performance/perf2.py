"""
    Use Context Manager Timer.

    Usage:
        $ python3 perf2.py
"""
from datetime import datetime
class Timer(object):
    def __enter__(self):
        self.start = datetime.now()
    def __exit__(self, *exc):
        diff = (datetime.now() - self.start).microseconds / 1000
        print("time: {}ms".format(diff))

with Timer():
    arr = []
    for i in range(10000000):
        arr.append(i)

# time: 637.091ms