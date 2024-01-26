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

from intcode import Computer
program = [int(n) for n in lines[0].split(',')]
computer = Computer(program)


# PART 1
instructions = [
    'NOT A J',
    'NOT B T',
    'OR T J',
    'NOT C T',
    'OR T J',
    'NOT D T',
    'NOT T T',
    'AND T J',
    'WALK'
]


instructions = [inst + '\n' for inst in instructions]

# Intcode code is really dirty and I should refactor it but oh well

for inst in instructions:
    for c in inst:
        while True:
            opcode = computer.run_until_io()
            if not computer.is_io_opcode_input(opcode):
                v = computer.run_until_output()
                print(chr(v), end='')

            else:
                v = ord(c)
                computer.run_until_input(v)
                break

while True:
    v = computer.run_until_output()
    if v > 1000:
        print(v)
    else:
        print(chr(v), end='')


# PART 2




