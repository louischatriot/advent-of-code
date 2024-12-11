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


# PART 1 & 2
matrix = [[int(c) for c in l] for l in lines]
N, M = len(matrix), len(matrix[0])

def paths_from(i, j, matrix):
    if matrix[i][j] == 9:
        yield [(i, j)]
        return

    for ni, nj, v in u.ortho_neighbours_iterator(matrix, i, j):
        if v == matrix[i][j] + 1:
            for path in paths_from(ni, nj, matrix):
                yield [(i, j)] + path

zeroes = list()
for i, j in itertools.product(range(N), range(M)):
    if matrix[i][j] == 0:
        zeroes.append((i, j))

part1 = 0
part2 = 0
for i, j in zeroes:
    score = set()

    for path in paths_from(i, j, matrix):
        score.add(path[-1])
        part2 += 1

    part1 += len(score)

print(part1)
print(part2)

