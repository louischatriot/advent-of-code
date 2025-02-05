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
    lines = [line[0:-1] for line in file]


# PART 1
instructions = dict()

def addr(mem, a, b, c):
    res = [v for v in mem]
    res[c] = res[a] + res[b]
    return res
instructions['addr'] = addr

def addi(mem, a, b, c):
    res = [v for v in mem]
    res[c] = res[a] + b
    return res
instructions['addi'] = addi

def mulr(mem, a, b, c):
    res = [v for v in mem]
    res[c] = res[a] * res[b]
    return res
instructions['mulr'] = mulr

def muli(mem, a, b, c):
    res = [v for v in mem]
    res[c] = res[a] * b
    return res
instructions['muli'] = muli

def banr(mem, a, b, c):
    res = [v for v in mem]
    res[c] = res[a] & res[b]
    return res
instructions['banr'] = banr

def bani(mem, a, b, c):
    res = [v for v in mem]
    res[c] = res[a] & b
    return res
instructions['bani'] = bani

def borr(mem, a, b, c):
    res = [v for v in mem]
    res[c] = res[a] | res[b]
    return res
instructions['borr'] = borr

def bori(mem, a, b, c):
    res = [v for v in mem]
    res[c] = res[a] | b
    return res
instructions['bori'] = bori

def setr(mem, a, b, c):
    res = [v for v in mem]
    res[c] = res[a]
    return res
instructions['setr'] = setr

def seti(mem, a, b, c):
    res = [v for v in mem]
    res[c] = a
    return res
instructions['seti'] = seti

def gtir(mem, a, b, c):
    res = [v for v in mem]
    res[c] = 1 if a > res[b] else 0
    return res
instructions['gtir'] = gtir

def gtri(mem, a, b, c):
    res = [v for v in mem]
    res[c] = 1 if res[a] > b else 0
    return res
instructions['gtri'] = gtri

def gtrr(mem, a, b, c):
    res = [v for v in mem]
    res[c] = 1 if res[a] > res[b] else 0
    return res
instructions['gtrr'] = gtrr

def eqir(mem, a, b, c):
    res = [v for v in mem]
    res[c] = 1 if a == res[b] else 0
    return res
instructions['eqir'] = eqir

def eqri(mem, a, b, c):
    res = [v for v in mem]
    res[c] = 1 if res[a] == b else 0
    return res
instructions['eqri'] = eqri

def eqrr(mem, a, b, c):
    res = [v for v in mem]
    res[c] = 1 if res[a] == res[b] else 0
    return res
instructions['eqrr'] = eqrr


opcodes = {12: 'eqir', 14: 'gtrr', 4: 'gtri', 7: 'eqri', 9: 'eqrr', 15: 'gtir', 0: 'bani', 5: 'banr', 8: 'seti', 1: 'addr', 2: 'mulr', 11: 'setr', 13: 'muli', 3: 'addi', 10: 'bori', 6: 'borr'}

class Computer:
    def __init__(self, ip_reg, program):
        self.ip = 0
        self.ip_reg = ip_reg
        self.program = [(opcode, a, b, c) for opcode, a, b, c in program]
        self.mem = [0 for _ in range(6)]

    def run(self):
        while True:
            if self.ip >= len(self.program):
                break

            opcode, a, b, c = self.program[self.ip]
            self.mem[self.ip_reg] = self.ip
            self.mem = instructions[opcode](self.mem, a, b, c)
            self.ip = self.mem[self.ip_reg]
            self.ip += 1


ip_reg = int(lines[0][-1])

program = list()
for line in lines[1:]:
    opcode, a, b, c = line.split()
    a, b, c = int(a), int(b), int(c)
    program.append((opcode, a, b, c))

computer = Computer(ip_reg, program)
computer.run()
print(computer.mem[0])


# PART 2
# Looking reaaaaaally hard at the code, you see that it's actually adding to zero all numbers that divide
# register 5 (after it is initialized) evenly. The N below is the one initialized after the first time the
# code jumped to inst 17 then back. To understand how it works look in particular at lines 3 to 11, a very
# inefficient way to determine whether register 1 divides register 5 and if yes add the quotient
N = 10551345
res = 0
for d in range(1, N+1):
    if N % d == 0:
        res += d

print(res)


