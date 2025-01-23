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
parts = [line.split('/') for line in lines]
parts = [(int(a[0]), int(a[1])) for a in parts]

import functools

# @functools.cache
def strongest_from(end, parts):
    if len(parts) == 0:
        return 0

    res = 0
    for a, b in parts:
        if end == a:
            __parts = [(aa, bb) for aa, bb in parts if a != aa or b != bb]
            res = max(res, a + b + strongest_from(b, __parts))
            continue

        if end == b:
            __parts = [(aa, bb) for aa, bb in parts if a != aa or b != bb]
            res = max(res, a + b + strongest_from(a, __parts))
            continue

    return res


res = strongest_from(0, parts)
print(res)


# PART 2
def strongest_from(end, parts):
    if len(parts) == 0:
        return (0, 0)

    res = (0, 0)
    for a, b in parts:
        if end == a:
            __parts = [(aa, bb) for aa, bb in parts if a != aa or b != bb]
            l, s = strongest_from(b, __parts)
            res = max(res, (l + 1, a + b + s))
            continue

        if end == b:
            __parts = [(aa, bb) for aa, bb in parts if a != aa or b != bb]
            l, s = strongest_from(a, __parts)
            res = max(res, (l + 1, a + b + s))
            continue

    return res

res = strongest_from(0, parts)[1]
print(res)




