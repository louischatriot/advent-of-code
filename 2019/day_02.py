import sys
import re
import u as u
from collections import defaultdict
import math
import itertools

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
comp = [int(l) for l in lines[0].split(',')]
comp[1] = 12
comp[2] = 2

def run_comp(comp):
    idx = 0
    while True:
        opcode = comp[idx]

        if opcode == 99:
            break

        a, b = comp[idx+1], comp[idx+2]
        a, b = comp[a], comp[b]

        if opcode == 1:
            res = a + b

        if opcode == 2:
            res = a * b

        comp[comp[idx+3]] = res
        idx += 4

    return comp[0]

print(run_comp(comp))


# PART 2
comp_base = [int(l) for l in lines[0].split(',')]
for noun in range(0, 100):
    for verb in range(0, 100):
        comp = [n for n in comp_base]
        comp[1] = noun
        comp[2] = verb
        if run_comp(comp) == 19690720:
            res = 100 * noun + verb
            print(res)





