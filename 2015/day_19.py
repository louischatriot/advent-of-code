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

pos = set()

for i, atom in enumerate(molecule):
    for new_atom in rules[atom]:
        new_one = [a for a in molecule]
        new_one[i] = new_atom
        pos.add(''.join(new_one))

print(len(pos))



