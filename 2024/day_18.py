import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import collections
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
N = 7 if is_example else 71
fallen = 12 if is_example else 1024

falling = list()
for line in lines:
    x, y = map(int, line.split(','))
    falling.append((x, y))

def get_path(fallen):
    visited = set(falling[0:fallen])
    start, end = (0, 0), (N-1, N-1)
    to_explore = collections.deque()
    to_explore.append((start, 0))

    while to_explore:
        node, distance = to_explore.popleft()

        if node in visited:
            continue
        visited.add(node)

        if node == end:
            return distance

        i, j = node
        for di, dj in u.ortho_neighbours:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                if (ni, nj) not in visited:
                    to_explore.append(((ni, nj), distance+1))

    return -1

res = get_path(fallen)
print(res)


# PART 2
# Brute force actually works, otherwise we could do a dichotomy
for f in range(fallen, len(falling)):
    if get_path(f) == -1:
        print(falling[f-1])
        break







