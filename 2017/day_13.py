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
ranges = dict()

for line in lines:
    d, r = line.split(': ')
    d, r = int(d), int(r)
    ranges[d] = 2 * r - 2

res = sum(p * (ranges[p] + 2) // 2 for p in ranges if p % ranges[p] == 0)
print(res)


# PART 2
delay = 0
while True:
    if not any((delay + p) % ranges[p] == 0 for p in ranges):
        print(delay)
        break

    delay += 1

