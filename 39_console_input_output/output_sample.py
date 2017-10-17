"""
    Samples for how to output to console.

    References:
        - https://qiita.com/airtoxin/items/bb445529c94d3cd871f3
"""

# Normal Usage.
print("Normal Usage.")
for i in range(3):
    print(i)

"""
0
1
2
"""


# Override the prev.
print("-------\nOverride the prev.")
import sys
import time
for i in range(10):
    sys.stdout.write("\r{}".format(i))
    sys.stdout.flush()
    time.sleep(0.1)
print()

"""
-------
Override the prev.
9
"""


# Append to the prev.
print("-------\nAppend to the prev.")
for i in range(10):
    sys.stdout.write("*")
    sys.stdout.flush()
    time.sleep(0.1)
print()

"""
Append to the prev.
**********
"""
