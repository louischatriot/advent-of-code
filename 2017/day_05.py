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
program = [int(line) for line in lines]

inst_pointer = 0
res = 0
while True:
    program[inst_pointer] += 1
    inst_pointer += program[inst_pointer] - 1
    res += 1
    if inst_pointer >= len(program):
        break

print(res)


# PART 2
program = [int(line) for line in lines]

inst_pointer = 0
res = 0
while True:
    change = -1 if program[inst_pointer] >= 3 else 1
    program[inst_pointer] += change
    inst_pointer += program[inst_pointer] - change
    res += 1
    if inst_pointer >= len(program):
        break

print(res)


