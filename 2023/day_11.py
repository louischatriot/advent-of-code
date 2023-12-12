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
I, J = len(lines), len(lines[0])
galaxies = set()
taken_is = set()
taken_js = set()
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == '#':
            galaxies.add((i, j))
            taken_is.add(i)
            taken_js.add(j)

empty_is = list()
for i in range(I):
    if i not in taken_is:
        empty_is.append(i)

empty_js = list()
for j in range(J):
    if j not in taken_js:
        empty_js.append(j)

# Could be linear in axis length but oh well
factor = 1000000  # Modify here between parts 1 and 2
offsets_is = list()
for i in range(I):
    offsets_is.append((factor - 1) * sum(1 if ei < i else 0 for ei in empty_is))

offsets_js = list()
for j in range(J):
    offsets_js.append((factor - 1) * sum(1 if ej < j else 0 for ej in empty_js))


res = 0
for g1, g2 in itertools.combinations(galaxies, 2):
    i1, j1 = g1
    i2, j2 = g2

    i1 += offsets_is[i1]
    j1 += offsets_js[j1]
    i2 += offsets_is[i2]
    j2 += offsets_js[j2]

    res += abs(i1 - i2) + abs(j1 - j2)

print(res)



