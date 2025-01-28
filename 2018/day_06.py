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
nodes = list()
grid = dict()
xm, xM, ym, yM = u.BIG, -u.BIG, u.BIG, -u.BIG

for line in lines:
    x, y = line.split(', ')
    x, y = int(x), int(y)
    nodes.append((x, y))
    grid[(x, y)] = (x, y)

    xm = min(xm, x)
    xM = max(xM, x)
    ym = min(ym, y)
    yM = max(yM, y)

N = (xM - xm + 1) * (yM - ym + 1)
N *= 12  # After having filled entirely the inner rectangle and part of the outside, the non infinite will have stopped

frontiers = defaultdict(lambda: list())
areas = defaultdict(lambda: 1)


def print_grid():
    corr = dict()
    for i, node in enumerate(nodes):
        corr[node] = chr(ord('a') + i)
    corr['X'] = 'X'

    print("======================================")

    for y in range(ym, yM + 1):
        l = ''.join([corr[grid[(x, y)]] if (x, y) in grid else '.' for x in range(xm, xM + 1)])
        print(l)

    print("======================================")


for node in nodes:
    frontiers[node].append(node)

while True:
    former_areas = {k: v for k, v in areas.items()}


    to_mark = defaultdict(lambda: defaultdict(lambda: 0))
    new_frontiers = defaultdict(lambda: list())

    for node in frontiers:
        for x, y in frontiers[node]:
            for dx, dy in u.ortho_neighbours:
                point = (x+dx, y+dy)
                if point not in grid:
                    to_mark[point][node] += 1

    for point in to_mark:
        if len(to_mark[point]) == 1 and 'X' not in to_mark[point]:
            node = list(to_mark[point].keys())[0]
        else:
            node = 'X'

        grid[point] = node
        areas[node] += 1
        new_frontiers[node].append(point)

    if len(grid) > N:
        break

    frontiers = new_frontiers


res = -u.BIG
for node in areas:
    if node != 'X' and former_areas[node] == areas[node]:
        res = max(res, areas[node])

print(res)



