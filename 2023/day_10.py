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
pipes = {
    '|': [(0, -1), (0, 1)],
    '-': [(-1, 0), (1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, 1), (-1, 0)],
    'F': [(0, 1), (1, 0)],
    '.': []  # Nothing connected to pure ground
}

matrix = [l for l in lines]
X, Y = len(matrix[0]), len(matrix)
xs, ys = None, None
for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c == 'S':
            xs, ys = x, y

visited = dict()
visited[(xs, ys)] = 0
to_visit = list()

# Initial to visit
for dx, dy in u.ortho_neighbours:
    xp, yp = xs+dx, ys+dy

    if 0 <= xp < X and 0 <= yp < Y:
        if (-dx, -dy) in pipes[matrix[yp][xp]]:
            to_visit.append(((xp, yp), 1))

# BFS
while len(to_visit) > 0:
    v, d = to_visit[0]
    to_visit = to_visit[1:]
    xv, yv = v
    visited[(xv, yv)] = d

    for dx, dy in pipes[matrix[yv][xv]]:
        xp, yp = xv+dx, yv+dy
        if (xp, yp) not in visited:
            to_visit.append(((xp, yp), d+1))

visited_matrix = [['.' for _ in range(0, X)] for _ in range(0, Y)]  # For a beautiful picture

res = 0
for v, d in visited.items():
    x, y = v
    visited_matrix[y][x] = matrix[y][x]
    res = max(res, d)

# for l in visited_matrix:
    # print(' '.join(map(str, l)))

print(res)


# PART 2
path = [(xs, ys)]
visited = set()
visited.add((xs, ys))
to_visit = None

# Initial to visit
for dx, dy in u.ortho_neighbours:
    xp, yp = xs+dx, ys+dy

    if 0 <= xp < X and 0 <= yp < Y:
        if (-dx, -dy) in pipes[matrix[yp][xp]]:
            if to_visit is None:
                to_visit = (xp, yp)

# BFS to find the path
while to_visit is not None:
    path.append(to_visit)
    visited.add(to_visit)
    xv, yv = to_visit
    to_visit = None

    for dx, dy in pipes[visited_matrix[yv][xv]]:
        xp, yp = xv+dx, yv+dy
        if (xp, yp) not in visited:
            to_visit = (xp, yp)

# Finding connex components
to_classify = set()
for x in range(0, X):
    for y in range(0, Y):
        if (x, y) not in visited:
            to_classify.add((x, y))

components = []

while len(to_classify) > 0:
    x0, y0 = to_classify.pop()

    component = set()
    to_visit = set()
    to_visit.add((x0, y0))
    while len(to_visit) > 0:
        x, y = to_visit.pop()
        component.add((x, y))

        for dx, dy in u.ortho_neighbours:
            if (x+dx, y+dy) in to_classify:
                to_visit.add((x+dx, y+dy))
                to_classify.remove((x+dx, y+dy))

    components.append(component)

# Nice viz of connext components
# for i, c in enumerate(components):
    # for x, y in c:
        # visited_matrix[y][x] = i
# for l in visited_matrix:
    # print(' '.join(map(str, l)))

# Would compute faster to first simplify the path i.e. only keep turning segments but I'm lazy
path.append(path[0])
xo, yo = -9999999, -9999999

res = 0
for component in components:
    xm, ym = component.pop()
    component.add((xm, ym))

    inside = False
    for a, b in u.pairwise(path):
        xa, ya = a
        xb, yb = b

        mo = (ym - yo) / (xm - xo)

        if ya == yb:
            y = ya
            x = xo + (ya - yo) / mo
        else:  # xa == xb
            x = xa
            y = yo + mo * (xa - xo)

        ps1 = (xa - x) * (xb - x) + (ya - y) * (yb - y)
        ps2 = (xo - x) * (xm - x) + (yo - y) * (ym - y)
        if ps1 < 0 and ps2 < 0:
            inside = not inside

    if inside:
        res += len(component)

    # for x, y in component:
        # if inside:
            # visited_matrix[y][x] = 'I'
        # else:
            # visited_matrix[y][x] = 'O'

# for l in visited_matrix:
    # print(' '.join(map(str, l)))

print(res)





