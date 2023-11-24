import sys
import re
import u as u
from collections import defaultdict
import math

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
matrix = [[int(n) for n in l] for l in lines]
M = max([max(l) for l in matrix]) + 1

res = 0
low_points = []
for i, l in enumerate(matrix):
    for j, n in enumerate(l):
        if all(n < u.get_pos(matrix, i, j, di, dj, M) for (di, dj) in u.ortho_neighbours):
            res += 1 + n
            low_points.append((i, j))

print(res)


# PART 2
basins = []
for lpi, lpj in low_points:
    todo = [(lpi, lpj)]
    basin = set()

    while len(todo) > 0:
        current, todo = todo[0], todo[1:]
        ci, cj = current
        basin.add(current)

        for di, dj in u.ortho_neighbours:
            level = u.get_pos(matrix, ci, cj, di, dj, M)

            if level == M or level == 9:
                continue

            if level > matrix[ci][cj] and (ci + di, cj + dj) not in basin:
                todo.append((ci + di, cj + dj))

    basins.append(basin)

bs = [len(basin) for basin in basins]
bs = sorted(bs)
print(bs[-1] * bs[-2] * bs[-3])


