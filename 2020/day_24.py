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
def parse_line(l):
    i, j = 0, 0

    while len(l) > 0:
        if l[0] == 'e':
            i += 1
            l = l[1:]

        elif l[0] == 'w':
            i -= 1
            l = l[1:]

        elif l[0:2] == 'ne':
            j += 1
            l = l[2:]

        elif l[0:2] == 'sw':
            j -= 1
            l = l[2:]

        elif l[0:2] == 'se':
            i += 1
            j -= 1
            l = l[2:]

        elif l[0:2] == 'nw':
            i -= 1
            j += 1
            l = l[2:]

    return i, j

blacks = set()
for l in lines:
    i, j = parse_line(l)

    if (i, j) in blacks:
        blacks.remove((i, j))
    else:
        blacks.add((i, j))

res = len(blacks)
print(res)


# PART 2
neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]

for _ in range(0, 100):
    to_look_at = set()
    for i, j in blacks:
        for di, dj in neighbours:
            to_look_at.add((i+di, j+dj))

    new_blacks = set()
    for i, j in to_look_at:
        n = sum([1 if (i+di, j+dj) in blacks else 0 for di, dj in neighbours])

        if (i, j) in blacks and not (n == 0 or n > 2):
            new_blacks.add((i, j))

        if (i, j) not in blacks and n == 2:
            new_blacks.add((i, j))

    blacks = new_blacks

res = len(blacks)
print(res)



