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
droites = []
for l in lines:
    one, two = l.split(' -> ')
    x1, y1 = one.split(',')
    x2, y2 = two.split(',')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    droites.append(((x1, y1), (x2, y2)))

# mx = min([min(p[0], q[0]) for p, q in droites])
# Mx = max([max(p[0], q[0]) for p, q in droites])

# my = min([min(p[1], q[1]) for p, q in droites])
# My = max([max(p[1], q[1]) for p, q in droites])

points = dict()
for p, q in droites:
    if p[0] == q[0]:
        for y in range(min(p[1], q[1]), max(p[1], q[1]) + 1):
            if (p[0], y) not in points:
                points[(p[0], y)] = 1
            else:
                points[(p[0], y)] += 1

    elif p[1] == q[1]:
        for x in range(min(p[0], q[0]), max(p[0], q[0]) + 1):
            if (x, p[1]) not in points:
                points[(x, p[1])] = 1
            else:
                points[(x, p[1])] += 1

    else:
        continue

res = 0
for point, v in points.items():
    if v >= 2:
        res += 1

print(res)


# PART 2
for p, q in droites:
    if p[0] != q[0] and p[1] != q[1]:
        dx, dy = q[0] - p[0], q[1] - p[1]
        N = abs(dx)
        dx, dy = -1 if dx < 0 else 1, -1 if dy < 0 else 1

        for n in range(0, N+1):
            point = (p[0] + n * dx, p[1] + n * dy)

            if point not in points:
                points[point] = 1
            else:
                points[point] += 1


res = 0
for point, v in points.items():
    if v >= 2:
        res += 1

print(res)








