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
# On 3 vectors instead of just 2

deltas = {
    'n': (1, 0, 0),
    's': (-1, 0, 0),
    'ne': (0, 1, 0),
    'sw': (0, -1, 0),
    'se': (0, 0, 1),
    'nw': (0, 0, -1),
}

dirs = lines[0].split(',')

def distance(x, y, z):
    if 0 in [x, y, z]:
        return abs(x) + abs(y) + abs(z)

    if y < 0 and z > 0:
        return distance(-x, -y, -z)

    if y < 0 and z < 0:
        return distance(-x, -y, -z)

    if y > 0 and z < 0:
        x, y, z = x + min(y, -z), y - min(y, -z), z + min(y, -z)

        if x >= 0:
            res = x + max(y, -z)
        else:
            res = max(-x, y, -z)

    if y > 0 and z > 0:
        if x > 0:
            x, y, z = x - min(x, z), y + min(x, z), z - min(x, z)
            res = max(x, z) + y

        else:
            x, y, z = x + min(-x, y), y - min(-x, y), z + min(-x, y)
            res = z + max(abs(x), y)

    return res


MAX = 0
x, y, z = 0, 0, 0
for dir in dirs:
    dx, dy, dz = deltas[dir]
    x, y, z = x+dx, y+dy, z+dz
    MAX = max(MAX, distance(x, y, z))


res = distance(x, y, z)
print(res)
print(MAX)





