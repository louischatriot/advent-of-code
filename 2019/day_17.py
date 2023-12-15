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
    print(' '.join(l))

I, J = len(data), len(data[0])

res = 0
intersections = set()
for i, j in itertools.product(range(I), range(J)):
    neighbs = [v for v in u.ortho_neighbours_iterator(data, i, j)]
    if sum(1 if v[2] == '#' else 0 for v in neighbs) == 4 and data[i][j] == '#':
        intersections.add((i, j))
        res += i * j

print(res)


# PART 2
# Doing this by hand as writing this kind of algo is a bit of a pain but
# it could be done with standard backtracking (state being length of the first two
# formulas being arbitrarily called A and B then fitting until the need to create C
# then expanding C until there is a solution, or backtrack. A pain.

si, sj = None, None
for i, l in enumerate(data):
    for j, c in enumerate(l):
        if c != '.' and c != '#':
            si, sj = i, j

functions = {
    'A': 'R,8,L,4,R,4,R,10,R,8',
    'B': 'L,12,L,12,R,8,R,8',
    'C': 'R,10,R,4,R,4',
    'Z': 'R,8,L,4,R,4,R,10,R,8,R,8,L,4,R,4,R,10,R,8,L,12,L,12,R,8,R,8,R,10,R,4,R,4,L,12,L,12,R,8,R,8,R,10,R,4,R,4,L,12,L,12,R,8,R,8,R,10,R,4,R,4,R,10,R,4,R,4,R,8,L,4,R,4,R,10,R,8'
}

"""
# Used to find the right sub functions manually
print(functions['Z'])

for f in functions:
    if f != 'Z' and len(functions[f]) > 0:
        functions['Z'] = functions['Z'].replace(functions[f], f)

print(functions['Z'])
"""

# formula = 'Z'
formula = 'A,A,B,C,B,C,B,C,C,A'

dirs = {
    'up': {'L': 'left', 'R': 'right'},
    'down': {'L': 'right', 'R': 'left'},
    'left': {'L': 'down', 'R': 'up'},
    'right': {'L': 'up', 'R': 'down'}
}

move_dir = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

dir = 'up'
i, j = si, sj

for f in formula.split(','):
    for c in functions[f].split(','):
        if c in ['L', 'R']:
            dir = dirs[dir][c]
            data[i][j] = f
        else:
            n = int(c)
            di, dj = move_dir[dir]
            for _ in range(0, n):
                i, j = i+di, j+dj
                data[i][j] = f

for l in data:
    print(' '.join(l))

# Running the computer with the right sequence
# This code is fucking ugly, I don't understand why it wants to spout the entire matrix first
# and the structure makes it hard and not interesting to debug so here we go
program = [int(n) for n in lines[0].split(',')]
program[0] = 2
computer = Computer(program)

for s in [formula, functions['A'], functions['B'], functions['C']]:
    for c in s:
        computer.run_until_input_ignore_output(ord(c))

    computer.run_until_input_ignore_output(10)


computer.run_until_input_ignore_output(ord('n'))
computer.run_until_input_ignore_output(10)

while True:
    res = computer.run_until_output()
    if res > 1000:
        print(res)
        break







