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
bots = list()
for line in lines:
    data = line.split('=<')[1]
    pos, radius = data.split('>, r=')
    x, y, z = pos.split(',')
    x, y, z, r = int(x), int(y), int(z), int(radius)

    bots.append((x, y, z, r))

rb = 0
rw = float('inf')
for x, y, z, r in bots:
    rb = max(rb, r)
    rw = min(rw, r)

botb = None
for bot in bots:
    if bot[3] == rb:
        botb = bot

xb, yb, zb, rb = botb

res = 0
for x, y, z, _ in bots:
    if abs(x - xb) + abs(y - yb) + abs(z - zb) <= rb:
        res += 1

print(res)


# PART 2
def d(bot1, bot2):
    if len(bot1) == 3:
        x1, y1, z1 = bot1
        x2, y2, z2 = bot2
    else:
        x1, y1, z1, r1 = bot1
        x2, y2, z2, r2 = bot2

    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

xm, ym, zm = float('inf'), float('inf'), float('inf')
xM, yM, zM = -float('inf'), -float('inf'), -float('inf')

# Assuming that we don't need to get outside the box laid out by bots
for x, y, z, r in bots:
    xm = min(xm, x)
    ym = min(ym, y)
    zm = min(zm, z)

    xM = max(xM, x)
    yM = max(yM, y)
    zM = max(zM, z)

print(xm, xM, '---', (xM-xm) // 1e6)
print(ym, yM, '---', (yM-ym) // 1e6)
print(zm, zM, '---', (zM-zm) // 1e6)

def clip(xm, xM, res):
    xxm = xm // res
    nxm = xxm * res

    xxM = xM // res
    nxM = xxM * res

    nxm, nxM = int(nxm), int(nxM) + 1  # In case we do not divide region evenly, we don't want to miss a part

    return nxm, nxM

# This code could be factored buy I am lazy, it works and that's already good enough

res = 25000000

nxm, nxM = clip(xm, xM, res)
nym, nyM = clip(ym, yM, res)
nzm, nzM = clip(zm, zM, res)

best = 0
regions = dict()
for xr in range(nxm, nxM+1, res):
    for yr in range(nym, nyM+1, res):
        for zr in range(nzm, nzM+1, res):
            center = (xr + res // 2, yr + res // 2, zr + res // 2)
            score = sum(1 if d(center, (x, y, z)) <= r else 0 for x, y, z, r in bots)
            regions[center] = score
            best = max(best, score)

best_regions = list()
for xr in range(nxm, nxM+1, res):
    for yr in range(nym, nyM+1, res):
        for zr in range(nzm, nzM+1, res):
            center = (xr + res // 2, yr + res // 2, zr + res // 2)

            if regions[center] == best:
                best_regions.append((xr, yr, zr, res))

print("Best for res", res, "---", best, "--- Matching regions: ", len(best_regions))

print(best_regions)

origin = (0, 0, 0, 0)


# Reducing the window size
for res in [2500000, 250000, 25000, 2500, 250, 25, 12]:
    # Find best
    regions = dict()
    best = 0
    for xbr, ybr, zbr, previous_res in best_regions:
        nxm, nxM = clip(xbr, xbr + previous_res - 1, res)
        nym, nyM = clip(ybr, ybr + previous_res - 1, res)
        nzm, nzM = clip(zbr, zbr + previous_res - 1, res)

        for xr in range(nxm, nxM+1, res):
            for yr in range(nym, nyM+1, res):
                for zr in range(nzm, nzM+1, res):
                    center = (xr + res // 2, yr + res // 2, zr + res // 2)
                    score = sum(1 if d(center, (x, y, z)) <= r else 0 for x, y, z, r in bots)
                    regions[center] = score
                    best = max(best, score)

    # Find all new best regions
    new_best_regions = list()
    for xbr, ybr, zbr, previous_res in best_regions:
        nxm, nxM = clip(xbr, xbr + previous_res - 1, res)
        nym, nyM = clip(ybr, ybr + previous_res - 1, res)
        nzm, nzM = clip(zbr, zbr + previous_res - 1, res)

        for xr in range(nxm, nxM+1, res):
            for yr in range(nym, nyM+1, res):
                for zr in range(nzm, nzM+1, res):
                    center = (xr + res // 2, yr + res // 2, zr + res // 2)

                    if regions[center] == best:
                        new_best_regions.append((xr, yr, zr, res))

    best_regions = new_best_regions
    print("Best for res", res, "---", best, "--- Matching regions: ", len(best_regions))

    # Keep the ones closest to the origin, I will need to be lucky
    clipped_regions = list()
    for region in best_regions:
        clipped_regions.append((d(origin, region), region))

    clipped_regions = sorted(clipped_regions)[0:10]

    best_regions = [region for _, region in clipped_regions]

    print(best_regions)



# Final regions of size 12, now cube by cube
regions = dict()
best = 0

for xbr, ybr, zbr, previous_res in best_regions:
    nxm, nxM = xbr, xbr + previous_res
    nym, nyM = ybr, ybr + previous_res
    nzm, nzM = zbr, zbr + previous_res

    for xr in range(nxm, nxM+1):
        for yr in range(nym, nyM+1):
            for zr in range(nzm, nzM+1):
                center = (xr, yr, zr)
                score = sum(1 if d(center, (x, y, z)) <= r else 0 for x, y, z, r in bots)
                regions[center] = score
                best = max(best, score)

    best_regions = list()
    for xr in range(nxm, nxM+1):
        for yr in range(nym, nyM+1):
            for zr in range(nzm, nzM+1):
                center = (xr, yr, zr)

                if regions[center] == best:
                    best_regions.append((d(origin, (xr, yr, zr, 1)), (xr, yr, zr)))



print("==================================================")

best_regions = sorted(best_regions)

print(best_regions[0:10])

print(best_regions[0][0])





