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
rules = []
for l in lines:
    if l[0:2] == 'on':
        op = 'on'
        contents = l[3:]
    else:
        op = 'off'
        contents = l[4:]

    x, y, z = contents.split(',')
    x, y, z = x[2:], y[2:], z[2:]
    xm, xM = x.split('..')
    xm, xM = int(xm), int(xM)
    ym, yM = y.split('..')
    ym, yM = int(ym), int(yM)
    zm, zM = z.split('..')
    zm, zM = int(zm), int(zM)

    rules.append((op, (xm, xM, ym, yM, zm, zM)))


cubes = set()
for r in rules:
    op, cube = r
    xm, xM, ym, yM, zm, zM = cube

    xm, ym, zm = max(-50, xm), max(-50, ym), max(-50, zm)
    xM, yM, zM = min(50, xM), min(50, yM), min(50, zM)

    for x in range(xm, xM+1):
        for y in range(ym, yM+1):
            for z in range(zm, zM+1):
                if op == 'on':
                    cubes.add((x, y, z))
                else:
                    if (x, y, z) in cubes:
                        cubes.remove((x, y, z))


print(len(cubes))


# PART 2
def get_intersection(cube1, cube2):
    xm1, xM1, ym1, yM1, zm1, zM1 = cube1
    xm2, xM2, ym2, yM2, zm2, zM2 = cube2

    xm, xM = max(xm1, xm2), min(xM1, xM2)
    ym, yM = max(ym1, ym2), min(yM1, yM2)
    zm, zM = max(zm1, zm2), min(zM1, zM2)

    if xm <= xM and ym <= yM and zm <= zM:
        return (xm, xM, ym, yM, zm, zM)
    else:
        return None


game_is_on = False

pos_cubes = []
neg_cubes = []

for op, cube in rules:
    if op == 'on':
        game_is_on = True

    if not game_is_on:
        continue

    if op == 'on' and len(pos_cubes) == 0:
        pos_cubes.append(cube)
        continue

    if op == 'on':
        new_pos_cubes = []
        new_neg_cubes = []

        new_pos_cubes.append(cube)

        for c in pos_cubes:
            inter = get_intersection(cube, c)
            if inter:
                new_neg_cubes.append(inter)

        for c in neg_cubes:
            inter = get_intersection(cube, c)
            if inter:
                new_pos_cubes.append(inter)

    if op == 'off':
        new_pos_cubes = []
        new_neg_cubes = []

        for c in pos_cubes:
            inter = get_intersection(cube, c)
            if inter:
                new_neg_cubes.append(inter)

        for c in neg_cubes:
            inter = get_intersection(cube, c)
            if inter:
                new_pos_cubes.append(inter)

    pos_cubes += new_pos_cubes
    neg_cubes += new_neg_cubes


res = 0

for cube in pos_cubes:
    xm, xM, ym, yM, zm, zM = cube
    res += (xM - xm + 1) * (yM - ym + 1) * (zM - zm + 1)

for cube in neg_cubes:
    xm, xM, ym, yM, zm, zM = cube
    res -= (xM - xm + 1) * (yM - ym + 1) * (zM - zm + 1)

print(res)




