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
places = set()
for l in lines:
    cts, _ = l.split(' = ')
    for place in cts.split(' to '):
        places.add(place)

places = list(places)
places_to_idx = {p: i for i, p in enumerate(places)}
N = len(places)

BIG = 9999999999
distances = [[BIG for _ in range(N)] for _ in range(N)]
for l in lines:
    cts, d = l.split(' = ')
    d = int(d)
    a, b = cts.split(' to ')
    distances[places_to_idx[a]][places_to_idx[b]] = d
    distances[places_to_idx[b]][places_to_idx[a]] = d

# Bourrin approach works because small dataset
best = BIG
for perm in itertools.permutations(list(range(N))):
    best = min(best, sum(distances[a][b] for a, b in u.pairwise(perm)))

print(best)


"""
# This does not work as it does not follow the graph (shame on me)
def shortest_path(distances, visited, current, d):
    if len(visited) == N:
        return d

    res = BIG

    for p in range(N):
        if p not in visited:
            __visited = visited.union({p})
            res = min(res, shortest_path(distances, __visited, p, d + distances[current][p]))

    return res

res = shortest_path(distances, {0}, 0, 0)
print(res)
"""


# PART 2
NEG_BIG = -BIG
distances = [[NEG_BIG for _ in range(N)] for _ in range(N)]
for l in lines:
    cts, d = l.split(' = ')
    d = int(d)
    a, b = cts.split(' to ')
    distances[places_to_idx[a]][places_to_idx[b]] = d
    distances[places_to_idx[b]][places_to_idx[a]] = d

# Bourrin approach works because small dataset
best = NEG_BIG
for perm in itertools.permutations(list(range(N))):
    best = max(best, sum(distances[a][b] for a, b in u.pairwise(perm)))

print(best)
