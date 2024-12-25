import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import collections
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
computers = set()
links = defaultdict(lambda: set())

for line in lines:
    a, b = line.split('-')
    computers.add(a)
    computers.add(b)

    links[a].add(b)
    links[b].add(a)


# Finding trios ; not efficient but ok for this exercise I guess
trios = set()
for comp1, links1 in links.items():
    for comp2 in links1:
        for comp3 in computers:
            if comp3 in links[comp1] and comp3 in links[comp2]:
                trios.add(tuple(sorted([comp1, comp2, comp3])))

res = 0
for trio in trios:
    if any(c[0] == 't' for c in trio):
        res += 1

print(res)


# PART 2
def get_full_component(computer):
    component = set()
    component.add(computer)

    for ncomp in  computers:
        if all(ncomp in links[c] for c in component):
            component.add(ncomp)

    return component

visited = set()
best = set()

for comp in computers:
    if comp in visited:
        continue

    component = get_full_component(comp)
    if len(component) > len(best):
        best = component

    visited = visited.union(component)

res = ','.join(sorted(list(best)))
print(res)






