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
data = [int(c) for c in lines[0]]
I = len(data)

def pattern(i):
    p = [0 for _ in range(i)] + [1 for _ in range(i)] + [0 for _ in range(i)] + [-1 for _ in range(i)]
    P = len(p)
    pos = 1

    while True:
        yield p[pos]
        pos = (pos + 1) % P

R = 100

for _ in range(R):
    res = []
    for i in range(I):
        p = pattern(i+1)
        n = 0
        for d in data:
            n += next(p) * d
        n = abs(n) % 10
        res.append(n)

    data = res

print(''.join(map(str, data[0:8])))


# PART 2
data = [int(c) for c in lines[0]]
I = len(data)
offset = int(''.join(map(str, data[0:7])))

useful = []
i = 10000 * I - 1
while i >= offset:
    useful.append(data[i % I])
    i -= 1

useful = np.array(useful)

R = 100
for _ in range(R):
    useful = np.cumsum(useful) % 10

print(''.join(map(str, list(reversed(useful[-8:])))))


