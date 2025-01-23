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
matrix = [[c for c in line] for line in lines]
N, M = len(matrix), len(matrix[0])
if N != M:
    raise ValueError("Expecting square")

m = N // 2
infected = set()
for i, j in itertools.product(range(N), repeat=2):
    if matrix[i][j] == '#':
        infected.add((i-m, j-m))

i, j = 0, 0
di, dj = -1, 0

res = 0
R = 10000
for _ in range(R):
    if (i, j) in infected:
        di, dj = u.right[(di, dj)]
    else:
        di, dj = u.left[(di, dj)]

    if (i, j) in infected:
        infected.remove((i, j))
    else:
        res += 1
        infected.add((i, j))

    i, j = i+di, j+dj

print(res)


# PART 2
state = dict()
for i, j in itertools.product(range(N), repeat=2):
    if matrix[i][j] == '#':
        state[(i-m, j-m)] = 'infected'

i, j = 0, 0
di, dj = -1, 0

res = 0
R = 10000000
for _ in range(R):
    if (i, j) not in state:
        di, dj = u.left[(di, dj)]
        state[(i, j)] = 'weakened'

    elif state[(i, j)] == 'weakened':
        res += 1
        state[(i, j)] = 'infected'

    elif state[(i, j)] == 'infected':
        di, dj = u.right[(di, dj)]
        state[(i, j)] = 'flagged'

    elif state[(i, j)] == 'flagged':
        di, dj = -di, -dj
        del state[(i, j)]

    else:
        raise ValueError("Unknown state")


    i, j = i+di, j+dj

print(res)





