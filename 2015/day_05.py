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
for l in lines:
    if sum(1 if c in 'aeiou' else 0 for c in l) < 3:
        continue

    if all(a != b for a, b in u.pairwise(l)):
        continue

    if any(sub in l for sub in ['ab', 'cd', 'pq', 'xy']):
        continue

    res += 1

print(res)


# PART 2
res = 0
for l in lines:
    if all(l[i] != l[i+2] for i in range(len(l)-2)):
        continue

    for i in range(len(l)-1):
        pat = l[i:i+2]

        if pat in l[i+2:]:
            res += 1
            break

print(res)

