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
    lines = [line[0:-1] for line in file]


# PART 1
BIG = float('inf')
xm, xM, ym, yM = BIG, -BIG, 0, -BIG
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
            yM = max(yM, h)

    data.append(datum)


for d in data:
    print(d)

print(xm, xM, ym, yM)


# Allow for overflow left and right
xm -= 1
xM += 1


matrix = [['.' for x in range(xm, xM+1)] for y in range(yM+1)]

for datum in data:
    for x, y in itertools.product(range(datum['x'][0], datum['x'][1]+1), range(datum['y'][0], datum['y'][1]+1)):
        matrix[y][x-xm] = '#'


for l in matrix:
    print(''.join(l))







