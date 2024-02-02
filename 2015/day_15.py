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
ingredients = dict()
for l in lines:
    ing_name, ing_contents = l.split(': ')
    cts = dict()
    for ing in ing_contents.split(', '):
        dim, v = ing.split(' ')
        v = int(v)
        cts[dim] = v

    ingredients[ing_name] = cts

total = 100
names = list(ingredients.keys())
dimensions = [d for d in ingredients[names[0]].keys() if d != 'calories']

best = -1
for i in range(0, total+1):
    for j in range(0, total-i+1):
        for k in range(0, total-i-j+1):
            l = total - i - j - k

            score = 1

            for dim in dimensions:
                subtot = ingredients[names[0]][dim] * i + ingredients[names[1]][dim] * j + ingredients[names[2]][dim] * k + ingredients[names[3]][dim] * l
                subtot = max(0, subtot)
                score *= subtot

            if score > best:
                best = score

print(best)


# PART 2
best = -1
for i in range(0, total+1):
    for j in range(0, total-i+1):
        for k in range(0, total-i-j+1):
            l = total - i - j - k

            score = 1

            for dim in dimensions:
                subtot = ingredients[names[0]][dim] * i + ingredients[names[1]][dim] * j + ingredients[names[2]][dim] * k + ingredients[names[3]][dim] * l
                subtot = max(0, subtot)
                score *= subtot

            # Lazyyyyy
            dim = 'calories'
            calories = ingredients[names[0]][dim] * i + ingredients[names[1]][dim] * j + ingredients[names[2]][dim] * k + ingredients[names[3]][dim] * l

            if score > best and calories == 500:
                best = score

print(best)






