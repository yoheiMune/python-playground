"""
    Use `time` command.

    Usage:
        $ time python3 perf1.py
"""

arr = []
for i in range(1000000):
    arr.append(i)

# real    0m0.240s
# user    0m0.198s
# sys 0m0.032s