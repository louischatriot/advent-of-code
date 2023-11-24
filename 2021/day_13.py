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
points = set()
folds = []
for l in lines:
    if l == '':
        continue

    if l[0] == 'f':
        fold = l[11:].split('=')
        folds.append((fold[0], int(fold[1])))
        continue

    x, y = l.split(',')
    points.add((int(x), int(y)))

axis, value = folds[0]
new_points = set()

if axis == 'x':
    for x, y in points:
        if x > value:
            new_points.add((2 * value - x, y))
        else:
            new_points.add((x, y))

if axis == 'y':
    for x, y in points:
        if y > value:
            new_points.add((x, 2 * value - y))
        else:
            new_points.add((x, y))

print(len(new_points))


# PART 2
points = new_points

for axis, value in folds[1:]:
    new_points = set()

    if axis == 'x':
        for x, y in points:
            if x > value:
                new_points.add((2 * value - x, y))
            else:
                new_points.add((x, y))

    if axis == 'y':
        for x, y in points:
            if y > value:
                new_points.add((x, 2 * value - y))
            else:
                new_points.add((x, y))

    points = new_points

mx, Mx, my, My = 99999999999, -99999999999, 9999999999, -99999999999
for x, y in points:
    mx = min(mx, x)
    Mx = max(Mx, x)
    my = min(my, y)
    My = max(My, y)


matrix = [['.' for _ in range(0, Mx-mx+1)] for _ in range(0, My-my+1)]

for x, y in points:
    matrix[y-my][x-mx] = '#'

for l in matrix:
    print(''.join(l))





