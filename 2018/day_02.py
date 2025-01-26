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
two, three = 0, 0
for line in lines:
    counts = defaultdict(lambda: 0)
    for c in line:
        counts[c] += 1

    for c, v in counts.items():
        if v == 2:
            two += 1
            break

    for c, v in counts.items():
        if v == 3:
            three += 1
            break

print(two * three)


# PART 2
for box1, box2 in itertools.combinations(lines, 2):
    errors = 0
    for i, cs in enumerate(zip(box1, box2)):  # Same length
        c1, c2 = cs
        if c1 != c2:
            errors += 1
            idx = i

    if errors == 1:
        res = box1[0:idx] + box1[idx+1:]
        print(res)
        break


