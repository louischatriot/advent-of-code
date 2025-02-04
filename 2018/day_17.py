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
    lines = [line[0:-1] for line in file]


# PART 1
BIG = float('inf')
xm, xM, ym, yM = BIG, -BIG, BIG, -BIG
data = list()
for line in lines:
    datum = dict()

    for part in line.split(', '):
        d, v = part.split('=')
        if '..' in v:
            l, h = v.split('..')
        else:
            l, h = v, v
        l, h = int(l), int(h)
        datum[d] = [l, h]

        if d == 'x':
            xm = min(xm, l)
            xM = max(xM, h)
        else:
            ym = min(ym, l)
            yM = max(yM, h)

    data.append(datum)

# Allow for overflow left and right
xm -= 5
xM += 5

matrix = [['.' for x in range(xm, xM+1)] for y in range(yM+1)]
for datum in data:
    for x, y in itertools.product(range(datum['x'][0], datum['x'][1]+1), range(datum['y'][0], datum['y'][1]+1)):
        matrix[y][x-xm] = '#'

initial_fountain = (0, 500)
fountains = deque()
fountains.append(initial_fountain)
done = set()

while fountains:
    fountain = fountains.popleft()
    if fountain in done:
        continue
    else:
        done.add(fountain)

    yf, xf = fountain
    yb = yf
    while yb <= yM and matrix[yb][xf-xm] != '#':
        yb += 1

    yb -= 1  # Went one step too far

    # Fill the cascade
    for y in range(yf, yb+1):
        matrix[y][xf - xm] = '|'

    # Reached the end, don't spill
    if yb == yM:
        continue

    # Fill the box
    for y in range(yb, 0, -1):
        new_fountains = list()

        xh = xf
        while True:
            if matrix[y][xh - xm] == '#':
                xh -= 1
                break

            if matrix[y+1][xh - xm] in ['.', '|']:
                new_fountains.append((y, xh))
                break

            xh += 1

        xl = xf
        while True:
            if matrix[y][xl - xm] == '#':
                xl += 1
                break

            if matrix[y+1][xl - xm] in ['.', '|']:
                new_fountains.append((y, xl))
                break

            xl -= 1

        char = '~' if len(new_fountains) == 0 else '|'


        for x in range(xl, xh+1):
            matrix[y][x-xm] = char

        if len(new_fountains) >= 1:
            break

    # Register new fountains after having filled
    for f in new_fountains:
        fountains.append(f)


# print("===================================================")
# for l in matrix:
    # print(''.join(l))


# Remove 1 because the initial fountain should not be counted
res = sum(1 if matrix[y][x-xm] in ['~', '|'] else 0 for y, x in itertools.product(range(ym, yM+1), range(xm, xM+1)))
print(res)


# PART 2
res = sum(1 if matrix[y][x-xm] in ['~'] else 0 for y, x in itertools.product(range(ym, yM+1), range(xm, xM+1)))
print(res)






