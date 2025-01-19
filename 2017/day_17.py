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
s = int(lines[0])

l = [0]
current = 0
R = 2017

for r in range(1, R+1):
    current = (current + s) % len(l)
    l = l[0:current+1] + [r] + l[current+1:]
    current += 1

res = l[current + 1]
print(res)


# PART 2
R = 50000000
current = 0
v = 0
for r in range(1, R+1):
    current = (current + s) % r + 1
    if current == 1:
        v = r

print(v)

