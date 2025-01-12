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
    words = line.split()
    if len(words) == len(set(words)):
        res += 1

print(res)


# PART 2
res = 0
for line in lines:
    words = line.split()
    if all(sorted(a) != sorted(b) for a, b in itertools.combinations(words, 2)):
        res += 1

print(res)





