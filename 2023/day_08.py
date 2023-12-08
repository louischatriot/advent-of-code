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
instructions = lines[0]

nodes = set()
inst = defaultdict(lambda: dict())

for l in lines[2:]:
    node, nexts = l.split(' = ')
    left, right = nexts[1:-1].split(', ')

    nodes.add(node)
    inst[node]['L'] = left
    inst[node]['R'] = right

start_node = 'AAA'
end_node = 'ZZZ'

current = start_node
res = 0
idx = 0
while current != end_node:
    current = inst[current][instructions[idx]]
    res += 1
    idx = (idx + 1) % len(instructions)

print(res)


# PART 2
start_nodes = list(filter(lambda x: x[-1] == 'A', nodes))
zs = defaultdict(lambda: [])

for start_node in start_nodes:
    current = start_node
    visited_zs = set()
    steps = 0

    while current not in visited_zs:
        if current[-1] == 'Z':
            zs[start_node].append((current, steps))
            visited_zs.add(current)

        current = inst[current][instructions[steps % len(instructions)]]
        steps += 1

    zs[start_node].append((current, steps))

# We are actually in a very specific case where all ghosts loop on a single node with starting position of 0
# So let's take a big fat shortcut
vals = []
for node in zs:
    vals.append(zs[node][0][1])

g = vals[0] * vals[1] // math.gcd(vals[0], vals[1])
for v in vals[2:]:
    g = g * v // math.gcd(g, v)

print(g)


# Ha ha ha it was worth a try
"""
currents = list(filter(lambda x: x[-1] == 'A', nodes))
res = 0
idx = 0
while not all(c[-1] == 'Z' for c in currents):
    new_currents = []
    for c in currents:
        cc = inst[c][instructions[idx]]
        new_currents.append(cc)

    currents = new_currents
    res += 1
    idx = (idx + 1) % len(instructions)

print(res)
"""



