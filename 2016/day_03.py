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
    a, b, c = map(int, line.split())
    if max(a, b, c) < a + b + c - max(a, b, c):
        res += 1

print(res)


# PART 2
thelist = iter(lines)
res = 0

while True:
    data = []
    data.append(next(thelist, None))
    data.append(next(thelist, None))
    data.append(next(thelist, None))

    if data[0] is None:
        break

    data = list(map(lambda line: list(map(int, line.split())) , data))

    for j in range(3):
        a, b, c = data[0][j], data[1][j], data[2][j]
        if max(a, b, c) < a + b + c - max(a, b, c):
            res += 1

print(res)


