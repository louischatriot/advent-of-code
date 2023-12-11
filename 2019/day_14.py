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
recipes = dict()
nodes = set()
edges = defaultdict(lambda: set())

for l in lines:
    ingredients, result = l.split(' => ')
    resv, res = result.split(' ')
    resv = int(resv)

    nodes.add(res)

    ing = []
    for iv in ingredients.split(', '):
        v, i = iv.split(' ')
        v = int(v)
        ing.append((i, v))
        edges[res].add(i)

    recipes[res] = (resv, ing)


L = u.topological_sort(nodes, edges)

def get_ore(fuel):
    ingredients = defaultdict(lambda: 0)
    ingredients['FUEL'] = fuel
    for rule in L:
        if rule not in ingredients:
            continue

        if rule == 'ORE':
            continue

        to_be_created = ingredients[rule]
        rule_creating, new_ingredients = recipes[rule]

        rule_n = to_be_created // rule_creating
        if to_be_created % rule_creating != 0:
            rule_n += 1

        for ing, v in new_ingredients:
            ingredients[ing] += v * rule_n

        # No need to delete ingredients, only one rule for each
    return ingredients['ORE']

res = get_ore(1)
print(res)


# PART 2
ore = 1000000000000

m = 1
M = ore

while True:
    pivot = (m + M) // 2

    if get_ore(pivot) <= ore <= get_ore(pivot+1):
        print(pivot)
        break

    if get_ore(pivot) > ore:
        M = pivot
    else:
        m = pivot




