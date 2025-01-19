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
am, bm = 16807, 48271
m = 2147483647  # Prime

a, b = lines[0].split(',')
a, b = int(a), int(b)

R = 40000000
res = 0
CUT = 2 ** 16
for _ in range(R):
    a, b = (a * am) % m, (b * bm) % m
    if (a - b) % CUT == 0:
        res += 1

print(res)


# PART 2
a, b = lines[0].split(',')
a, b = int(a), int(b)

def generate_from(current, mult, mod, acceptable):
    while True:
        current = (current * mult) % mod
        if current % acceptable == 0:
            yield current

res = 0
turns = 5000000
for a, b in zip(generate_from(a, am, m, 4), generate_from(b, bm, m, 8)):
    if a % CUT == b % CUT:
        res += 1

    turns -= 1
    if turns == 0:
        break

print(res)




