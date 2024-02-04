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
for c in lines[0]:
    if c == '(':
        res += 1
    elif c == ')':
        res -= 1
    else:
        raise ValueError()

print(res)


# PART 1
res = 0
for i, c in enumerate(lines[0]):
    if c == '(':
        res += 1
    elif c == ')':
        res -= 1
    else:
        raise ValueError()

    if res == -1:
        print(i+1)
        break


