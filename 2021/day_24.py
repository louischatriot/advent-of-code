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


# PART 1 & 2
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

d = [1, 1, 1, 1, 26, 1, 26, 1, 26, 26, 1, 26, 26, 26]
a = [14, 11, 12, 11, -10, 15, -14, 10, -4, -3, 13, -3, -9, -12]
b = [16, 3, 2, 7, 13, 6, 10, 11, 6, 5, 11, 4, 4, 6]

# Increase if we need to search more
z_boundary = 1000000
R = 14

possible_outputs = { 0 }
outputs_by_stage = [possible_outputs]


for r in range(1, R+1):
    dn, an, bn = d[-r], a[-r], b[-r]
    new_possible_outputs = set()

    for wn in range(1, 10):
        for znminus in range(-z_boundary, z_boundary):
            xn = znminus % 26 + an
            zn = znminus // dn

            if xn != wn:
                zn = 26 * zn + wn + bn

            if zn in possible_outputs:
                new_possible_outputs.add(znminus)

    print(len(new_possible_outputs))
    possible_outputs = new_possible_outputs
    outputs_by_stage = [possible_outputs] + outputs_by_stage


print("outputs by stage", len(outputs_by_stage))


z = outputs_by_stage[0].pop()

for r in range(0, R):
    dn, an, bn = d[r], a[r], b[r]

    # for wn in range(9, 0, -1):  # PART 1
    for wn in range(1, 10):  # PART 2
        xn = z % 26 + an
        zn = z // dn

        if xn != wn:
            zn = 26 * zn + wn + bn

        if zn in outputs_by_stage[r+1]:
            print("FOUND", wn)
            z = zn
            break



