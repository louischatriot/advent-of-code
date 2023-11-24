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


# PART 1 & 2
matrix = [[int(c) for c in l] for l in lines]
R = 1000000
N = len(matrix)
M = len(matrix[0])
res = 0

for r in range(0, R):
    to_flash = set()

    for i in range(0, N):
        for j in range(0, M):
            matrix[i][j] = matrix[i][j] + 1
            if matrix[i][j] > 9:
                to_flash.add((i, j))

    to_zero = set()
    while len(to_flash) > 0:
        i, j = to_flash.pop()
        to_zero.add((i, j))

        for di, dj in u.all_neighbours:
            p = (i+di, j+dj)
            if p in to_zero:
                continue

            if not (0 <= i+di < N and 0 <= j+dj < M):
                continue

            matrix[i+di][j+dj] += 1
            if matrix[i+di][j+dj] > 9:
                to_flash.add(p)

    # Uncomment these 3 lines for part 2, comment for part 1
    if len(to_zero) == N * M:
        print(r+1)
        sys.exit(0)

    for i, j in to_zero:
        matrix[i][j] = 0
        res += 1

print(res)

