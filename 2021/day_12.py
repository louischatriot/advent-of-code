import sys
import re
import u as u
from collections import defaultdict
import math

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
edges = defaultdict(lambda: [])
for l in lines:
    a, b = l.split('-')
    edges[a].append(b)
    edges[b].append(a)

paths = [['start']]

# Super inefficient
while True:
    new_paths = []

    for path in paths:
        if path[-1] == 'end':
            new_paths.append(path)
            continue

        for b in edges[path[-1]]:
            if not u.is_all_lowercase(b) or b not in path:
                new_paths.append(path + [b])

    # Oh god
    if len(new_paths) == len(paths):
        break

    paths = new_paths

print(len(paths))


# PART 2
def bad_path(p):
    vs = defaultdict(lambda: 0)
    for s in p:
        if u.is_all_lowercase(s):
            vs[s] += 1

    res = 0
    for k, v in vs.items():
        if v >= 3:
            return True

        if v == 2:
            if k in ['start', 'end']:
                return True
            else:
                res += 1

    return (res > 1)

paths = [['start']]

# Super inefficient
while True:
    new_paths = []

    for path in paths:
        if path[-1] == 'end':
            new_paths.append(path)
            continue

        for b in edges[path[-1]]:
            if not u.is_all_lowercase(b) or not bad_path(path + [b]):
                new_paths.append(path + [b])

    # Oh god
    if len(new_paths) == len(paths):
        break

    paths = new_paths

print(len(paths))





