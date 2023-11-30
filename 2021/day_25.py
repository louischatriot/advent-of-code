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
N = len(lines)
M = len(lines[0])

east = set()
south = set()

for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == 'v':
            south.add((i, j))
        elif c == '>':
            east.add((i, j))


R = 6000
for r in range(0, R):
    east_changes = set()

    for i, j in east:
        next_pos = (i, (j+1) % M)
        if next_pos not in east and next_pos not in south:
            east_changes.add((i, j))

    for i, j in east_changes:
        east.remove((i, j))
        next_pos = (i, (j+1) % M)
        east.add(next_pos)


    south_changes = set()

    for i, j in south:
        next_pos = ((i+1) % N, j)
        if next_pos not in east and next_pos not in south:
            south_changes.add((i, j))

    for i, j in south_changes:
        south.remove((i, j))
        next_pos = ((i+1) % N, j)
        south.add(next_pos)


    if len(east_changes) + len(south_changes) == 0:
        print(r+1)
        break



