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
def flip_h(matrix):
    return [[c for c in reversed(line)] for line in matrix]

def flip_v(matrix):
    return [[c for c in line] for line in reversed(matrix)]

def rot_90(matrix):
    N = len(matrix)  # Assumes square matrix
    res = [[None for _ in range(N)] for _ in range(N)]
    for i, j in itertools.product(range(N), range(N)):
        res[i][j] = matrix[j][N - 1 - i]
    return res

def flatten(matrix):
    return '/'.join([''.join(line) for line in matrix])

def expand(line):
    return [[c for c in chunk] for chunk in line.split('/')]

rules = dict()
for line in lines:
    pat, res = line.split(' => ')
    m = expand(pat)
    __keys = set(rules.keys())

    for mm in [m, rot_90(m), rot_90(rot_90(m)), rot_90(rot_90(rot_90(m)))]:
        for entry in [flatten(mm), flatten(flip_h(mm)), flatten(flip_v(mm))]:
            if entry in __keys:
                raise ValueError("Conflict")

            rules[entry] = res




grid = ".#./..#/###"
grid = expand(grid)

R = 18
for r in range(R):
    N = len(grid)
    S = 2 if N % 2 == 0 else 3
    BIG_N = N // S

    new_grid = [[[[None for _ in range(S)] for _ in range(S)] for _ in range(BIG_N)] for _ in range(BIG_N)]
    for I, J in itertools.product(range(BIG_N), range(BIG_N)):
        for i, j in itertools.product(range(S), range(S)):
            new_grid[I][J][i][j] = grid[S * I + i][S * J + j]


    for I, J in itertools.product(range(BIG_N), range(BIG_N)):
        KEY = flatten(new_grid[I][J])

        # print(">>>", backtrack[KEY])

        new_grid[I][J] = expand(rules[KEY])


    S += 1
    grid = [[None for _ in range(BIG_N * S)] for _ in range(BIG_N * S)]


    for I, J in itertools.product(range(BIG_N), range(BIG_N)):
        for i, j in itertools.product(range(S), range(S)):
            grid[S * I + i][S * J + j] = new_grid[I][J][i][j]

    if r in [4, 17]:
        res = 0
        for l in grid:
            for c in l:
                if c == '#':
                    res += 1
        print(res)








