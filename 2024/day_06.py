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


# PART 1 - Overall, not beautiful code
look_ahead = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
nexts = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

i, j = None, None
dir = None
N, M = len(lines), len(lines[0])
for _i, _j in itertools.product(range(N), range(M)):
    if lines[_i][_j] in look_ahead.keys():
        i, j = _i, _j

dir = lines[i][j]

visited = set()
visited.add((i, j))

while True:
    di, dj = look_ahead[dir]
    ni, nj = i+di, j+dj

    if not (0 <= ni < N and 0 <= nj < M):
        break

    # Assuming we can only do one turn, which is a special case but this is AoC day 6
    if lines[ni][nj] == '#':
        dir = nexts[dir]

    di, dj = look_ahead[dir]
    ni, nj = i+di, j+dj

    if not (0 <= ni < N and 0 <= nj < M):
        break

    visited.add((ni, nj))
    i, j = ni, nj


print(len(visited))


# PART 2
def get_loop(lines):
    i, j = None, None
    dir = None
    N, M = len(lines), len(lines[0])

    for _i, _j in itertools.product(range(N), range(M)):
        if lines[_i][_j] in look_ahead.keys():
            i, j = _i, _j

    dir = lines[i][j]

    visited = set()
    visited.add((i, j, dir))

    while True:
        di, dj = look_ahead[dir]
        ni, nj = i+di, j+dj

        if not (0 <= ni < N and 0 <= nj < M):
            break

        # Assuming only one turn did not work anymore for part 2 :)
        for _ in range(2):
            if lines[ni][nj] == '#':
                dir = nexts[dir]

            di, dj = look_ahead[dir]
            ni, nj = i+di, j+dj

        if not (0 <= ni < N and 0 <= nj < M):
            break

        if (ni, nj, dir) in visited:
            return True

        visited.add((ni, nj, dir))
        i, j = ni, nj

    return False

res = 0
matrix = [[lines[i][j] for j in range(M)] for i in range(N)]

import time
s = time.time()

nodes = list(visited)
N = len(nodes)
b = 8
batches = [set(nodes[i * N // b: (i+1) * N // b]) for i in range(b-1)] + [set(nodes[(b-1) * N // b:])]

# Was 13.4s before parallel processing
import ray
ray.init()

@ray.remote
def do_batch(nodes):
    res = 0

    for i, j in nodes:
        if matrix[i][j] == '.':
            matrix[i][j] = '#'
            if get_loop(matrix):
                res += 1

            matrix[i][j] = '.'

    return res

res = [do_batch.remote(batches[i]) for i in range(b)]
res = ray.get(res)
print(sum(res))

print("Time spent: ", time.time() - s)




