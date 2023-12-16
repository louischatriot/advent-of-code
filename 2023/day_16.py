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
I, J = len(matrix), len(matrix[0])

dirs = {
    'right': (0, 1),
    'left': (0, -1),
    'up': (-1, 0),
    'down': (1, 0)
}

neutral = {
    'right': '-',
    'left': '-',
    'up': '|',
    'down': '|'
}

reflection = {
    'right': { '/': 'up', '\\': 'down' },
    'left': { '/': 'down', '\\': 'up' },
    'up': { '/': 'right', '\\': 'left' },
    'down': { '/': 'left', '\\': 'right' }
}

def print_done(matrix, energized):
    I, J = len(matrix), len(matrix[0])
    done = [['.' for _ in range(J)] for _ in range(I)]
    for coord, v in energized.items():
        i, j = coord
        done[i][j] = str(v)

    for l, ll in zip(matrix, done):
        print(''.join(l), "       ", ''.join(ll))


def calc_energized(matrix, i0, j0, dir0):
    energized = defaultdict(lambda: set())
    to_beam = list()
    to_beam.append((i0, j0, dir0))

    while len(to_beam) > 0:
        beam, to_beam = to_beam[0], to_beam[1:]
        i, j, dir = beam

        while True:
            energized[(i, j)].add(dir)

            # Continue ray
            if matrix[i][j] in ['.', neutral[dir], '/', '\\']:
                if matrix[i][j] in ['/', '\\']:
                    dir = reflection[dir][matrix[i][j]]

                di, dj = dirs[dir]
                i, j = i+di, j+dj

                # Beam out of bounds
                if not (0 <= i < I and 0 <= j < J):
                    break
                else:
                    continue

            # Split -
            if matrix[i][j] == '-':
                if j > 0 and 'left' not in energized[(i, j-1)]:
                    to_beam.append((i, j-1, 'left'))

                if j < J-1 and 'right' not in energized[(i, j+1)]:
                    to_beam.append((i, j+1, 'right'))

                break

            # Split |
            if matrix[i][j] == '|':
                if i > 0 and 'up' not in energized[(i-1, j)]:
                    to_beam.append((i-1, j, 'up'))

                if i < I-1 and 'down' not in energized[(i+1, j)]:
                    to_beam.append((i+1, j, 'down'))

                break

    return len(energized)


print(calc_energized(matrix, 0, 0, 'right'))


# PART 2
res = 0
for i in range(I):
    res = max(res, calc_energized(matrix, i, 0, 'right'))
    res = max(res, calc_energized(matrix, i, J-1, 'left'))

for j in range(J):
    res = max(res, calc_energized(matrix, 0, j, 'down'))
    res = max(res, calc_energized(matrix, I-1, j, 'up'))

print(res)





