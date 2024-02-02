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
__target_sue = "children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1"
target_sue = dict()
for b in __target_sue.split(', '):
    k, v = b.split(': ')
    v = int(v)
    target_sue[k] = v

sues = dict()
for l in lines:
    i = l.find(':')
    s = l[0:i]
    __t = l[i+2:]
    s = int(s[4:])

    t = dict()
    for b in __t.split(', '):
        k, v = b.split(': ')
        v = int(v)
        t[k] = v

    sues[s] = t

for k, v in sues.items():
    if all(target_sue[kk] == vv for kk, vv in v.items()):
        print(k)


# PART 2
greater = ['cats', 'trees']
fewer = ['pomeranians', 'goldfish']
for sue_number, sue_items in sues.items():
    match = True
    for k, v in sue_items.items():
        if k in greater:
            if v <= target_sue[k]:
                match = False

        elif k in fewer:
            if v >= target_sue[k]:
                match = False

        else:
            if target_sue[k] != v:
                match = False

    if match:
        print(sue_number)
