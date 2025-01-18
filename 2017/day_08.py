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
mem = defaultdict(lambda: 0)

def get_value(s):
    try:
        return int(s)
    except ValueError:
        return mem[s]

conds = dict()
conds['>'] = lambda a, b: get_value(a) > get_value(b)
conds['<'] = lambda a, b: get_value(a) < get_value(b)
conds['>='] = lambda a, b: get_value(a) >= get_value(b)
conds['<='] = lambda a, b: get_value(a) <= get_value(b)
conds['=='] = lambda a, b: get_value(a) == get_value(b)
conds['!='] = lambda a, b: get_value(a) != get_value(b)

MAX = 0

for line in lines:
    inst, cond = line.split(' if ')
    a, op, b = cond.split()

    if conds[op](a, b):
        a, op, b = inst.split()
        if op == 'inc':
            mem[a] += get_value(b)
        else:
            mem[a] -= get_value(b)

        MAX = max(MAX, mem[a])

res = max(mem.values())
print(res)


# PART 2
print(MAX)


