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
patterns = []
pattern = []
for l in lines:
    if l == '':
        patterns.append(np.array(pattern))
        pattern = []
    else:
        pattern.append([c for c in l])

if len(pattern) > 0:
    patterns.append(np.array(pattern))


res = 0
reflexions = list()
for id, p in enumerate(patterns):
    N = len(p)
    M = len(p[0, :])

    reflexions.append(None)

    for r in range(1, N):
        if all(np.array_equal(p[r-1-ro, :], p[r+ro, :]) for ro in range(0, min(r, N-r))):
            res += 100 * r
            reflexions[id] = ('row', r)

    for c in range(1, M):
        if all(np.array_equal(p[:, c-1-co], p[:, c+co]) for co in range(0, min(c, M-c))):
            res += c
            reflexions[id] = ('col', c)


print(res)


# PART 2 - Brute forcing
res = 0
for id, p in enumerate(patterns):
    N = len(p)
    M = len(p[0, :])

    for i, j in itertools.product(range(N), range(M)):
        p[i][j] = '.' if p[i][j] == '#' else '#'

        found = False
        for r in range(1, N):
            if all(np.array_equal(p[r-1-ro, :], p[r+ro, :]) for ro in range(0, min(r, N-r))):
                t, v = reflexions[id]
                if t != 'row' or v != r:
                    found = True
                    res += 100 * r

        for c in range(1, M):
            if all(np.array_equal(p[:, c-1-co], p[:, c+co]) for co in range(0, min(c, M-c))):
                t, v = reflexions[id]
                if t != 'col' or v != c:
                    found = True
                    res += c

        if found:
            break
        else:
            p[i][j] = '.' if p[i][j] == '#' else '#'


print(res)




