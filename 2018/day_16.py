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


idx = 0
res = 0
pos = defaultdict(lambda: list())
while idx < len(lines) and lines[idx][0:6] == 'Before':
    memb = [int(v) for v in lines[idx].split(': ')[1][1:-1].split(', ')]
    mema = [int(v) for v in lines[idx+2].split(':  ')[1][1:-1].split(', ')]
    op, a, b, c = lines[idx+1].split()
    op, a, b, c = int(op), int(a), int(b), int(c)

    candidates = {k for k in instructions if instructions[k](memb, a, b, c) == mema}
    if len(candidates) >= 3:
        res += 1

    pos[op].append(candidates)

    idx += 4

print(res)


# PART 2
for op in pos:
    p, pps = pos[op][0], pos[op][1:]
    for pp in pps:
        p = p.intersection(pp)
    pos[op] = p

opcodes = dict()
while len(opcodes) < 16:
    for op in pos:
        if len(pos[op]) == 1:
            break

    instr = pos[op].pop()
    opcodes[op] = instr

    for op in pos:
        if instr in pos[op]:
            pos[op].remove(instr)



idx += 2
mem = [0, 0, 0, 0]
for line in lines[idx:]:
    op, a, b, c = line.split()
    op, a, b, c = int(op), int(a), int(b), int(c)
    mem = instructions[opcodes[op]](mem, a, b, c)


print(mem)







