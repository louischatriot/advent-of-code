import sys
import re
import u as u
from collections import defaultdict, deque
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
N = 16
if is_example:
    N = 5

steps = list()
for danse in lines[0].split(','):
    t, c = danse[0], danse[1:]

    if t == 's':
        steps.append(('s', int(c), None))

    elif t == 'x':
        i, j = c.split('/')
        i, j = int(i), int(j)
        steps.append(('x', i, j))

    elif t == 'p':
        a, b = c.split('/')
        steps.append(('p', a, b))

    else:
        raise ValueError("Unknown danse step")

def danse(l):
    for t, i, j in steps:
        if t == 's':
            l = l[-i:] + l[0:-i]
        elif t == 'x':
            l[i], l[j] = l[j], l[i]
        elif t == 'p':
            i, j = l.index(i), l.index(j)
            l[i], l[j] = l[j], l[i]

    return l


l = [chr(ord('a') + o) for o in range(N)]
l = danse(l)
res = ''.join(l)
print(res)


# PART 2
R = 1000000000

seen = dict()
loop = 1

l = [chr(ord('a') + o) for o in range(N)]
for r in range(R):
    sig = ''.join(l)
    if sig in seen:
        loop = r - seen[sig]
        break

    seen[sig] = r
    l = danse(l)


l = [chr(ord('a') + o) for o in range(N)]
for r in range(R%loop):
    l = danse(l)

res = ''.join(l)
print(res)






