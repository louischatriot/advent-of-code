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
digits = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

i, j = 1, 1
m, M = 0, 2
res = ''

for line in lines:
    for c in line:
        if c == 'U':
            i = max(m, i-1)
        elif c == 'D':
            i = min(M, i+1)
        elif c == 'R':
            j = min(M, j+1)
        elif c == 'L':
            j = max(m, j-1)
        else:
            raise ValueError()

    res += digits[i][j]

print(res)


# PART 2
digits = [
    ['N', 'N', '1', 'N', 'N'],
    ['N', '2', '3', '4', 'N'],
    ['5', '6', '7', '8', '9'],
    ['N', 'A', 'B', 'C', 'N'],
    ['N', 'N', 'D', 'N', 'N']
]

i, j = 2, 0
m, M = 0, 4
res = ''

for line in lines:
    for c in line:
        di, dj = 0, 0
        if c == 'U':
            di = -1
        elif c == 'D':
            di = 1
        elif c == 'R':
            dj = 1
        elif c == 'L':
            dj = -1
        else:
            raise ValueError()

        if (m <= i+di <= M) and (m <= j+dj <= M):
            if digits[i+di][j+dj] != 'N':
                i, j = i+di, j+dj

    res += digits[i][j]

print(res)


