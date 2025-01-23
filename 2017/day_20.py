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
    lines = [line.rstrip() for line in file]


# PART 1
particles = list()

for pn, line in enumerate(lines):
    p, v, a = line.split(', ')
    p = list(map(int, p[3:-1].split(',')))
    v = list(map(int, v[3:-1].split(',')))
    a = list(map(int, a[3:-1].split(',')))
    particles.append((sum(map(abs,a)), sum(map(abs, v)), sum(map(abs, p)), pn, p, v, a))

particles = sorted(particles)
print(particles[0][3])


# PART 2
particles = list()

for pn, line in enumerate(lines):
    p, v, a = line.split(', ')
    p = list(map(int, p[3:-1].split(',')))
    v = list(map(int, v[3:-1].split(',')))
    a = list(map(int, a[3:-1].split(',')))
    particles.append([pn, p, v, a])

T = 1000  # Found empirically :)

for _ in range(T):
    pos = defaultdict(lambda: list())

    for part in particles:
        pn, p, v, a = part
        v[0], v[1], v[2] = v[0] + a[0], v[1] + a[1], v[2] + a[2]
        p[0], p[1], p[2] = v[0] + p[0], v[1] + p[1], v[2] + p[2]

        pos[tuple(p)].append(pn)

    for _, pns in pos.items():
        if len(pns) > 1:
            particles = [p for p in particles if p[0] not in pns]

print(len(particles))


