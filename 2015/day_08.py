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
diff = 0
for l in lines:
    diff += 2

    i = 1
    while i < len(l)-1:
        if l[i] == '\\':
            if l[i+1] == 'x':
                i += 4
                diff += 3
                continue
            else:
                i += 2
                diff += 1
                continue

        i += 1
        continue

print(diff)


# PART 2
diff = 0
for l in lines:
    diff += 2

    for c in l:
        if c in ['"', '\\']:
            diff += 1

print(diff)




