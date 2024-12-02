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
from intcode import Computer

# PART 1
program = [int(n) for n in lines[0].split(',')]

N = 50

computers = list()
for c in range(N):
    computer = Computer(program)
    computer.run_until_input(c)
    computers.append(computer)

packets = [list() for _ in range(N)]

while True:
    for c in range(N):
        computer = computers[c]
        opcode = computer.run_until_io()

        if computer.is_io_opcode_input(opcode):
            if len(packets[c]) == 0:
                computer.run_until_input(-1)
            else:
                X, Y = packets[c].pop(0)
                computer.run_until_input(X)
                computer.run_until_input(Y)

        else:
            addr = computer.run_until_output()
            X = computer.run_until_output()
            Y = computer.run_until_output()

            if addr == 255:
                print(Y)
                break

            packets[addr].append((X, Y))

    else:
        continue

    break


# PART 2
computers = list()
for c in range(N):
    computer = Computer(program)
    computer.run_until_input(c)
    computers.append(computer)

packets = [list() for _ in range(N)]







