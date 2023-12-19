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
instructions = []
for l in lines:
    inst, color = l.split(' (')
    color = color[0:-1]
    inst = inst.split(' ')
    inst[1] = int(inst[1])
    instructions.append((inst[0], inst[1], color))

dirs = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1)
}

holes = set()
holes.add((0, 0))

i, j = 0, 0
mi, Mi, mj, Mj = 0, 0, 0, 0
for dir, v, _ in instructions:
    di, dj = dirs[dir]
    for _ in range(v):
        i, j = i+di, j+dj
        holes.add((i, j))
        mi, Mi, mj, Mj = min(mi, i), max(Mi, i), min(mj, j), max(Mj, j)

# u.print_set(holes, ' ')

# Works with nice inputs :)
i0, j0 = None, None
for j in range(mj, Mj+1):
    if (mi+1, j) in holes:
        i0, j0 = mi+1,j+1
        break

inner = set()
to_explore = set()
to_explore.add((i0, j0))

while len(to_explore) > 0:
    i, j = to_explore.pop()
    inner.add((i, j))

    for di, dj in u.ortho_neighbours:
        ni, nj = i+di, j+dj
        if (ni, nj) not in inner and (ni, nj) not in holes:
            to_explore.add((ni, nj))

res = len(holes) + len(inner)
print(res)


# PART 2
digit_to_dir = ['R', 'D', 'L', 'U']
area = 0
perimeter = 0

i, j = 0, 0
for _, _, v in instructions:
    dir = digit_to_dir[int(v[-1])]
    v = int(v[1:-1], 16)
    former_i, former_j = i, j

    if dir == 'R':
        j += v

    elif dir == 'L':
        j -= v

    elif dir == 'D':
        i += v

    elif dir == 'U':
        i -= v

    else:
        raise ValueError("Unexpected direction")

    area += (former_j + j) * (former_i - i)
    perimeter += abs(i - former_i) + abs(j - former_j)

res = abs(area) // 2 + perimeter // 2 + 1
print(res)



