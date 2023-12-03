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
games = dict()
for l in lines:
    g, contents = l.split(': ')
    drawings = contents.split('; ')
    game = []
    for drawing in drawings:
        d = defaultdict(lambda: 0)
        balls = drawing.split(', ')
        for b in balls:
            v, k = b.split(' ')
            d[k] = int(v)

        game.append(d)


    _, g = g.split(' ')
    g = int(g)
    games[g] = game


res = 0
maxes = { 'red': 12 , 'green': 13 , 'blue': 14 }

for gn, game in games.items():
    if all([ all([ drawing[b] <= maxes[b]  for b in maxes ]) for drawing in game]):
        res += gn

print(res)


# PART 2
res = 0
for gn, game in games.items():
    maxes = defaultdict(lambda: 0)
    for drawing in game:
        for b, v in drawing.items():
            maxes[b] = max(maxes[b], v)

    res += maxes['red'] * maxes['blue'] * maxes['green']

print(res)






