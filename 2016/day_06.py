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


# PART 1 & 2
C = len(lines[0])
cols = [defaultdict(lambda: 0) for _ in range(C)]

for line in lines:
    for i, c in enumerate(line):
        cols[i][c] += 1

message = ''
for d in cols:
    l = [(v, k) for k, v in d.items()]
    _, c = sorted(l)[0]   # -1 for part 1, 0 for part 2
    message += c

print(message)


