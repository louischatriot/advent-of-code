import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
res = 0

for line in lines:
    jolts = [int(c) for c in line]
    joltage = max(jolts[0:-1])
    joltage = 10 * joltage + max(jolts[jolts.index(joltage)+1:])
    res += joltage

print(res)


# PART 2



