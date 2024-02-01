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
__rules = [l.split(' => ') for l in lines[0:-2]]
__molecule = lines[-1]
rules = defaultdict(lambda: list())
for k, v in __rules:
    rules[k].append(v)

molecule_parser = re.compile('[A-Z][a-z]?')
molecule = [m.group() for m in molecule_parser.finditer(__molecule)]

def one_step(molecule):
    pos = set()
    for i, atom in enumerate(molecule):
        for new_atom in rules[atom]:
            new_one = [a for a in molecule]
            new_one[i] = new_atom
            pos.add(''.join(new_one))

    return pos

print(len(one_step(molecule)))


# PART 2
pos = {'e'}
target_molecule = ''.join(molecule)
reductions = [(v, re.compile(v), k) for k, v in __rules]

todo = [(target_molecule, 0)]


molecule, steps = todo.pop(0)

for expanded, expanded_regex, reduced in reductions:
    for m in expanded_regex.finditer(molecule):
        print(expanded)
        s, e = m.span()
        new_molecule = molecule[0:s] + reduced + molecule[e:]
        if new_molecule == 'e':
            print(steps+1)
            sys.exit(0)

        todo.append((new_molecule, steps+1))




"""
# Brute force approach too slow
step = 0
while True:
    step += 1
    new_pos = set()
    for mol in pos:
        new_pos = new_pos.union(one_step(mol))

    if target_molecule in new_pos:
        print(step)
        break

    pos = new_pos
"""



