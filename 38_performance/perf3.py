"""
    Use line profile.

    Dependencies:
        $ pip3 install -U line_profiler

    References:
        - https://github.com/rkern/line_profiler
        - https://yakst.com/ja/posts/42

    Usage:
        $ kernprof -l -v perf3.py
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
$ kernprof -l -v perf3.py 
Wrote profile results to perf3.py.lprof
Timer unit: 1e-06 s

Total time: 0.874731 s
File: perf3.py
Function: get_images at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    12                                           @profile
    13                                           def get_images():
    14         1            4      4.0      0.0      images = []
    15        11           35      3.2      0.0      for index in range(500, 510):
    16        10       282544  28254.4     32.3          with urlopen("http://www.yoheim.net/image/{}.jpg".format(index)) as res:
    17        10       592147  59214.7     67.7              images.append(res.read())
    18         1            1      1.0      0.0      return images

Line #:
    The line number in the file.
Hits:
    The number of times that line was executed.
Time:
    The total amount of time spent executing the line in the timer's units. In the header information before the tables, you will see a line "Timer unit:" giving the conversion factor to seconds. It may be different on different systems.
Per Hit:
    The average amount of time spent executing the line once in the timer's units.
% Time:
    The percentage of time spent on that line relative to the total amount of recorded time spent in the function.
Line Contents:
    The actual source code. Note that this is always read from disk when the formatted results are viewed, not when the code was executed. If you have edited the file in the meantime, the lines will not match up, and the formatter may not even be able to locate the function for display.
"""