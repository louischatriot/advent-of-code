import sys
import re
import u as u
from collections import defaultdict
import math
import itertools

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
portals = dict()

def add_portal(portals, name, i, j):
    key = f"{name}-1"
    if key in portals:
        key = f"{name}-2"

    portals[key] = (i, j)



left = re.compile('[A-Z]{2}\.')
right = re.compile('\.[A-Z]{2}')

for i, l in enumerate(lines):
    for m in left.finditer(l):
        add_portal(portals, m.group()[0:2], i, m.start() + 2)

    for m in right.finditer(l):
        add_portal(portals, m.group()[1:], i, m.start())

print(portals)


