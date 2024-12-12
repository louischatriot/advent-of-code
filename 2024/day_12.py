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


# PART 1
matrix = [[c for c in l] for l in lines]
N, M = len(matrix), len(matrix[0])
regions = u.get_matrix_regions(matrix)


part1, part2 = 0, 0
for name, region in regions:
    area = len(region)
    perimeter = 4 * area - sum(1 if (i + di, j+ dj) in region else 0 for di, dj in u.ortho_neighbours for i, j in region)

    horiz = [list() for _ in range(N+1)]
    vert = [list() for _ in range(M+1)]

    for i, j in region:
        if (i-1, j) not in region:
            horiz[i].append((j, -1))

        if (i+1, j) not in region:
            horiz[i+1].append((j, 1))

        if (i, j-1) not in region:
            vert[j].append(i)

        if (i, j+1) not in region:
            vert[j+1].append(i)

    horiz = [sorted(h) for h in horiz]
    vert = [sorted(v) for v in horiz]
    sides = 0

    for h in horiz:
        sides += len(h)
        for h1, h2 in u.pairwise(h):
            h1v, h1d = h1
            h2v, h2d = h2

            if h2v == h1v + 1 and h1d == h2d:
                sides -= 1

    for v in vert:
        sides += len(v)
        for v1, v2 in u.pairwise(v):
            v1v, v1d = v1
            v2v, v2d = v2

            if v2v == v1v + 1 and v1d == v2d:
                sides -= 1

    part1 += area * perimeter
    part2 += area * sides



print(part1)
print(part2)


