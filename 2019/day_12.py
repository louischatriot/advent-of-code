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
i_xes, i_yes, i_zes = [], [], []
for l in lines:
    x, y, z = l[1:-1].split(', ')
    x, y, z = x[2:], y[2:], z[2:]
    x, y, z = int(x), int(y), int(z)

    i_xes.append([x, 0])
    i_yes.append([y, 0])
    i_zes.append([z, 0])

xes = [[xe[0], xe[1]] for xe in i_xes]
yes = [[ye[0], ye[1]] for ye in i_yes]
zes = [[ze[0], ze[1]] for ze in i_zes]


# Calculate axes separately
def simulate_one_round_one_axis(xes):
    # Gravity
    for m1, m2 in itertools.combinations(xes, 2):
        x1, vx1 = m1
        x2, vx2 = m2

        if x1 < x2:
            vx1 += 1
            vx2 -= 1
        elif x1 > x2:
            vx1 -= 1
            vx2 += 1

        m1[1] = vx1
        m2[1] = vx2

    # Position
    for m in xes:
        x, vx = m
        m[0] = x+vx


R = 1000

for r in range(0, R):
    simulate_one_round_one_axis(xes)
    simulate_one_round_one_axis(yes)
    simulate_one_round_one_axis(zes)

res = 0
for xe, ye, ze in zip(xes, yes, zes):
    x, vx = xe
    y, vy = ye
    z, vz = ze
    res += (abs(x) + abs(y) + abs(z)) * (abs(vx) + abs(vy) + abs(vz))

print(res)


# PART 2
xes = [[xe[0], xe[1]] for xe in i_xes]
yes = [[ye[0], ye[1]] for ye in i_yes]
zes = [[ze[0], ze[1]] for ze in i_zes]

x = 1
simulate_one_round_one_axis(xes)
while True:
    if all(xe1[0] == xe2[0] and xe1[1] == xe2[1] for xe1, xe2 in zip(xes, i_xes)):
        break
    simulate_one_round_one_axis(xes)
    x += 1

y = 1
simulate_one_round_one_axis(yes)
while True:
    if all(ye1[0] == ye2[0] and ye1[1] == ye2[1] for ye1, ye2 in zip(yes, i_yes)):
        break
    simulate_one_round_one_axis(yes)
    y += 1

z = 1
simulate_one_round_one_axis(zes)
while True:
    if all(ze1[0] == ze2[0] and ze1[1] == ze2[1] for ze1, ze2 in zip(zes, i_zes)):
        break
    simulate_one_round_one_axis(zes)
    z += 1

res = u.lcm(x, y)
res = u.lcm(res, z)

print(res)









