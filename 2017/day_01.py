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
s = lines[0] + lines[0][0]
res = 0
for a, b in u.pairwise(s):
    if a == b:
        res += int(a)
print(res)


# PART 2
s = lines[0]
res = 0
N = len(s) // 2
for i, a in enumerate(s):
    if s[(i+N) % len(s)] == a:
        res += int(a)
print(res)



