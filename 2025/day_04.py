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
res = 0
N, M = len(lines), len(lines[0])
matrix = [[c for c in line] for line in lines]

for i, j in itertools.product(range(N), range(M)):
    if matrix[i][j] == '@' and sum(1 if d == '@' else 0 for ii, jj, d in u.neighbours_not_center_iterator(matrix, i, j)) < 4:
        res += 1

print(res)


# PART 2
res = 0

while True:
    to_remove = list()

    for i, j in itertools.product(range(N), range(M)):
        if matrix[i][j] == '@' and sum(1 if d == '@' else 0 for ii, jj, d in u.neighbours_not_center_iterator(matrix, i, j)) < 4:
            to_remove.append((i, j))

    res += len(to_remove)

    for i, j in to_remove:
        matrix[i][j] = '.'

    if len(to_remove) == 0:
        break

print(res)



