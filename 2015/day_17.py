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
total = 25 if is_example else 150
containers = sorted([int(l) for l in lines], key= lambda n: -n)

def how_many(containers, total):
    if total == 0:
        return 1

    res = 0

    for i in range(len(containers)):
        container = containers[i]

        if total >= container:
            __containers = [c for c in containers[i+1:]]
            res += how_many(__containers, total - container)

    return res

res = how_many(containers, total)
print(res)


# PART 2
# Well not so many possibilities so let's list them
def pos(containers, total, used):
    if total == 0:
        return [used]

    res = []

    for i in range(len(containers)):
        container = containers[i]

        if total >= container:
            __containers = [c for c in containers[i+1:]]
            __used = [c for c in used] + [container]
            res += pos(__containers, total - container, __used)

    return res

possibilities = pos(containers, total, [])
the_min = min(map(len, possibilities))
res = sum(1 if len(p) == the_min else 0 for p in possibilities)
print(res)

