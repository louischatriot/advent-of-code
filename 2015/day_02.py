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
res = 0
for l in lines:
    a, b, c = l.split('x')
    a, b, c = int(a), int(b), int(c)
    a, b, c = a * b, a * c, b * c
    res += 2 * (a + b + c) + min(a, b, c)

print(res)


# PART 2
res = 0
for l in lines:
    a, b, c = l.split('x')
    a, b, c = int(a), int(b), int(c)
    a, b, c, v = 2 * (a + b), 2 * (a + c), 2 * (b + c), a * b * c
    res += v + min(a, b, c)

print(res)


