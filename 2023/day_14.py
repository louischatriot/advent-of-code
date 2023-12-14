import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import numpy as np

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
matrix = [[c for c in l] for l in lines]
N, M = len(matrix), len(matrix[0])

tilted = [['.' for _ in range(M)] for _ in range(N)]

for j in range(M):
    target_i = 0

    for i in range(N):
        if matrix[i][j] == '.':
            continue

        elif matrix[i][j] == '#':
            tilted[i][j] = '#'
            target_i = i+1

        elif matrix[i][j] == 'O':
            tilted[target_i][j] = 'O'
            target_i += 1

        else:
            raise ValueError("Unexpected matrix element")

res = 0
for i, l in enumerate(reversed(tilted)):
    for c in l:
        if c == 'O':
            res += (i+1)

print(res)


# PART 2
# Too lazy to generalize let's copy paste comme un cochon
def roll_rocks(matrix):
    # North
    tilted = [['.' for _ in range(M)] for _ in range(N)]
    for j in range(M):
        target_i = 0

        for i in range(N):
            if matrix[i][j] == '.':
                continue

            elif matrix[i][j] == '#':
                tilted[i][j] = '#'
                target_i = i+1

            elif matrix[i][j] == 'O':
                tilted[target_i][j] = 'O'
                target_i += 1

            else:
                raise ValueError("Unexpected matrix element")
    matrix = tilted

    # West
    tilted = [['.' for _ in range(M)] for _ in range(N)]
    for i in range(N):
        target_j = 0

        for j in range(M):
            if matrix[i][j] == '.':
                continue

            elif matrix[i][j] == '#':
                tilted[i][j] = '#'
                target_j = j+1

            elif matrix[i][j] == 'O':
                tilted[i][target_j] = 'O'
                target_j += 1

            else:
                raise ValueError("Unexpected matrix element")
    matrix = tilted

    # South
    tilted = [['.' for _ in range(M)] for _ in range(N)]
    for j in range(M):
        target_i = N-1

        for i in range(N-1, -1, -1):
            if matrix[i][j] == '.':
                continue

            elif matrix[i][j] == '#':
                tilted[i][j] = '#'
                target_i = i-1

            elif matrix[i][j] == 'O':
                tilted[target_i][j] = 'O'
                target_i -= 1

            else:
                raise ValueError("Unexpected matrix element")
    matrix = tilted

    # East
    tilted = [['.' for _ in range(M)] for _ in range(N)]
    for i in range(N):
        target_j = M-1

        for j in range(M-1, -1, -1):
            if matrix[i][j] == '.':
                continue

            elif matrix[i][j] == '#':
                tilted[i][j] = '#'
                target_j = j-1

            elif matrix[i][j] == 'O':
                tilted[i][target_j] = 'O'
                target_j -= 1

            else:
                raise ValueError("Unexpected matrix element")
    matrix = tilted

    return matrix


matrix = [[c for c in l] for l in lines]

last_signature = '--'.join([''.join(l) for l in matrix])
signatures = dict()
signatures[last_signature] = 0

A_LOT = 99999999999
R = A_LOT  # Hu hu hu
loop_start, loop_end = None, None
for r in range(1, R):
    matrix = roll_rocks(matrix)
    signature = '--'.join([''.join(l) for l in matrix])

    if signature in signatures:
        loop_start = signatures[signature]
        loop_end = r
        break
    else:
        signatures[signature] = r

cycles = 1000000000
cycles -= loop_start
cycles %= (loop_end - loop_start)

for _ in range(cycles):
    matrix = roll_rocks(matrix)

res = 0
for i, l in enumerate(reversed(matrix)):
    for c in l:
        if c == 'O':
            res += (i+1)

print(res)




