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
mem = {'a': 1, 'b': 0}
inst_reg = 0
program = [l for l in lines]

while True:
    if inst_reg >= len(program):
        break

    print(inst_reg, mem)

    full_inst = program[inst_reg]
    inst = full_inst[0:3]
    op = full_inst[4:]

    if inst in ['hlf', 'tpl', 'inc', 'jmp']:
        if inst == 'hlf':
            mem[op] //= 2
            inst_reg += 1

        elif inst == 'tpl':
            mem[op] *= 3
            inst_reg += 1

        elif inst == 'inc':
            mem[op] += 1
            inst_reg += 1

        elif inst == 'jmp':
            inst_reg += int(op)

        continue

    if inst in ['jie', 'jio']:
        r, offset = op.split(', ')
        offset = int(offset)

        if inst == 'jie':
            if mem[r] % 2 == 0:
                inst_reg += offset
            else:
                inst_reg += 1

        if inst == 'jio':
            if mem[r] == 1:
                inst_reg += offset
            else:
                inst_reg += 1

        continue

    raise ValueError('Unexpected instruction', inst)

print(mem)

