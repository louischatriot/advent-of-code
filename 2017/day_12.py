import sys
import re
import u as u
from collections import defaultdict, deque
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
edges = dict()
nodes = set()
for line in lines:
    s, es = line.split(' <-> ')
    edges[s] = es.split(', ')
    nodes.add(s)


def get_group(start):
    explored = set()
    to_explore = deque()
    to_explore.append(start)
    while to_explore:
        node = to_explore.popleft()
        if node in explored:
            continue
        else:
            explored.add(node)

        for e in edges[node]:
            to_explore.append(e)

    return explored

group = get_group('0')
print(len(group))


# PART 2
explored = set()
res = 0
for node in nodes:
    if node in explored:
        continue

    res += 1
    group = get_group(node)
    explored = explored.union(group)

print(res)

