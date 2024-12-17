import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import collections
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
from computer import Computer

program, registers = Computer.parse_input(lines)
computer = Computer(program, registers)
computer.run()
print(','.join(list(map(str, computer.stdout))))


# PART 2
computer = Computer(program, registers)
if is_example:
    computer.registers['a'] = 117440
else:
    computer.registers['a'] = 107413700225434  # Found by the algorithm below
computer.run()

res = ','.join(list(map(str, computer.stdout)))
print("Computation result", res)

target = ','.join(map(str, program))
print("Target            ", target)


def out(a):
    b = a % 8
    b = b ^ 5
    c = a // (2 ** b)
    b = b ^ 6
    b = b ^ c

    return b % 8


def antecedents(t, terminal=False):
    res = list()

    bound = 8 if terminal else 1024

    for a in range(bound):
        if out(a) == t:
            res.append(a)

    return res


def padded(n):
    res = bin(n)
    res = '0b' + '0' * (12-len(res)) + res[2:]
    return res


def possible(l):
    ants = [antecedents(l[0], True)] + [antecedents(n) for n in l[1:]]
    ants = [list(map(lambda x: padded(x)[2:], ant)) for ant in ants]
    pos = [[a] for a in ants[-1]]

    for i in range(len(ants) - 2, -1, -1):
        next_list = list()

        for a, p in itertools.product(ants[i], pos):
            if a[3:] == p[0][0:7]:
                next_list.append([a, *p])

        pos = next_list

    return pos


def collapse(l):
    n = l[0] + ''.join(a[-3:] for a in l[1:])
    n = int('0b' + n, 2)
    return n


# All possibilities to get the exact copy of the program
pos = possible(list(reversed(program)))

best = 99999999999999999999999  # Should be big enough!

for p in pos:
    a = collapse(p)
    best = min(best, collapse(p))

    # Uncomment the below to check that all solutions yield the program itself (only works with actual input)
    # computer = Computer(program)
    # computer.registers['a'] = a
    # computer.run()
    # res = ','.join(list(map(str, computer.stdout)))
    # print(res)

print(best)


