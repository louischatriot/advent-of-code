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
N, M = len(lines), len(lines[0])
matrix = [[c for c in line] for line in lines]

R = 10
for _ in range(R):
    nm = [[None for _ in range(M)] for _ in range(N)]

    for i, j in itertools.product(range(N), range(M)):
        if matrix[i][j] == '.':
            n = sum(1 if v == '|' else 0 for _, _, v in u.neighbours_not_center_iterator(matrix, i, j))
            if n >= 3:
                nm[i][j] = '|'
            else:
                nm[i][j] = '.'

        elif matrix[i][j] == '|':
            n = sum(1 if v == '#' else 0 for _, _, v in u.neighbours_not_center_iterator(matrix, i, j))
            if n >= 3:
                nm[i][j] = '#'
            else:
                nm[i][j] = '|'

        elif matrix[i][j] == '#':
            nl = sum(1 if v == '#' else 0 for _, _, v in u.neighbours_not_center_iterator(matrix, i, j))
            nt = sum(1 if v == '|' else 0 for _, _, v in u.neighbours_not_center_iterator(matrix, i, j))
            if nl >= 1 and nt >= 1:
                nm[i][j] = '#'
            else:
                nm[i][j] = '.'

        else:
            raise ValueError("Unknown acre")

    matrix = nm

res = sum(1 if matrix[i][j] == '|' else 0 for i, j in itertools.product(range(N), range(M)))
res *= sum(1 if matrix[i][j] == '#' else 0 for i, j in itertools.product(range(N), range(M)))
print(res)


# PART 2
matrix = [[c for c in line] for line in lines]
seen = dict()

# Was used to find the cycle start and size
# R = 2000

cycle = 28
start = 475
TARGET = 1000000000

a = TARGET - start
a = a % cycle
R = a + start
for r in range(R):
    # Used to find cycle start and size
    # key = '==='.join([';'.join(l) for l in matrix])

    # if key in seen:
        # print(seen[key], r)
        # break
    # else:
        # seen[key] = r

    nm = [[None for _ in range(M)] for _ in range(N)]

    for i, j in itertools.product(range(N), range(M)):
        if matrix[i][j] == '.':
            n = sum(1 if v == '|' else 0 for _, _, v in u.neighbours_not_center_iterator(matrix, i, j))
            if n >= 3:
                nm[i][j] = '|'
            else:
                nm[i][j] = '.'

        elif matrix[i][j] == '|':
            n = sum(1 if v == '#' else 0 for _, _, v in u.neighbours_not_center_iterator(matrix, i, j))
            if n >= 3:
                nm[i][j] = '#'
            else:
                nm[i][j] = '|'

        elif matrix[i][j] == '#':
            nl = sum(1 if v == '#' else 0 for _, _, v in u.neighbours_not_center_iterator(matrix, i, j))
            nt = sum(1 if v == '|' else 0 for _, _, v in u.neighbours_not_center_iterator(matrix, i, j))
            if nl >= 1 and nt >= 1:
                nm[i][j] = '#'
            else:
                nm[i][j] = '.'

        else:
            raise ValueError("Unknown acre")

    matrix = nm


res = sum(1 if matrix[i][j] == '|' else 0 for i, j in itertools.product(range(N), range(M)))
res *= sum(1 if matrix[i][j] == '#' else 0 for i, j in itertools.product(range(N), range(M)))
print(res)



