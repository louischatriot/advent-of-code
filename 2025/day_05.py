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
ranges = list()
i = 0
for line in lines:
    i+= 1
    if line == '':
        break

    a, b = line.split('-')
    a, b = int(a), int(b)
    ranges.append((a, b))


ids = list()
for line in lines[i:]:
    ids.append(int(line))


res = 0
for id in ids:
    if any(a<= id <= b for a, b in ranges):
        res += 1

print(res)


# PART 2
def merge(range_list, range):
    a0, b0 = range
    new_range_list = list()
    for a, b in range_list:
        if a <= a0 <= b or a <= b0 <= b or a0 <= a <= b0 or a0 <= b <= b0:
            a0 = min(a, a0)
            b0 = max(b, b0)
        else:
            new_range_list.append((a, b))

    new_range_list.append((a0, b0))
    return new_range_list

rl = [ranges[0]]
for range in ranges[1:]:
    rl = merge(rl, range)

res = 0
for a, b in rl:
    res += b - a + 1

print(res)

