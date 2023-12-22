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
R = 6 if is_example else 64

matrix = [[c for c in l] for l in lines]
I, J = len(matrix), len(matrix[0])
iz, jz = None, None
for i, j in itertools.product(range(I), range(J)):
    if matrix[i][j] == 'S':
        iz, jz = i, j
        matrix[i][j] = '.'
        break

for l in matrix:
    print(''.join(l))

can_get_to = set()
can_get_to.add((iz, jz))

for r in range(0, R):
    new_can_get_to = set()

    for i, j in can_get_to:
        for ni, nj, v in u.ortho_neighbours_iterator(matrix, i, j):
            if v == '.':
                new_can_get_to.add((ni, nj))

    can_get_to = new_can_get_to

print('')
print('')
m = [[c for c in l] for l in matrix]
for i, j in can_get_to:
    m[i][j] = 'O'

for l in m:
    print(''.join(l))

print(len(can_get_to))


# PART 2
"""
Thanks to the input being very special the problem ends up being much simpler than a general version
The big empty losange is larger than any gap created by walls, so after 65 + 131n (n>=0) steps the covered
territory is always a perfect, completely filled losange. Calculation is a bit of a bitch though
"""

s = 26501365
s -= 65
s //= 131
s //= 2  # Parity means that the formula changes if (s-65)//131 is odd or even

a = (2 * s + 1) ** 2
b = (2 * s - 1) ** 2 + 2 + 3 * (2 * s - 1)
c = (2 * s) ** 2
d = 2 * s

aa = 3726  # Even losange count
bb = 3556  # Even triangles count (i.e. even square minus even losange)
cc = 7331  # Odd square (including losanges and triangles)
dd = 3739  # Odd triangles

print(a * aa + b * bb + c * cc + d * dd)


