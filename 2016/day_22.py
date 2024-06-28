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
nodes = []
for line in lines[2:]:
    contents = line[15:].split()
    x, y = contents[0].split('-')
    x, y = int(x[1:]), int(y[1:])
    nodes.append(((x, y), int(contents[1][0:-1]), int(contents[2][0:-1]), int(contents[3][0:-1])))

res = 0
for n in nodes:
    for m in nodes:
        ncoord, _, nused, navail = n
        mcoord, _, mused, mavail = m

        nx, ny = ncoord
        mx, my = mcoord

        if nx != mx or ny != my:
            if nused <= mavail:  # Symetric case checked when n and m are swapped
                if nused > 0:
                    res += 1

print(res)


# PART 2

