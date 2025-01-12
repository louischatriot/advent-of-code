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
programs = dict()
nexts = defaultdict(lambda: list())
nonroot = set()
for line in lines:
    i = line.index('(')
    j = line.index(')')
    program = line[0:i-1]
    weight = int(line[i+1:j])
    programs[program] = weight

    if '->' in line:
        parent, children = line.split(' -> ')
        children = children.split(', ')
        for child in children:
            nonroot.add(child)
            nexts[program].append(child)

root = set(programs.keys()).difference(nonroot)
root = root.pop()
print(root)


# PART 2
# Inefficient to start from the root (same calculation done multiple times) but easier to code
import statistics

def total_weight(node):
    to_explore = deque()
    to_explore.append(node)
    res = 0
    while to_explore:
        node = to_explore.popleft()
        res += programs[node]
        for child in nexts[node]:
            to_explore.append(child)

    return res

to_check = root
while True:
    weights = [total_weight(child) for child in nexts[to_check]]
    if len(weights) == 2 and weights[0] != weights[1]:
        raise ValueError("Incompatible with problem statement")

    mode = statistics.mode(weights)

    if mode * len(weights) == sum(weights):
        print("Culprit:", to_check, programs[to_check] + delta)
        break

    for i in range(len(weights)):
        if weights[i] != mode:
            break

    delta = mode - weights[i]
    to_check = nexts[to_check][i]








