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
pos = (0, 0)
visited = set()
visited.add(pos)
for c in lines[0]:
    if c == '^':
        pos = (pos[0], pos[1] + 1)
    elif c == 'v':
        pos = (pos[0], pos[1] - 1)
    elif c == '<':
        pos = (pos[0] - 1, pos[1])
    elif c == '>':
        pos = (pos[0] + 1, pos[1])
    else:
        raise ValueError()

    visited.add(pos)

print(len(visited))


# PART 2
N = len(lines[0])
pos = (0, 0)
visited = set()
visited.add(pos)
for i in range(0, N, 2):
    c = lines[0][i]

    if c == '^':
        pos = (pos[0], pos[1] + 1)
    elif c == 'v':
        pos = (pos[0], pos[1] - 1)
    elif c == '<':
        pos = (pos[0] - 1, pos[1])
    elif c == '>':
        pos = (pos[0] + 1, pos[1])
    else:
        raise ValueError()

    visited.add(pos)

pos = (0, 0)
for i in range(1, N, 2):
    c = lines[0][i]

    if c == '^':
        pos = (pos[0], pos[1] + 1)
    elif c == 'v':
        pos = (pos[0], pos[1] - 1)
    elif c == '<':
        pos = (pos[0] - 1, pos[1])
    elif c == '>':
        pos = (pos[0] + 1, pos[1])
    else:
        raise ValueError()

    visited.add(pos)

print(len(visited))



