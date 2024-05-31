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
nexts = dict()
nexts['L'] = {'n': 'w', 'w': 's', 's': 'e', 'e': 'n'}
nexts['R'] = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}

dir = 'n'
x, y = 0, 0

for inst in lines[0].split(', '):
    turn, steps = inst[0], int(inst[1:])
    dir = nexts[turn][dir]

    if dir == 'n':
        y += steps
    elif dir == 's':
        y -= steps
    elif dir == 'w':
        x -= steps
    elif dir == 'e':
        x += steps
    else:
        raise ValueError()

print(abs(x) + abs(y))


# PART 2
visited = set()

dir = 'n'
x, y = 0, 0
visited.add((x, y))

for inst in lines[0].split(', '):
    turn, steps = inst[0], int(inst[1:])
    dir = nexts[turn][dir]
    dx, dy = 0, 0

    if dir == 'n':
        dy = 1
    elif dir == 's':
        dy = -1
    elif dir == 'w':
        dx -= 1
    elif dir == 'e':
        dx = 1
    else:
        raise ValueError()

    for _ in range(steps):
        x, y = x+dx, y+dy

        if (x, y) in visited:
            print(abs(x) + abs(y))
            sys.exit(0)
        else:
            visited.add((x, y))



