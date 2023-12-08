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
asteroids = set()
for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c == '#':
            asteroids.add((x, y))

def visible_from(ast, other):
    xa, ya = ast
    xo, yo = other

    if xa == xo:
        if all((xa, y) not in asteroids for y in range(min(ya, yo)+1, max(ya, yo))):
            return True

    elif ya == yo:
        if all((x, ya) not in asteroids for x in range(min(xa, xo)+1, max(xa, xo))):
            return True

    else:  # Not horizontal, not vertical
        if xa > xo:
            xa, ya, xo, yo = xo, yo, xa, ya

        bad = False
        for x in range(xa+1, xo):
            yi = ya + (x - xa) * (yo - ya) / (xo - xa)
            if abs(round(yi) - yi) < epsilon:  # Integer coordinates (better way would be to replace / by // above and do a cross product check)
                if (x, yi) in asteroids:
                    bad = True

        if not bad:
            return True

    return False


epsilon = 0.0000000001
visibles = defaultdict(lambda: 0)
for ast in asteroids:
    for other in asteroids:
        if ast == other:
            continue

        if visible_from(ast, other):
            visibles[ast] += 1


best = None
most_visible = -1
for k, v in visibles.items():
    if v > most_visible:
        most_visible = v
        best = k

print(best)
print(most_visible)


# PART 2
def get_theta(ast):
    xb, yb = ast
    x, y = xb, -yb

    if x == 0 and y > 0:
        theta = 90

    elif x == 0 and y < 0:
        theta = 270

    elif x > 0:
        theta = math.atan(y / x) * 180 / math.pi
        if theta < 0:
            theta += 360

    elif x < 0:
        theta = 180 - math.atan(-y / x) * 180 / math.pi

    theta = 90 - theta
    if theta < 0:
        theta += 360

    return theta

vectors = list()
xbest, ybest = best
for x, y in asteroids:
    if x != xbest or y != ybest:
        vector = (x - xbest, y - ybest)
        vectors.append(vector)

vectors.sort(key=get_theta)

last_vaporized_theta = None
vaporized = 0
idx = -1
while True:
    idx += 1
    vector = vectors[idx % len(vectors)]

    if vector == -1:
        continue

    if last_vaporized_theta != get_theta(vector):
        vaporized += 1
        if vaporized == 200:
            x, y = vector
            x, y = x + xbest, y + ybest
            print(100 * x + y)
            sys.exit(0)

        last_vaporized_theta = get_theta(vector)
        vectors[idx % len(vectors)] = -1






