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


# The code clearly balooned into this ugly mess but it works - I should make it more systematic
class Computer:
    def __init__(self, program):
        self.program = [n for n in program] + [0 for _ in range(0, 100000)]  # Large memory!
        self.idx = 0
        self.relative_base = 0

    def get_value(self, idx, mode):
        if mode == '0':  # Position mode
            return self.program[self.program[idx]]
        elif mode == '1':  # Immediate mode
            return self.program[idx]
        elif mode == '2':
            return self.program[self.program[idx] + self.relative_base]
        else:
            raise ValueError(f"Unknown mode {mode}")

    def set_value(self, idx, mode, value):
        if mode == '0':  # Position mode
            self.program[self.program[idx]] = value
        elif mode == '1':  # Immediate mode
            raise ValueError("Immediate mode refused for setting a value")
        elif mode == '2':
            self.program[self.program[idx] + self.relative_base] = value
        else:
            raise ValueError(f"Unknown mode {mode}")

    def run_until_io(self):
        while True:
            opcode = self.program[self.idx]
            opcode = str(opcode)
            opcode = '0' * (5 - len(opcode)) + opcode

            if opcode == '00099':
                return None

            # Addition (1), multiplication (2), lt comparison (7), eql comparison (8)
            if opcode[3:] in ['01', '02', '07', '08']:  # 4 parameter instruction
                a = self.get_value(self.idx+1, opcode[2])
                b = self.get_value(self.idx+2, opcode[1])

                if opcode[3:] == '01':
                    self.set_value(self.idx+3, opcode[0], a + b)

                if opcode[3:] == '02':
                    self.set_value(self.idx+3, opcode[0], a * b)

                if opcode[3:] == '07':
                    if a < b:
                        self.set_value(self.idx+3, opcode[0], 1)
                    else:
                        self.set_value(self.idx+3, opcode[0], 0)

                if opcode[3:] == '08':
                    if a == b:
                        self.set_value(self.idx+3, opcode[0], 1)
                    else:
                        self.set_value(self.idx+3, opcode[0], 0)

                self.idx += 4

            # Conditional jump
            if opcode[3:] in ['05', '06']:
                a = self.get_value(self.idx+1, opcode[2])
                b = self.get_value(self.idx+2, opcode[1])

                if opcode[3:] == '05':
                    if a != 0:
                        self.idx = b
                    else:
                        self.idx += 3

                if opcode[3:] == '06':
                    if a == 0:
                        self.idx = b
                    else:
                        self.idx += 3

            # Relative base update
            if opcode[3:] == '09':
                self.relative_base += self.get_value(self.idx+1, opcode[2])
                self.idx += 2

            # Input (3) / output (8)
            if opcode[3:] in ['03', '04']:
                return opcode


    def run_until_input(self, the_input):
        opcode = self.run_until_io()

        if opcode is None:
            return None

        if opcode[3:] != '03':
            raise ValueError("Ran until input but no input instruction")

        self.set_value(self.idx+1, opcode[2], the_input)
        self.idx += 2


    def run_until_output(self):
        opcode = self.run_until_io()

        if opcode is None:
            return None

        if opcode[3:] != '04':
            raise ValueError("Ran until output but no output instruction")

        res = self.get_value(self.idx+1, opcode[2])
        self.idx += 2
        return res

# PART 1
program = [int(n) for n in lines[0].split(',')]
moves = { (-1, 0): [(0, -1), (0, 1)], (1, 0): [(0, 1), (0, -1)], (0, -1): [(1, 0), (-1, 0)], (0, 1): [(-1, 0), (1, 0)] }

comp = Computer(program)
painted = dict()

x, y = 0, 0
direction = (-1, 0)  # Up
out = None
while True:
    current_color = 0
    if (x, y) in painted and painted[(x, y)] == 1:
        current_color = 1

    comp.run_until_input(current_color)

    paint = comp.run_until_output()
    if paint is None:
        break

    painted[(x, y)] = paint

    move = comp.run_until_output()
    if move is None:
        break

    direction = moves[direction][move]
    x, y = x + direction[0], y + direction[1]


print(len(painted))


# PART 2
comp = Computer(program)
painted = dict()
painted[(0, 0)] = 1

x, y = 0, 0
direction = (-1, 0)  # Up
out = None
while True:
    current_color = 0
    if (x, y) in painted and painted[(x, y)] == 1:
        current_color = 1

    comp.run_until_input(current_color)

    paint = comp.run_until_output()
    if paint is None:
        break

    painted[(x, y)] = paint

    move = comp.run_until_output()
    if move is None:
        break

    direction = moves[direction][move]
    x, y = x + direction[0], y + direction[1]

mx, Mx, my, My = 999999999, -999999999, 999999999, -999999999
for x, y in painted:
    mx, Mx, my, My = min(mx, x), max(Mx, x), min(my, y), max(My, y)

matrix = [['.' for _ in range(my, My+1)] for _ in range(mx, Mx+1)]

for x, y in painted:
    if painted[(x, y)] == 1:
        matrix[x][y] = 'X'

for l in matrix:
    print(' '.join(l))





