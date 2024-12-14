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
M=100

machines = list()
idx = 0
while idx < len(lines):
    machine = dict()

    a = lines[idx][10:]
    a = a.split(', ')
    a = list(map(int, [s[2:] for s in a]))
    machine['a'] = a
    idx += 1

    b = lines[idx][10:]
    b = b.split(', ')
    b = list(map(int, [s[2:] for s in b]))
    machine['b'] = b
    idx += 1

    p = lines[idx][7:]
    p = p.split(', ')
    p = list(map(int, [s[2:] for s in p]))
    machine['p'] = p
    idx += 2

    machines.append(machine)


res = 0
for m in machines:
    for bpush in range(M, -1, -1):
        xneed = m['p'][0] - bpush * m['b'][0]

        if xneed % m['a'][0] == 0:
            apush = xneed // m['a'][0]

            if apush * m['a'][1] + bpush * m['b'][1] == m['p'][1] and 0 <= apush <= M:
                cost = 3 * apush + bpush
                res += cost
                break

    else:
        continue

print(res)


# PART 2
BIG = 10000000000000
res = 0

for m in machines:
    m['p'] = list(map(lambda x: BIG + x, m['p']))

    K = m['b'][1] * m['p'][0] - m['b'][0] * m['p'][1]
    D = m['b'][1] * m['a'][0] - m['b'][0] * m['a'][1]

    if K % D != 0:
        continue

    pa = K // D

    if pa < 0:
        continue

    G = m['p'][0] - pa * m['a'][0]

    if G % m['b'][0] != 0:
        continue

    pb = G // m['b'][0]

    if pb < 0:
        continue

    res += 3 * pa + pb


print(res)



