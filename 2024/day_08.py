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
N, M = len(lines), len(lines[0])
antennas = defaultdict(lambda: [])

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if lines[i][j] != '.':
            antennas[lines[i][j]].append((i, j))

antinodes = set()
for signal, ants in antennas.items():
    for a1, a2 in itertools.combinations(ants, 2):
        x1, y1 = a1
        x2, y2 = a2
        dx, dy = x2 - x1, y2 - y1
        antinodes.add((x1 - dx, y1 - dy))
        antinodes.add((x2 + dx, y2 + dy))

res = sum(1 if 0 <= x < N and 0 <= y < M else 0 for x, y in antinodes)
print(res)


# PART 2
the_max = max(N, M) + 2  # Spoiler alert: it's going to be clean

antinodes = set()
for signal, ants in antennas.items():
    for a1, a2 in itertools.combinations(ants, 2):
        x1, y1 = a1
        x2, y2 = a2
        dx, dy = x2 - x1, y2 - y1

        for n in range(-the_max, the_max):
            antinodes.add((x1 - dx * n, y1 - dy * n))

res = sum(1 if 0 <= x < N and 0 <= y < M else 0 for x, y in antinodes)
print(res)



