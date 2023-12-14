import sys
import re
import u as u
from collections import defaultdict
import math
import itertools

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
matrix = [[c for c in l] for l in lines]
N, M = len(matrix), len(matrix[0])
bios = set()

bio = sum(2**(N*i + j) if matrix[i][j] == '#' else 0 for i, j in itertools.product(range(N), range(M)))
bios.add(bio)

R = 10000
for r in range(0, R):
    new_matrix = [[matrix[i][j] for j in range(M)] for i in range(N)]

    for i, j in itertools.product(range(N), range(M)):
        adj = 0
        for di, dj in u.ortho_neighbours:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M:
                if matrix[ni][nj] == '#':
                    adj += 1

        if matrix[i][j] == '#' and adj != 1:
            new_matrix[i][j] = '.'

        elif matrix[i][j] == '.' and adj in [1, 2]:
            new_matrix[i][j] = '#'

    matrix = new_matrix

    bio = sum(2**(N*i + j) if matrix[i][j] == '#' else 0 for i, j in itertools.product(range(N), range(M)))
    if bio in bios:
        print(bio)
        break
    else:
        bios.add(bio)


# PART 2
# Not generalizing to any N and M
def neighbours(node):
    depth, i, j = node
    res = []

    if i == 2 and j == 2:
        raise ValueError("Can't look at center tile")

    for di, dj in u.ortho_neighbours:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M:
            if ni != 2 or nj != 2:
                res.append((depth, ni, nj))

    if i == 0:
        res.append((depth-1, 1, 2))

    if i == N-1:
        res.append((depth-1, 3, 2))

    if j == 0:
        res.append((depth-1, 2, 1))

    if j == M-1:
        res.append((depth-1, 2, 3))

    if i == 1 and j == 2:
        res += [(depth+1, 0, jd) for jd in range(0, M)]

    if i == 2 and j == 1:
        res += [(depth+1, id, 0) for id in range(0, N)]

    if i == 3 and j == 2:
        res += [(depth+1, N-1, jd) for jd in range(0, M)]

    if i == 2 and j == 3:
        res += [(depth+1, id, M-1) for id in range(0, N)]

    return res


bugs = set()
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == '#':
            bugs.add((0, i, j))

R = 200
for r in range(0, R):
    to_try = set()
    for node in bugs:
        for n in neighbours(node):
            to_try.add(n)

    new_bugs = set()
    for node in to_try:
        adj = 0
        for bug in neighbours(node):
            if bug in bugs:
                adj += 1

        if node in bugs and adj == 1:
            new_bugs.add(node)

        elif node not in bugs and adj in [1, 2]:
            new_bugs.add(node)

    bugs = new_bugs

print(len(bugs))












