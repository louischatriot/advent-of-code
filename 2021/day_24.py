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


z_boundary = 1000000
possible_z = set()

for z in range(-z_boundary, z_boundary):
    possible_z.add(z)

new_possible_z = set()
for w in range(0, 10):
    x = (z % 26) - 12

    zn = z // 26
    if x != w:
        zn *= 26

    zn += x * (w + 6)

    if zn == 0:
        new_possible_z.add(z)

print(len(new_possible_z))






