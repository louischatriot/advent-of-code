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
weapons = [
    (8, 4),
    (10, 5),
    (25, 6),
    (40, 7),
    (74, 8)
]

armors = [
    (0, 0),
    (13, 1),
    (31, 2),
    (53, 3),
    (75, 4),
    (102, 5)
]

rings = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3)
]

# Puzzle input
boss = [100, 8, 2]

def simulate_battle(damage, armor, boss):
    hp = 100
    boss_hp, boss_damage, boss_armor = boss

    while True:
        boss_hp -= 1 if damage <= boss_armor else damage - boss_armor
        if boss_hp <= 0:
            return True

        hp -= 1 if boss_damage <= armor else boss_damage - armor
        if hp <= 0:
            return False

min_cost = 999999999

for weapon in weapons:
    for armor_pick in armors:
        for L in [0, 1, 2]:
            for ring_choice in itertools.combinations(rings, L):
                damage = weapon[1]
                armor = armor_pick[1]
                cost = weapon[0] + armor_pick[0]

                for ring in ring_choice:
                    cost += ring[0]
                    damage += ring[1]
                    armor += ring[2]

                if simulate_battle(damage, armor, boss):
                    min_cost = min(min_cost, cost)

print(min_cost)


# PART 2
max_cost = -1

for weapon in weapons:
    for armor_pick in armors:
        for L in [0, 1, 2]:
            for ring_choice in itertools.combinations(rings, L):
                damage = weapon[1]
                armor = armor_pick[1]
                cost = weapon[0] + armor_pick[0]

                for ring in ring_choice:
                    cost += ring[0]
                    damage += ring[1]
                    armor += ring[2]

                if not simulate_battle(damage, armor, boss):
                    max_cost = max(max_cost, cost)

print(max_cost)







