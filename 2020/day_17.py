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
neighbours = [(dx, dy, dz) for dx in [-1, 0, 1] for dy in [-1, 0, 1] for dz in [-1, 0, 1] if not (dx == 0 and dy == 0 and dz == 0)]

actives = set()
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == '#':
            actives.add((i, j, 0))

enveloppe = [[0, len(lines) - 1], [0, len(lines[0]) - 1], [0, 0]]

for _ in range(0, 6):
    newactives = set()

    for e in enveloppe:
        e[0] -= 1
        e[1] += 1

    for x in range(enveloppe[0][0], enveloppe[0][1] + 1):
        for y in range(enveloppe[1][0], enveloppe[1][1] + 1):
            for z in range(enveloppe[2][0], enveloppe[2][1] + 1):
                n = sum([1 if (x+dx, y+dy, z+dz) in actives else 0 for dx, dy, dz in neighbours])

                if (x, y, z) in actives and n in [2, 3]:
                    newactives.add((x, y, z))

                if (x, y, z) not in actives and n == 3:
                    newactives.add((x, y, z))

    actives = newactives

res = len(actives)
print(res)


# PART 2
neighbours = [(dx, dy, dz, dw) for dx in [-1, 0, 1] for dy in [-1, 0, 1] for dz in [-1, 0, 1] for dw in [-1, 0, 1] if not (dx == 0 and dy == 0 and dz == 0 and dw == 0)]

actives = set()
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == '#':
            actives.add((i, j, 0, 0))

enveloppe = [[0, len(lines) - 1], [0, len(lines[0]) - 1], [0, 0], [0, 0]]

for _ in range(0, 6):
    newactives = set()

    for e in enveloppe:
        e[0] -= 1
        e[1] += 1

    for x in range(enveloppe[0][0], enveloppe[0][1] + 1):
        for y in range(enveloppe[1][0], enveloppe[1][1] + 1):
            for z in range(enveloppe[2][0], enveloppe[2][1] + 1):
                for w in range(enveloppe[3][0], enveloppe[3][1] + 1):
                    n = sum([1 if (x+dx, y+dy, z+dz, w+dw) in actives else 0 for dx, dy, dz, dw in neighbours])

                    if (x, y, z, w) in actives and n in [2, 3]:
                        newactives.add((x, y, z, w))

                    if (x, y, z, w) not in actives and n == 3:
                        newactives.add((x, y, z, w))

    actives = newactives

res = len(actives)
print(res)


