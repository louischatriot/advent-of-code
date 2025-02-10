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
immunes = list()
infections = list()

current = immunes


for line in lines:
    if line == '':
        current = infections
        continue

    if line[0] == 'I':
        continue

    left, right = line.split('(')
    center, right = right.split(')')

    nunits, hp = left.split(' units each with ')
    hp = hp.split(' ')[0]

    dmg, initiative = right[26:].split(' damage at initiative ')
    dmg, dmg_type = dmg.split(' ')

    nunits, hp, dmg, initiative = int(nunits), int(hp), int(dmg), int(initiative)

    group = dict()
    group['nunits'] = nunits
    group['hp'] = hp
    group['dmg'] = dmg
    group['initiative'] = initiative

    if center != 'nothing':
        center = center.split('; ')

        for c in center:
            if c[0:4] == 'weak':
                key = 'weak'
            else:
                key = 'immune'

            c = c.split(' to ')[1].split(', ')
            group[key] = c

    current.append(group)



print(infections)






