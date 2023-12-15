import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import numpy as np

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
def get_hash(s):
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res

res = 0
for s in lines[0].split(','):
    res += get_hash(s)

print(res)


# PART 2 - super not optimized
boxes = [[] for _ in range(0, 256)]
for inst in lines[0].split(','):
    if inst[-1] == '-':
        label = inst[0:-1]
        box = get_hash(label)
        boxes[box] = [lens for lens in boxes[box] if lens[0] != label]

    else:
        label, focal = inst.split('=')
        focal = int(focal)
        box = get_hash(label)

        new_contents = []
        replaced = False
        for lab, foc in boxes[box]:
            if lab != label:
                new_contents.append((lab, foc))
            else:
                new_contents.append((label, focal))
                replaced = True

        if not replaced:
            new_contents.append((label, focal))

        boxes[box] = new_contents

res = 0
for box, contents in enumerate(boxes):
    for idx, c in enumerate(contents):
        res += (box+1) * (idx+1) * c[1]

print(res)






