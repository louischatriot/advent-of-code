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


# PART 1 & 2
particles_start = list()
for line in lines:
    data = line.split('<')
    pos = data[1].split('>')[0]
    vel = data[2][0:-1]
    x, y = pos.split(',')
    x, y = int(x), int(y)
    vx, vy = vel.split(',')
    vx, vy = int(vx), int(vy)

    particles_start.append((x, y, vx, vy))


def get_box(particles):
    xm, xM, ym, yM = float('inf'), -float('inf'), float('inf'), -float('inf')
    for x, y, _, _ in particles:
        xm = min(xm, x)
        xM = max(xM, x)
        ym = min(ym, y)
        yM = max(yM, y)

    return xm, xM, ym, yM

def print_cloud(particles):
    xm, xM, ym, yM = get_box(particles)

    pos = set()
    for x, y, _, _ in particles:
        pos.add((x, y))

    for y in range(ym, yM+1):
        l = ''.join('#' if (x, y) in pos else '.' for x in range(xm, xM+1))
        print(l)



particles = [[x, y, vx, vy] for x, y, vx, vy in particles_start]
xm, xM, ym, yM = get_box(particles)
D = xM - xm

r = 0

while True:
    for p in particles:
        p[0] += p[2]
        p[1] += p[3]

    xm, xM, ym, yM = get_box(particles)
    if xM - xm > D:
        break
    else:
        D = xM - xm

    r += 1


# Back one step, when we were at the minimum width
for p in particles:
    p[0] -= p[2]
    p[1] -= p[3]


print_cloud(particles)


# PART 2
print(r)


