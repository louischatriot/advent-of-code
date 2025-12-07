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
pos = defaultdict(lambda: 0)

for i, c in enumerate(lines[0]):
    if c == 'S':
        pos[i] += 1

splitters = dict()
N = 0
for i, line in enumerate(lines):
    N = i+1
    s = set()
    for j, c in enumerate(line):
        if c == '^':
            s.add(j)

    splitters[i] = s


splits = 0
for i in range(N):
    new_pos = defaultdict(lambda: 0)
    for p in pos:
        if p in splitters[i]:
            new_pos[p-1] += pos[p]
            new_pos[p+1] += pos[p]
            splits += 1
        else:
            new_pos[p] += pos[p]

    pos = new_pos

print(splits)


# PART 2
res = sum(v for p, v in pos.items())
print(res)




