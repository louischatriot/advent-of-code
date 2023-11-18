import sys
import re
import u as u
from collections import defaultdict
import math

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
def get_masks(mask):
    mask0 = 2**37 - 1
    mask1 = 0

    for idx, c in enumerate(reversed(mask)):
        if c == '1':
            mask1 += 2**idx

        if c == '0':
            mask0 -= 2**idx

    return mask0, mask1

memory = dict()

for l in lines:
    if l[0:4] == 'mask':
        mask0, mask1 = get_masks(l[7:])
        continue

    m, v = l.split(' = ')
    v = int(v)
    v = (v & mask0) | mask1
    m = int(m[4:-1])
    memory[m] = v

res = 0
for k, v in memory.items():
    res += v

print(res)


# PART 2
def get_masks_2(mask):
    mask0 = 2**37 - 1
    mask1 = 0
    maskX = []

    for idx, c in enumerate(reversed(mask)):
        if c == '1':
            mask1 += 2**idx

        if c == 'X':
            mask0 -= 2**idx
            maskX.append(2**idx)

    return mask0, mask1, u.all_partial_sums(maskX)

memory = dict()

for l in lines:
    if l[0:4] == 'mask':
        mask0, mask1, maskX = get_masks_2(l[7:])
        continue

    m, v = l.split(' = ')
    m = int(m[4:-1])
    v = int(v)
    m = (m & mask0) | mask1
    for mm in maskX:
        memory[m + mm] = v

res = 0
for k, v in memory.items():
    res += v

print(res)

