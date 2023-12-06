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
comp_template = [int(l) for l in lines[0].split(',')]

def get_value(comp, idx, mode):
    if mode == '0':
        return comp[comp[idx]]
    else:
        return comp[idx]

class Computer:
    def __init__(self, program):
        self.program = [n for n in program]
        self.idx = 0

    def run_until_io(self):
        while True:
            opcode = self.program[self.idx]
            opcode = str(opcode)
            opcode = '0' * (5 - len(opcode)) + opcode

            if opcode == '00099':
                return None

            if opcode[3:] in ['01', '02', '07', '08']:  # 4 parameter instruction
                a = get_value(self.program, self.idx+1, opcode[2])
                b = get_value(self.program, self.idx+2, opcode[1])

                if opcode[3:] == '01':
                    res = a + b
                    self.program[self.program[self.idx+3]] = res

                if opcode[3:] == '02':
                    res = a * b
                    self.program[self.program[self.idx+3]] = res

                if opcode[3:] == '07':
                    c = self.program[self.idx+3]
                    if a < b:
                        self.program[c] = 1
                    else:
                        self.program[c] = 0

                if opcode[3:] == '08':
                    c = self.program[self.idx+3]
                    if a == b:
                        self.program[c] = 1
                    else:
                        self.program[c] = 0

                self.idx += 4

            if opcode[3:] in ['05', '06']:
                a = get_value(self.program, self.idx+1, opcode[2])
                b = get_value(self.program, self.idx+2, opcode[1])

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

            if opcode[3:] in ['03', '04']:
                return opcode


    def run_until_input(self, the_input):
        opcode = self.run_until_io()

        if opcode is None:
            return None

        if opcode[3:] != '03':
            raise ValueError("Ran until input but no input instruction")

        self.program[self.program[self.idx+1]] = the_input
        self.idx += 2


    def run_until_output(self):
        opcode = self.run_until_io()

        if opcode is None:
            return None

        if opcode[3:] != '04':
            raise ValueError("Ran until output but no output instruction")

        res = get_value(self.program, self.idx+1, opcode[2])
        self.idx += 2
        return res



best = -99999999999
for sequence in itertools.permutations(range(5)):
    comps = [Computer(comp_template), Computer(comp_template), Computer(comp_template), Computer(comp_template), Computer(comp_template)]
    for i, s in enumerate(sequence):
        comps[i].run_until_input(s)

    out = 0
    for i in range(5):
        comps[i].run_until_input(out)
        out = comps[i].run_until_output()

    best = max(best, out)

print(best)


# PART 2
best = -99999999999
for __sequence in itertools.permutations(range(5)):
    sequence = [s+5 for s in __sequence]

    comps = [Computer(comp_template), Computer(comp_template), Computer(comp_template), Computer(comp_template), Computer(comp_template)]
    for i, s in enumerate(sequence):
        comps[i].run_until_input(s)

    out = 0
    last_out = None
    while out is not None:
        for i in range(5):
            comps[i].run_until_input(out)
            out = comps[i].run_until_output()
            if out is None:
                break

        if out is not None:
            last_out = out

    best = max(best, last_out)

print(best)


