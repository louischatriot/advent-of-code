import sys
import re
import u as u
from collections import defaultdict
import math

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
crabs = list(map(int, lines[0].split(',')))
targets = dict()

# Always align on a crab to reduce search space (never optimal to align between crabs)
res = 9999999999999  # Hu hu hu
for c in crabs:
    res = min(res, sum([abs(cc - c) for cc in crabs]))

print(res)


# PART 2 - positions between crabs not necessarily suboptimal anymore
m = min(crabs)
M = max(crabs)
res = 9999999999999

for p in range(m, M+1):
    res = min(res, sum([abs(cc - p) * (abs(cc - p) + 1) // 2 for cc in crabs]))

print(res)


