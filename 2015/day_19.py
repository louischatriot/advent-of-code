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
target_molecule = ''.join(molecule)

# Greedy approach to search & backtracking
rules = sorted(__rules, key=lambda t: -len(t[1]))

def search(molecule, steps):
    if molecule == 'e':
        return steps

    for a, b in rules:
        cnt = molecule.count(b)
        if cnt > 0:
            res = search(molecule.replace(b, a), steps + cnt)  # Wow
            if res is not None:
                return res

    return None

# Surprisingly, this very coarse approach works and is really fast
# There should be inputs where this does not work but the general case is exponential ...
# The correct approach would be a parser (LL(1) or otherwise) but since greedy works I'll take my stars and leave
res = search(target_molecule, 0)
print(res)





"""
# Another brute force, by reducing, also does not work
reductions = [(v, re.compile(v), k) for k, v in __rules]
todo = [(target_molecule, 0)]

while True:
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


"""
# Brute force approach too slow
pos = {'e'}
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



