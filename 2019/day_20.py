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

matrix = [[c for c in l] for l in lines]

# Padding
J = max(len(l) for l in matrix)
for l in matrix:
    for _ in range(len(l), J):
        l.append(' ')

matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(J)]

for i, __l in enumerate(matrix):
    l = ''.join(__l)

    for m in left.finditer(l):
        add_portal(portals, m.group()[0:2], m.start() + 2, i)

    for m in right.finditer(l):
        add_portal(portals, m.group()[1:], m.start(), i)

matrix = [[c for c in l] for l in lines]

coord_to_portal = dict()
for k, v in portals.items():
    coord_to_portal[v] = k


def next_portals(portals, matrix, start):
    i, j = portals[start]

    todo = [(i, j, 0)]
    done = set()

    while len(todo) > 0:



