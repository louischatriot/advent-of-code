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
reds = list()
for line in lines:
    red = line.split(',')
    reds.append((int(red[0]), int(red[1])))

best = 0
for r1, r2 in itertools.combinations(reds, 2):
    x1, y1 = r1
    x2, y2 = r2

    xm, xM = min(x1, x2), max(x1, x2)
    ym, yM = min(y1, y2), max(y1, y2)

    surface = (xM - xm + 1) * (yM - ym + 1)
    best = max(best, surface)

print(best)


# PART 2
# Verified that
# We always change direction
# No vertical path touches another (two horizontal ones do but we don't care)
# Every vertical and horizontal has only one segment
# SCRATCH THAT, actually just checking if an edge is in the rectangle works, though
# I think it is wrong in the general case, the input is too nice. Correct approach would be to check
# Every rectangle line by line, for which you need to first calculate the inner boundary or the polygon
# which is a freaking pain so I'm not doing it
verticals = set()
vert_bounds = defaultdict(lambda: list())

horizontals = set()
horiz_bounds = defaultdict(lambda: list())

for r1, r2 in itertools.chain(u.pairwise(reds), [(reds[-1], reds[0])]):
    x1, y1 = r1
    x2, y2 = r2

    if x1 == x2:
        verticals.add(x1)
        ym, yM = min(y1, y2), max(y1, y2)
        vert_bounds[x1].append((ym, yM))

    if y1 == y2:
        horizontals.add(y1)
        xm, xM = min(x1, x2), max(x1, x2)
        horiz_bounds[y1].append((xm, xM))


verticals = sorted(list(verticals))
horizontals = sorted(list(horizontals))

for x in verticals:
    vert_bounds[x] = vert_bounds[x][0]

for y in horizontals:
    horiz_bounds[y] = horiz_bounds[y][0]

# Find start and offset (to calculate polygon inner boundary)
# start = sorted(reds)[0]
# offset = None
# for i, red in enumerate(reds):
    # if red == start:
        # offset = i

# N = len(reds)
# for i in range(len(reds)):
    # r1 = reds[(i + offset) % N]
    # r2 = reds[(i + offset + 1) % N]

best = 0
for r1, r2 in itertools.combinations(reds, 2):
    x1, y1 = r1
    x2, y2 = r2

    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    if x1 == x2 or y1 == y2:
        continue  # Thin rectangles will not be optimal in a sane scenario

    ok = True
    for x in verticals:
        if x1 < x < x2:
            ym, yM = vert_bounds[x]

            if ym < y2 and yM > y1:
                ok = False

    for y in horizontals:
        if y1 < y < y2:
            xm, xM = horiz_bounds[y]

            if xm < x2 and xM > x1:
                ok = False

    if ok:
        xm, xM = min(x1, x2), max(x1, x2)
        ym, yM = min(y1, y2), max(y1, y2)
        surface = (xM - xm + 1) * (yM - ym + 1)
        best = max(best, surface)

print(best)










