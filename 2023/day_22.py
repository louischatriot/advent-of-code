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
# Let's go bourrin
def node_name(node):
    a, b = node
    return ','.join(map(str, a)) + '~' + ','.join(map(str, b))

def parse_node_name(name):
    a, b = name.split('~')
    a, b = a.split(','), b.split(',')
    a, b = tuple(map(int, a)), tuple(map(int, b))
    return (a, b)

def brick_surface_iterator(brick):
    a, b = brick
    if a[0] == b[0]:
        for y in range(a[1], b[1]+1):
            yield (a[0], y)

    elif a[1] == b[1]:
        for x in range(a[0], b[0]+1):
            yield (x, a[1])

    else:
        raise ValueError("Bricks should be one dimensional")


bricks = [parse_node_name(l) for l in lines]

# Determining order in which bricks can fall
nodes = { node_name(b) for b in bricks }
edges = defaultdict(lambda: set())

for b1, b2 in itertools.product(bricks, repeat=2):
    if b1 == b2:
        continue

    if b1[1][2] < b2[0][2]:  # Brick 1 below brick 2
        mx, Mx = max(b1[0][0], b2[0][0]), min(b1[1][0], b2[1][0])
        my, My = max(b1[0][1], b2[0][1]), min(b1[1][1], b2[1][1])

        if mx <= Mx and my <= My:  # Brick 1 under brick 2
            edges[node_name(b1)].add(node_name(b2))

order = u.topological_sort(nodes, edges)

FLOOR = '<floor>'
heights = defaultdict(lambda: (FLOOR, 0))
supported_by = defaultdict(lambda: set())
supporting = defaultdict(lambda: set())

for idx, brick_name in enumerate(order):
    zmin = 1
    brick = parse_node_name(brick_name)

    # First pass = finding the min
    for x, y in brick_surface_iterator(brick):
        supporter, height = heights[(x, y)]
        zmin = max(zmin, height)

    # Second pass = finding the supporters
    for x, y in brick_surface_iterator(brick):
        supporter, height = heights[(x, y)]
        if height == zmin and supporter != FLOOR:
            supported_by[brick_name].add(supporter)
            supporting[supporter].add(brick_name)

    # Third pass = updating the 3d map
    if brick[0][2] != brick[1][2]:  # Vertical brick
        heights[(brick[0][0], brick[0][1])] = (brick_name, zmin + brick[1][2] - brick[0][2] + 1)

    else:
        for x, y in brick_surface_iterator(brick):
            heights[(x, y)] = (brick_name, zmin + 1)

destroyable = set()
for brick, supporters in supported_by.items():
    if len(supporters) == 1:
        supporter = supporters.pop()
        destroyable.add(supporter)
        supporters.add(supporter)  # Repairing

res = len(bricks) - len(destroyable)
print(res)


# PART 2
def get_destroyed(supporting, supported_by, brick):
    supporting = {k: {b for b in v} for k, v in supporting.items()}
    supported_by = {k: {b for b in v} for k, v in supported_by.items()}

    to_destroy = [brick]
    destroyed = set()

    while len(to_destroy) > 0:
        brick, to_destroy = to_destroy[0], to_destroy[1:]

        if brick in destroyed:
            continue

        destroyed.add(brick)

        if brick in supporting:
            for b in supporting[brick]:
                supported_by[b].remove(brick)
                if len(supported_by[b]) == 0:
                    to_destroy.append(b)

    return len(destroyed) - 1


res = 0
for brick in bricks:
    res += get_destroyed(supporting, supported_by, node_name(brick))

print(res)






