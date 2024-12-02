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
program = [int(n) for n in lines[0].split(',')]
computer = Computer(program)

def print_message(computer):
    while True:
        opcode = computer.run_until_io()
        if computer.is_io_opcode_input(opcode):
            break

        c = computer.run_until_output()
        print(chr(c), end='')

def input_command(computer, cmd):
    for c in cmd:
        computer.run_until_input(ord(c))
    computer.run_until_input(10)


while True:
    print_message(computer)
    cmd = input()
    input_command(computer, cmd)


# Now play the game and find the password :)




