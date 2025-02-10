import sys
import re
import u as u
from collections import defaultdict, deque
import math
import itertools
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line[0:-1] for line in file]


# PART 1
points = list()
for line in lines:
    x, y, z, t = line.split(',')
    x, y, z, t = int(x), int(y), int(z), int(t)
    points.append((x, y, z, t))


def d(p1, p2):
    x1, y1, z1, t1 = p1
    x2, y2, z2, t2 = p2

    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2) + abs(t1-t2)


edges = defaultdict(lambda: list())
for p1, p2 in itertools.combinations(points, 2):
    if d(p1, p2) <= 3:
        edges[p1].append(p2)
        edges[p2].append(p1)


res = 0
seen = set()

for point in points:
    if point in seen:
        continue

    res += 1

    to_explore = deque()
    to_explore.append(point)
    while to_explore:
        pt = to_explore.popleft()

        if pt in seen:
            continue
        else:
            seen.add(pt)

        for npt in edges[pt]:
            to_explore.append(npt)


print(res)



