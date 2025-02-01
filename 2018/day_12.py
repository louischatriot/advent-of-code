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
state = set()
xm, xM = float('inf'), -float('inf')
for x, c in enumerate(lines[0].split(': ')[1]):
    if c == '#':
        state.add(x)
        xm = min(xm, x)
        xM = max(xM, x)

rules = dict()
for line in lines[2:]:
    pat, res = line.split(' => ')
    rules[pat] = res


R = 20
for _ in range(R):
    xm -= 2
    xM += 2

    new_state = set()
    nxm, nxM = float('inf'), -float('inf')

    for x in range(xm, xM+1):
        pat = ''.join('#' if x + dx in state else '.' for dx in range(-2, 3))

        if pat in rules and rules[pat] == '#':
            new_state.add(x)
            nxm = min(nxm, x)
            nxM = max(nxM, x)

    state = new_state
    xm, xM = nxm, nxM

print(sum(state))


# PART 2
state = set()
xm, xM = float('inf'), -float('inf')
for x, c in enumerate(lines[0].split(': ')[1]):
    if c == '#':
        state.add(x)
        xm = min(xm, x)
        xM = max(xM, x)


def print_plants(state, xm, xM):
    l = ''.join('#' if x in state else '.' for x in range(xm, xM+1))
    print(l)


R = 1000
for r in range(R):
    xm -= 2
    xM += 2

    new_state = set()
    nxm, nxM = float('inf'), -float('inf')

    for x in range(xm, xM+1):
        pat = ''.join('#' if x + dx in state else '.' for dx in range(-2, 3))

        if pat in rules and rules[pat] == '#':
            new_state.add(x)
            nxm = min(nxm, x)
            nxM = max(nxM, x)

    state = new_state
    xm, xM = nxm, nxM

final_delta = xM - xm  # After a few rounds, the pattern is always the same but moves to the right one step each second
pat_1000 = sorted(list(state))

N = 50000000000

res = sum(pat_1000) + len(pat_1000) * (N - R)
print(res)


