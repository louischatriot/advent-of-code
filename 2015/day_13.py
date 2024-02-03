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
names = set()
for l in lines:
    i0 = l.find(' ')
    names.add(l[0:i0])

names = list(names)
name_to_idx = {n: i for i, n in enumerate(names)}
N = len(names)

happy = [[0 for _ in range(N)] for _ in range(N)]

for l in lines:
    i0 = l.find(' ')
    name = l[0:i0]
    rest = l[i0+7:]

    if rest[0:4] == 'gain':
        sign = 1
    else:
        sign = -1

    rest = rest[5:]
    i0 = rest.find(' ')
    val = int(rest[0:i0])
    rest = rest[i0+36:]
    target = rest[0:-1]

    happy[name_to_idx[name]][name_to_idx[target]] = sign * val

best = -1

for perm in itertools.permutations(list(range(N))):
    score = 0
    for a, b in u.pairwise(perm):
        score += happy[a][b] + happy[b][a]

    score += happy[perm[-1]][perm[0]] + happy[perm[0]][perm[-1]]

    if score > best:
        best = score

print(best)


# PART 2
N += 1

for l in happy:
    l.append(0)

happy.append([0 for _ in range(N)])

best = -1

for perm in itertools.permutations(list(range(N))):
    score = 0
    for a, b in u.pairwise(perm):
        score += happy[a][b] + happy[b][a]

    score += happy[perm[-1]][perm[0]] + happy[perm[0]][perm[-1]]

    if score > best:
        best = score

print(best)





