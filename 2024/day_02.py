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

def is_safe(l):
    return all(1 <= b - a <= 3 for a, b in u.pairwise(l)) or all(1 <= a - b <= 3 for a, b in u.pairwise(l))

reports = [list(map(int, line.split())) for line in lines]

for r in reports:
    if is_safe(r):
        res += 1

print(res)


# PART 2
res = 0

for r in reports:
    if any(is_safe(r[0:k] + r[k+1:]) for k in range(-1, len(r))):
        res += 1

print(res)




