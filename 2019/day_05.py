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

def get_value(comp, idx, mode):
    if mode == '0':
        return comp[comp[idx]]
    else:
        return comp[idx]

def run_comp(comp):
    idx = 0

    while True:
        opcode = comp[idx]
        opcode = str(opcode)
        opcode = '0' * (5 - len(opcode)) + opcode

        if opcode == '00099':
            break

        if opcode[3:] in ['01', '02', '07', '08']:  # 4 parameter instruction
            a = get_value(comp, idx+1, opcode[2])
            b = get_value(comp, idx+2, opcode[1])

            if opcode[3:] == '01':
                res = a + b
                comp[comp[idx+3]] = res

            if opcode[3:] == '02':
                res = a * b
                comp[comp[idx+3]] = res

            if opcode[3:] == '07':
                c = comp[idx+3]
                if a < b:
                    comp[c] = 1
                else:
                    comp[c] = 0

            if opcode[3:] == '08':
                c = comp[idx+3]
                if a == b:
                    comp[c] = 1
                else:
                    comp[c] = 0

            idx += 4

        if opcode[3:] in ['05', '06']:
            a = get_value(comp, idx+1, opcode[2])
            b = get_value(comp, idx+2, opcode[1])

            if opcode[3:] == '05':
                if a != 0:
                    idx = b
                else:
                    idx += 3

            if opcode[3:] == '06':
                if a == 0:
                    idx = b
                else:
                    idx += 3

        if opcode[3:] == '03':
            comp[comp[idx+1]] = 5
            idx += 2

        if opcode[3:] == '04':
            res = get_value(comp, idx+1, opcode[2])
            print("OUPUT", res)
            idx += 2

    return comp[0]

run_comp(comp)

