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
for line in lines:
    ns = [int(n) for n in line.split()]
    res += max(ns) - min(ns)

print(res)


# PART 2
res = 0
for line in lines:
    ns = [int(n) for n in line.split()]
    for a, b in itertools.combinations(ns, 2):
        m, M = min(a, b), max(a, b)
        if M % m == 0:
            res += M // m

print(res)




