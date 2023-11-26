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
xa, ya = lines[0][15:].split(', y=')
xm, xM = xa.split('..')
ym, yM = ya.split('..')
xm, xM, ym, yM = int(xm), int(xM), int(ym), int(yM)

vx0_min = math.floor((2 * xm) ** .5 - 1)  # Should be ceil but let's add one case to be safe oO
vx0_max = xM

possibles_times = set()
min_t_all_ok = None  # If we can hit the target on the x axis for at least one vx0, at some point for all times we can find a vx0 that hits the target on the x axis

all_possible_times = defaultdict(lambda: [])
all_min_t_all_ok = defaultdict(lambda: 999999999)


for vx0 in range(vx0_min, vx0_max+1):
    x_pos = 0
    possibles_times.add(0)

    for t in range(0, vx0):
        x_pos += (vx0 - t)

        if xm <= x_pos <= xM:
            possibles_times.add(t)

            all_possible_times[t].append(vx0)


    if xm <= x_pos <= xM:
        if min_t_all_ok is None:
            min_t_all_ok = t+1
        else:
            min_t_all_ok = min(min_t_all_ok, t+1)

        all_min_t_all_ok[vx0] = min(all_min_t_all_ok[vx0], t+1)

# Assuming ym and yM negative
def find_best_vy0():
    for vy0 in range(-ym, -1, -1):
        t = 2 * vy0 + 1  # That's when the probe is back at y=0 with y velocity -(vy0+1)
        y = 0  # Simulating the trajectory (could go algebraic but lazy and should be fast enough)
        vy = -vy0 - 1

        while y >= ym:
            if ym <= y <= yM:
                if t in possibles_times or t >= min_t_all_ok:
                    return vy0

            y += vy
            vy -= 1

vy0 = find_best_vy0()
print(vy0 * (vy0 + 1) // 2)


# PART 2
# This is freakin ugly but not interesting challenge, leaving it at that
def find_all_vy0():
    pairs = set()

    for vy0 in range(-ym, -999, -1):
        for vx0 in range(vx0_min, vx0_max+1):


            x, y = 0, 0
            vx, vy = vx0, vy0

            ok = False

            while x <= xM and y >= ym:
                if xm <= x <= xM and ym <= y <= yM:
                    ok = True
                    break

                x += vx
                y += vy
                if vx > 0:
                    vx -= 1
                vy -= 1

            if ok:
                pairs.add((vx0, vy0))

    print(len(pairs))
    1/0


    for vy0 in range(-ym, -1, -1):
        t = 2 * vy0 + 1  # That's when the probe is back at y=0 with y velocity -(vy0+1)
        y = 0  # Simulating the trajectory (could go algebraic but lazy and should be fast enough)
        vy = -vy0 - 1

        while y >= ym:
            if ym <= y <= yM:
                if t in possibles_times or t >= min_t_all_ok:
                    for vx0 in all_possible_times[t]:
                        pairs.add((vx0, vy0))

                    for vx0 in range(vx0_min, vx0_max+1):
                        if all_min_t_all_ok[vx0] <= t:
                            pairs.add((vx0, vy0))

            y += vy
            vy -= 1

    print(len(pairs))


find_all_vy0()



