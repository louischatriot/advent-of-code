import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import collections
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
import functools

patterns = set(lines[0].split(', '))
to_build = lines[2:]

@functools.cache
def buildable(target):
    if target in patterns:
        return True

    if len(target) == 1:
        return False

    return any(buildable(target[0:i]) and buildable(target[i:]) for i in range(1, len(target)))


res = sum(1 if buildable(t) else 0 for t in to_build)
print(res)


# PART 2
@functools.cache
def arrs(target):
    if target == '':
        return 1
    else:
        return sum(arrs(target[len(p):]) if target.startswith(p) else 0 for p in patterns)



res = sum(arrs(t) for t in to_build)
print(res)




