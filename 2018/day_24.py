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
__immunes = list()
__infections = list()

current = __immunes
__type = 'immunes'
for line in lines:
    if line == '':
        current = __infections
        __type = 'infections'
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
    group['type'] = __type
    group['dmg_type'] = dmg_type

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


def total_damage(attacker, defender):
    if 'immune' in defender:
        if attacker['dmg_type'] in defender['immune']:
            return 0

    booster = 1
    if 'weak' in defender:
        if attacker['dmg_type'] in defender['weak']:
            booster = 2

    return booster * attacker['nunits'] * attacker['dmg']


import copy

def simulate_battle(__immunes, __infections, boost):
    immunes = [copy.deepcopy(group) for group in __immunes]
    infections = [copy.deepcopy(group) for group in __infections]
    all = immunes + infections
    all_by_id = { group['initiative']: group for group in all }

    for group in immunes:
        group['dmg'] += boost

    while True:
        # Define attack order ; use initiative as group id for mapping
        targets = dict()
        group_order = sorted(all, reverse=True, key=lambda group: (group['nunits'] * group['dmg'], group['initiative']))
        for attack_group in group_order:
            possible_targets = immunes if attack_group['type'] == 'infections' else infections
            possible_targets = [group for group in possible_targets if group['initiative'] not in targets.values()]
            possible_targets = [group for group in possible_targets if total_damage(attack_group, group) > 0]

            # Do we still have defending groups that are not targetted already and that are not immune to the attacker?
            if len(possible_targets) == 0:
                continue

            defense_group = sorted(possible_targets, reverse=True, key=lambda group: (total_damage(attack_group, group), group['nunits'] * group['dmg'], group['initiative']))[0]
            targets[attack_group['initiative']] = defense_group['initiative']


        # Attack in the correct order
        attacks = [(k, v) for k, v in targets.items()]
        attacks = sorted(attacks, reverse=True)

        for a_id, d_id in attacks:
            attack_group = all_by_id[a_id]
            defense_group = all_by_id[d_id]

            # Already dead
            if attack_group['nunits'] == 0:
                continue

            nkills = min(total_damage(attack_group, defense_group) // defense_group['hp'], defense_group['nunits'])
            defense_group['nunits'] -= nkills


        # Update armies
        immunes = [group for group in immunes if group['nunits'] > 0]
        infections = [group for group in infections if group['nunits'] > 0]
        all = immunes + infections
        all_by_id = { group['initiative']: group for group in all }

        if len(immunes) == 0 or len(infections) == 0:
            break

    return (sum(group['nunits'] for group in immunes), sum(group['nunits'] for group in infections))


score_immunes, score_infections = simulate_battle(__immunes, __infections, 0)
print(score_immunes, score_infections)


# PART 2
# Manual dichotomy because I am lazy :)
score_immunes, score_infections = simulate_battle(__immunes, __infections, 35)
print(score_immunes, score_infections)









