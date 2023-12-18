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
# So I was doing a line by line analysis of the shape and got always a few off by one
# errors. Then discovered the shoelace formula. Fuck.
# No interest in debugging the line by line that would work but is not interesting

digit_to_dir = ['R', 'D', 'L', 'U']
# rows = defaultdict(lambda: [])

area = 0
perimeter = 0

i, j = 0, 0
for _, _, v in instructions:
    dir = digit_to_dir[int(v[-1])]
    v = int(v[1:-1], 16)
    former_i, former_j = i, j

    if dir == 'R':
        # rows[i].append((j, j+v))
        j += v

    elif dir == 'L':
        # rows[i].append((j-v, j))
        j -= v

    elif dir == 'D':
        # for __i in range(i+1, i+v):
            # rows[__i].append(j)

        i += v

    elif dir == 'U':
        # for __i in range(i-v+1, i):
            # rows[__i].append(j)

        i -= v

    else:
        raise ValueError("Unexpected direction")

    area += (former_j + j) * (former_i - i)
    perimeter += abs(i - former_i) + abs(j - former_j)

res = abs(area) // 2 + perimeter // 2 + 1
print(res)



# def row_value(row):
    # row.sort(key = lambda x: x if type(x) == int else x[0])

    # print(row)

    # m = row[0] if type(row[0]) == int else row[0][0]
    # M = row[-1] if type(row[-1]) == int else row[-1][1]

    # res = 0
    # inner_start = None
    # idx = 0
    # while idx < len(row):
        # v = row[idx]

        # if type(v) == int:
            # if inner_start is None:
                # inner_start = v
                # idx += 1
            # else:
                # res += v - inner_start + 1
                # inner_start = None
                # idx += 1

        # else:  # A pair
            # if inner_start is None:
                # pass
                # # res += v[1] - v[0] + 1
            # else:
                # res -= (v[1] - v[0] + 1)

            # idx += 1
            # continue

    # return res

# row = rows[500254]
# print(row_value(row))


# 1/0

# res = 0
# for i in sorted(rows.keys()):
    # row = rows[i]
    # row.sort(key = lambda x: x if type(x) == int else x[0])

    # inner_start = None
    # idx = 0
    # while idx < len(row):
        # v = row[idx]

        # if type(v) == int:
            # if inner_start is None:
                # inner_start = v
                # idx += 1
            # else:
                # res += v - inner_start + 1
                # inner_start = None
                # idx += 1

        # else:  # A pair
            # if inner_start is None:
                # res += v[1] - v[0] + 1
            # else:
                # res -= (v[1] - v[0] + 1)

            # idx += 1
            # continue





    # # pairs = list()
    # # idx = 0
    # # s = signature(row)
    # # while len(row) > 0:
        # # if len(row) == 1:
            # # print("ROW", i, '-->', row)
            # # if type(row[0]) == int:
                # # raise ValueError("WTF", s)
            # # else:
                # # pairs.append((row[0][0], row[0][1]))
                # # row = []

            # # continue

        # # a, b, row = row[0], row[1], row[2:]

        # # if type(a) == int and type(b) == int:
            # # pairs.append((a, b))
            # # continue

        # # if type(a) != int and type(b) != int:
            # # pairs.append(a)
            # # pairs.append(b)
            # # continue

        # # if type(a) == int and type(b) != int:
            # # pairs.append((a, b[1]))

        # # if type(a) != int and type(b) == int:
            # # pairs.append((a[0], b))



    # LOOK = 356353

    # if abs(LOOK - i) <= 1:
        # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%", i)
        # print(res)
        # print(row)





    # # if len(row) == 2 and type(row[0]) != int and type(row[1]) != int:
        # # res += row[0][1] - row[0][0] + 1
        # # res += row[1][1] - row[1][0] + 1
        # # continue

    # # inner_start = None
    # # idx = 0

    # # while idx < len(row):
        # # if type(row[idx]) != int:
            # # if len(row) == 1:
                # # res += row[idx][1] - row[idx][0] + 1
                # # idx += 1
                # # continue


            # # if idx == 0:
                # # inner_start = row[idx][0]
                # # idx += 1
                # # continue

            # # if idx == len(row) - 1 and inner_start is not None:
                # # res += row[idx][1] - inner_start + 1
                # # idx += 1
                # # continue

            # # if inner_start is None:
                # # res += row[idx][1] - row[idx][0] + 1

            # # idx += 1
            # # continue

        # # if inner_start is None:
            # # inner_start = row[idx]
            # # idx += 1
        # # else:
            # # res += row[idx] - inner_start + 1
            # # inner_start = None
            # # idx += 1

# print(">>>>>>>>>>>>>>>>", res)
# 1/0


