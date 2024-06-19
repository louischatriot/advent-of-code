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
number = int(lines[0])

target = (7, 4)
if not is_example:
    target = (31, 39)

start = (1, 1)
res = None
less_than_fifty = set()

done = False
to_explore = [(start, 0)]
explored = set()
while len(to_explore) > 0:
    node, length = to_explore.pop(0)
    if node in explored:
        continue
    else:
        explored.add(node)

    # Works because our target is farther than 50 steps
    if length <= 50:
        less_than_fifty.add(node)

    x, y = node
    for dx, dy in u.ortho_neighbours:
        nx, ny = x+dx, y+dy
        if (nx, ny) == target:
            res = length + 1
            done = True
            break

        if min(nx, ny) >= 0:
            n = nx*nx + 3*nx + 2*nx*ny + ny + ny*ny + number
            if sum(1 if c == '1' else 0 for c in bin(n)) % 2 == 0:
                to_explore.append(((nx, ny), length + 1))

    if done:
        break

print(res)


# PART 2
print(len(less_than_fifty))


