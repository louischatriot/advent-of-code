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
state = lines[0][-2]
steps = int(lines[1][36:-7])

states = dict()
i = 3
while i < len(lines):
    __s = dict()
    s = lines[i][-2]

    w = int(lines[i+2][-2])
    d = -1 if lines[i+3][-3] == 'f' else 1
    ns = lines[i+4][-2]
    __s[0] = (w, d, ns)

    w = int(lines[i+6][-2])
    d = -1 if lines[i+7][-3] == 'f' else 1
    ns = lines[i+8][-2]
    __s[1] = (w, d, ns)

    states[s] = __s
    i += 10

tape = set()
pos = 0
for _ in range(steps):
    cv = 1 if pos in tape else 0

    w, d, ns = states[state][cv]

    if w == 1:
        tape.add(pos)
    else:
        if pos in tape:
            tape.remove(pos)

    pos += d
    state = ns


print(len(tape))

