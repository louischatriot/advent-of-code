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
serial = int(lines[0])

N = 300
cells = dict()
for x, y in itertools.product(range(1, N+1), repeat = 2):
    p = x + 10
    p *= y
    p += serial
    p *= (x + 10)
    p = p // 100
    p = p % 10
    p -= 5

    cells[(x, y)] = p


# Partial sums would be much faster
best = -float('inf')
for x0, y0 in itertools.product(range(1, N-1), repeat = 2):
    candidate = sum(cells[(x0+x, y0+y)] for x, y in itertools.product(range(0, 3), repeat=2))
    best = max(best, candidate)


for x0, y0 in itertools.product(range(1, N-1), repeat = 2):
    candidate = sum(cells[(x0+x, y0+y)] for x, y in itertools.product(range(0, 3), repeat=2))
    if candidate == best:
        print(','.join([str(x0), str(y0)]))


# PART 2
best = -float('inf')
candidates = dict()
for size in range(1, 20):  # No need to go too far!
    for x0, y0 in itertools.product(range(1, N+2-size), repeat=2):
        candidate = sum(cells[(x0+x, y0+y)] for x, y in itertools.product(range(0, size), repeat=2))
        key = f"{x0},{y0},{size}"
        candidates[key] = candidate
        best = max(best, candidate)

print("Best:", best)

for k, v in candidates.items():
    if v == best:
        print(k)


