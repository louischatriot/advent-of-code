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
"""
n_digits = 14
batch = len(lines) // n_digits
batch_length = 10

for b in range(0, batch):
    l = ''
    for d in range(0, n_digits):

        to_add = lines[batch * d + b]
        to_add += ' ' * (batch_length - len(to_add))

        l += to_add

    print(l)
"""

d = [-99999999, 1, 1, 1, 1, 26, 1, 26, 1, 26, 26, 1, 26, 26, 26]
a = [-99999999, 14, 11, 12, 11, -10, 15, -14, 10, -4, -3, 13, -3, -9, -12]
b = [-99999999, 16, 3, 2, 7, 13, 6, 10, 11, 6, 5, 11, 4, 4, 6]

# Increase if we need to search more
z_boundary = 1000000
possible_z = set()
for z in range(0, z_boundary):
    possible_z.add(z)
    possible_z.add(-z)


dn, an, bn = d[-1], a[-1], b[-1]

new_possible_z = set()
for wn in range(0, 10):
    for znminus in possible_z:
        xn = znminus % 26
        zn = znminus // dn
        xn = xn + an
        if xn != wn:
            zn = 26 * zn + wn + bn

        if zn == 0:
            new_possible_z.add(znminus)

print(new_possible_z)

# First step is quite slow
new_possible_z = {12, 13, 14, 15, 16, 17, 18, 19, 20, 21}
possible_z = new_possible_z





for round in range(2, 14):
    dn, an, bn = d[-round], a[-round], b[-round]

    new_possible_z = set()
    for wn in range(0, 10):
        for znminus in possible_z:
            xn = znminus % 26
            zn = znminus // dn
            xn = xn + an
            if xn != wn:
                zn = 26 * zn + wn + bn

            if zn == 0:
                new_possible_z.add(znminus)

    print(new_possible_z)
    possible_z = new_possible_z




