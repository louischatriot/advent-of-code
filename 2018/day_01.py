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
    res += int(line)

print(res)


# PART 2
res = 0
seen = set()
seen.add(res)
for _ in range(u.BIG):
    for line in lines:
        res += int(line)

        if res in seen:
            print(res)
            sys.exit(0)
        else:
            seen.add(res)



