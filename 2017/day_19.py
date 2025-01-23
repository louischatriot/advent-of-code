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
    lines = [line for line in file]


# PART 1
matrix = [[c for c in line[0:-1]] for line in lines]
N, M = len(matrix), len(matrix[0])

for j in range(M):
    if matrix[0][j] == '|':
        break

i = 0
di, dj = 1, 0
res = ''
steps = 1

while True:
    c = matrix[i][j]

    # Assuming letters don't change direction
    if 'A' <= c <= 'Z':
        res += c
        ni, nj = i+di, j+dj
        if not (0 <= ni < N) or not (0 <= nj < M) or matrix[ni][nj] == ' ':
            break

    # Assuming there are spaces between all paths :)
    elif c == '+':
        for ci, cj in u.ortho_neighbours:
            if ci + di == 0 and cj + dj == 0:
                continue

            ni, nj = i+ci, j+cj
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] != ' ':
                di, dj = ci, cj
                break

    # Move forward
    i, j = i+di, j+dj
    steps += 1


print(res)
print(steps)

