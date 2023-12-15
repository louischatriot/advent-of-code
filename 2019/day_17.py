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
from intcode import Computer
program = [int(n) for n in lines[0].split(',')]
computer = Computer(program)

data = []
l = []
while True:
    out = computer.run_until_output()
    if out is None:
        break
    else:
        if out == 10 and len(l) > 0:
            data.append(l)
            l = []
        else:
            l.append(chr(out))

for l in data:
    print(''.join(l))

si, sj = None, None
for i, l in enumerate(data):
    for j, c in enumerate(l):
        if c != '.' and c != '#':
            si, sj = i, j





