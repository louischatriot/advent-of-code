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
lights_l = list()
buttons_l = list()
joltages_l = list()

for line in lines:
    data = line.split(' ')

    lights = [True if c == '#' else False for c in data[0][1:-1]]
    lights_l.append(lights)

    buttons = list()
    for b in data[1:-1]:
        bb = list(map(int, b[1:-1].split(',')))
        buttons.append(bb)
    buttons_l.append(buttons)

    joltages = list(map(int, data[-1][1:-1].split(',')))
    joltages_l.append(joltages)


res = 0

# Input small enough for an exhaustive search
# Faster method is a system of linear equations
for lights, buttons in zip(lights_l, buttons_l):
    best = len(buttons) + 1

    for presses in itertools.product([True, False], repeat=len(buttons)):
        state = [False for _ in lights]
        score = sum(1 if p is True else 0 for p in presses)
        if score >= best:
            continue

        for i, p in enumerate(presses):
            if p is True:
                button = buttons[i]
                for b in button:
                    state[b] = not state[b]

        if all(s == l for s, l in zip(state,lights)):
            best = min(best, score)

    res += best

print(res)


# PART 2
# This is a system of linear equations with a constraint
# I'm using z3 to solve it though it is much slower than simply triangulating the matrix then looking at
# all possible values, but it is a pain to code well
from z3 import *

def get_all_results(s):
    result = s.check()

    while result == z3.sat:
        m = s.model()
        yield { str(var()): int(str(m[var])) for var in m }
        # Block current model
        block = [var() != m[var] for var in m]
        s.add(z3.Or(block))
        result = s.check()

n_to_alpha = [c for c in 'abcdefghijklmnopqrstuvwxyz']
alpha_to_n = { c: ord(c) - ord('a') for c in 'abcdefghijklmnopqrstuvwxyz' }

res = 0
for lights, joltages, buttons in zip(lights_l, joltages_l, buttons_l):
    s = Solver()
    variables = list()
    for i in range(len(buttons)):
        variables.append(Int(n_to_alpha[i]))
        s.add(variables[-1] >= 0)

    for j, joltage in enumerate(joltages):
        s.add(sum(    variables[b] if j in button else 0 for b, button in enumerate(buttons)   ) == joltage)

    best = 99999999999999999999
    for r in get_all_results(s):
        score = sum(v for k, v in r.items())
        best = min(best, score)

    res += best

print(res)

