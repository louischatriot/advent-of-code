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
N = 1000
grid = [[0 for _ in range(N)] for _ in range(N)]

for l in lines:
    if l[0:3] == 'tog':
        op = 'toggle'
        coords = l[7:]
    elif l[0:7] == 'turn on':
        op = 'on'
        coords = l[8:]
    elif l[0:7] == 'turn of':
        op = 'off'
        coords = l[9:]
    else:
        raise ValueError("Unexpected op")

    m, M = coords.split(' through ')
    mi, mj = m.split(',')
    Mi, Mj = M.split(',')
    mi, mj, Mi, Mj = int(mi), int(mj), int(Mi), int(Mj)

    for i in range(mi, Mi+1):
        for j in range(mj, Mj+1):
            if op == 'on':
                grid[i][j] = 1
            elif op == 'off':
                grid[i][j] = 0
            elif op == 'toggle':
                grid[i][j] = 1 - grid[i][j]
            else:
                raise ValueError("Wow")

res = sum(grid[i][j] for i, j in itertools.product(range(N), range(N)))
print(res)


# PART 2
grid = [[0 for _ in range(N)] for _ in range(N)]

for l in lines:
    if l[0:3] == 'tog':
        op = 'toggle'
        coords = l[7:]
    elif l[0:7] == 'turn on':
        op = 'on'
        coords = l[8:]
    elif l[0:7] == 'turn of':
        op = 'off'
        coords = l[9:]
    else:
        raise ValueError("Unexpected op")

    m, M = coords.split(' through ')
    mi, mj = m.split(',')
    Mi, Mj = M.split(',')
    mi, mj, Mi, Mj = int(mi), int(mj), int(Mi), int(Mj)

    for i in range(mi, Mi+1):
        for j in range(mj, Mj+1):
            if op == 'on':
                grid[i][j] += 1
            elif op == 'off':
                grid[i][j] -= 1
                grid[i][j] = max(0, grid[i][j])
            elif op == 'toggle':
                grid[i][j] += 2
            else:
                raise ValueError("Wow")

res = sum(grid[i][j] for i, j in itertools.product(range(N), range(N)))
print(res)


