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
l, r = list(), list()
for line in lines:
    a, b = line.split()
    l.append(int(a))
    r.append(int(b))

l = sorted(l)
r = sorted(r)

res = sum(abs(a - b) for a, b in zip(l, r))
print(res)


# PART 2
res = sum(a * r.count(a) for a in l)
print(res)



