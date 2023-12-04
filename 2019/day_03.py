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
wire1 = lines[0].split(',')
wire2 = lines[1].split(',')

wire1_points = set()
x, y = 0, 0
for inst in wire1:
    d, n = inst[0], int(inst[1:])

    for _ in range(0, n):
        if d == 'R':
            x += 1

        if d == 'L':
            x -= 1

        if d == 'U':
            y += 1

        if d == 'D':
            y -= 1

        wire1_points.add((x, y))


x, y = 0, 0
intersections = set()
for inst in wire2:
    d, n = inst[0], int(inst[1:])

    for _ in range(0, n):
        if d == 'R':
            x += 1

        if d == 'L':
            x -= 1

        if d == 'U':
            y += 1

        if d == 'D':
            y -= 1

        if (x, y) in wire1_points:
            intersections.add((x, y))


best = 999999999999  # Hu hu hu
for x, y in intersections:
    d = abs(x) + abs(y)
    if d < best:
        best = d

print(best)


# PART 2
wire1_points = dict()
x, y = 0, 0
steps = 0
for inst in wire1:
    d, n = inst[0], int(inst[1:])

    for _ in range(0, n):
        steps += 1

        if d == 'R':
            x += 1

        if d == 'L':
            x -= 1

        if d == 'U':
            y += 1

        if d == 'D':
            y -= 1

        if (x, y) not in wire1_points:
            wire1_points[(x, y)] = steps


x, y = 0, 0
steps = 0
intersections = dict()
for inst in wire2:
    d, n = inst[0], int(inst[1:])

    for _ in range(0, n):
        steps += 1

        if d == 'R':
            x += 1

        if d == 'L':
            x -= 1

        if d == 'U':
            y += 1

        if d == 'D':
            y -= 1

        if (x, y) in wire1_points and (x, y) not in intersections:
            intersections[(x, y)] = steps


best = 999999999999  # Hu hu hu
for k, v in intersections.items():
    d = v + wire1_points[k]
    if d < best:
        best = d

print(best)








