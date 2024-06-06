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
I, J = 6, 50
if is_example:
    I, J = 3, 7

matrix = [['.' for _ in range(J)] for _ in range(I)]

for line in lines:
    if line[0:4] == 'rect':
        w, h = line[5:].split('x')
        w, h = int(w), int(h)
        for i, j in itertools.product(range(h), range(w)):
            matrix[i][j] = '#'

        continue

    contents = line.split(' ')
    t = int(contents[2][2:])
    offset = int(contents[4])

    if contents[1] == 'row':
        matrix[t] = [matrix[t][(j - offset) % J] for j in range(J)]
    else:
        new_col = [matrix[(i - offset) % I][t] for i in range(I)]
        for i in range(I):
            matrix[i][t] = new_col[i]

for l in matrix:
    print(' '.join(l))

print(sum(1 if matrix[i][j] == '#' else 0 for i, j in itertools.product(range(I), range(J))))




