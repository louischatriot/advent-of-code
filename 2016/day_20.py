import sys
import re
import u as u
from collections import defaultdict, deque
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
allowed = [(0, 4294967295)]
if is_example:
    allowed = [(0, 9)]

for line in lines:
    lm, lM = line.split('-')
    lm, lM = int(lm), int(lM)

    new_allowed = []
    for am, aM in allowed:
        if lm <= am <= aM <= lM:
            continue

        if lm <= am <= lM < aM:
            new_allowed.append((lM+1, aM))

        elif am < lm <= aM <= lM:
            new_allowed.append((am, lm-1))

        elif am < lm <= lM < aM:
            new_allowed.append((am, lm-1))
            new_allowed.append((lM+1, aM))

        elif lM < am or aM < lM:
            new_allowed.append((am, aM))

    allowed = new_allowed

print(allowed[0][0])


# PART 2
res = 0
for am, aM in allowed:
    res += 1 + aM - am

print(res)




