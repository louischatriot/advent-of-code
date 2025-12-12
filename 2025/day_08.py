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
boxes = list()
for line in lines:
    box = line.split(',')
    box = tuple([int(c) for c in box])
    boxes.append(box)

def d(b1, b2):
    return math.sqrt((b1[0] - b2[0])**2 + (b1[1] - b2[1])**2 + (b1[2] - b2[2])**2)

distances = list()
for b1, b2 in itertools.combinations(boxes, 2):
    distances.append((d(b1, b2), b1, b2))
distances = sorted(distances)

def graph(N):
    edges = defaultdict(lambda: set())
    i = 0
    for d, b1, b2 in distances:
        edges[b1].add(b2)
        edges[b2].add(b1)

        i += 1
        if i >= N:
            break

    components = list()
    done = set()

    for box in boxes:
        if box in done:
            continue

        # BFS
        component = set()
        to_explore = set()
        to_explore.add(box)
        while len(to_explore) > 0:
            current = to_explore.pop()
            if current in component:
                continue

            done.add(current)
            component.add(current)
            to_explore = to_explore.union(edges[current])

        components.append(component)

    return components


N = 10 if is_example else 1000
components = graph(N)
components_sizes = [len(c) for c in components]
components_sizes = sorted(components_sizes)
res = components_sizes[-1] * components_sizes[-2] * components_sizes[-3]
print(res)


# PART 2
# Manual dichotomy too lazy
N = 5943
components = graph(N)
print(len(components))  # Looking for smallest N to get only one component
_, b1, b2 = distances[N-1]
res = b1[0] * b2[0]
print(res)


