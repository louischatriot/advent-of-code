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
def check_string(s):
    return any(s[i] != s[i+1] and s[i] == s[i+3] and s[i+1] == s[i+2] for i in range(len(s) - 3))

def parse(line):
    insb, outsb = [], ['']
    init = False

    for c in line:
        if c == '[':
            init = True
            insb.append('')
            continue
        elif c == ']':
            init = False
            outsb.append('')
            continue

        if init:
            insb[-1] += c
        else:
            outsb[-1] += c

    if outsb[-1] == '':
        outsb = outsb[0:-1]

    return (insb, outsb)

res = 0
for line in lines:
    insb, outsb = parse(line)

    if any(check_string(s) for s in outsb) and not any(check_string(s) for s in insb):
        res += 1

print(res)


# PART 2
def extract(s):
    return set(s[i:i+3] for i in range(len(s)-2) if s[i] == s[i+2] and s[i] != s[i+1])

res = 0
for line in lines:
    insb, outsb = parse(line)

    babin, babout = set(), set()
    for s in insb:
        babin = babin.union(extract(s))
    for s in outsb:
        babout = babout.union(extract(s))

    babout = set(f"{s[1]}{s[0]}{s[1]}" for s in babout)
    if len(babin.intersection(babout)) > 0:
        res += 1

print(res)


