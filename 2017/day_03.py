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
# Omagad
n = int(lines[0])
r = 1
while (2*r+1) ** 2 < n:
    r += 1

d = (2*r+1) ** 2 - n
x, y = r, r

if d >= 2*r:
    x = -r
    d -= 2*r
else:
    x -= d
    d = 0

if d >= 2*r:
    y = -r
    d -= 2*r
else:
    y -= d
    d = 0

if d >= 2*r:
    x = r
    d -= 2*r
else:
    x += d
    d = 0

y += d
res = abs(x) + abs(y)
print(res)


# PART 2
grid = defaultdict(lambda: 0)
grid[(0, 0)] = 1

R = 3000
for r in range(1, R):
    def positions():
        x = r
        for y in range(r-1, -r-1, -1):
            yield x, y

        y = -r
        for x in range(r, -r-1, -1):
            yield x, y

        x = -r
        for y in range(-r, r+1):
            yield x, y

        y = r
        for x in range(-r, r+1):
            yield x, y

    for x, y in positions():
        v = sum(grid[(x+dx, y+dy)] for dx, dy in u.all_neighbours)
        if v > n:
            print(v)
            sys.exit(0)
        grid[(x, y)] = v




