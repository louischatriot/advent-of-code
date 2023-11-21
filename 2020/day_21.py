import sys
import re
import u as u
from collections import defaultdict
import math

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
foods = []
for l in lines:
    ing, all = l.split(' (contains ')
    foods.append((ing.split(' '), all[0:-1].split(', ')))

print(foods)

ingredients = set()
allergens = set()
for ing, all in foods:
    for i in ing:
        ingredients.add(i)
    for a in all:
        allergens.add(a)

print(ingredients)
print(allergens)

all_possible_ingredients = set()

possible_ingredients_by_allergen = dict()

for a in allergens:
    possible_ingredients = {i for i in ingredients}

    for ing, all in foods:
        if a in all:
            possible_ingredients = possible_ingredients.intersection(ing)

    all_possible_ingredients = all_possible_ingredients.union(possible_ingredients)
    possible_ingredients_by_allergen[a] = possible_ingredients


impossible_ingredients = ingredients - all_possible_ingredients
res = 0
for ing, all in foods:
    for i in ing:
        if i in impossible_ingredients:
            res += 1

print(res)


# PART 2
print(possible_ingredients_by_allergen)
new_ones = list()
for a, ing in possible_ingredients_by_allergen.items():
    if len(ing) == 1:
        new_ones.append(list(ing)[0])  # No shame

while len(new_ones) > 0:
    i, new_ones = new_ones[0], new_ones[1:]

    for a, ing in possible_ingredients_by_allergen.items():
        if len(ing) > 1:
            if i in ing:
                ing.remove(i)
                if len(ing) == 1:
                    new_ones.append(list(ing)[0])

arrange = [k + '-' + list(v)[0] for k, v in possible_ingredients_by_allergen.items()]
arrange = sorted(arrange)

res = []
for a in arrange:
    res.append(a.split('-')[1])

res = ','.join(res)
print(res)

