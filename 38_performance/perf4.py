"""
    Use memory profiler

    Dependencies:
        $ pip3 install -U memory_profiler
        $ pip3 install -U psutil

    References:
        - https://github.com/fabianp/memory_profiler

    Usage:
        $ python3 -m memory_profiler perf4.py
"""
from urllib.request import urlopen

@profile
def get_images():
    images = []
    for index in range(500, 510):
        with urlopen("http://www.yoheim.net/image/{}.jpg".format(index)) as res:
            images.append(res.read())
    return images

images = get_images()

"""
$ python3 -m memory_profiler perf4.py 
Filename: perf4.py

Line #    Mem usage    Increment   Line Contents
================================================
    12   38.965 MiB    0.000 MiB   @profile
    13                             def get_images():
    14   38.965 MiB    0.000 MiB       images = []
    15   44.242 MiB    5.277 MiB       for index in range(500, 510):
    16   43.980 MiB   -0.262 MiB           with urlopen("http://www.yoheim.net/image/{}.jpg".format(index)) as res:
    17   44.242 MiB    0.262 MiB               images.append(res.read())
    18   44.242 MiB    0.000 MiB       return images

Line #:
    the line number of the code that has been profiled.

Mem usage:
    the memory usage of the Python interpreter after that line has been executed.

Increment:
    the difference in memory of the current line with respect to the last one.

Line Contents:
    the code that has been profiled.
"""