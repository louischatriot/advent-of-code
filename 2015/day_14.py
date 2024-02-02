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
num_regex = re.compile('[0-9]+')

reinders = list()
for l in lines:
    i0 = l.find(' ')
    cts = [l[0:i0]]
    for m in num_regex.finditer(l):
        cts.append(int(m.group()))
    reinders.append(tuple(cts))

def distance(speed, tfly, trest, total_time):
    periods = total_time // (tfly + trest)
    distance = periods * speed * tfly
    remaining = total_time - periods * (tfly + trest)
    distance += speed * min(tfly, remaining)
    return distance

total = 2503

best = -1
for name, speed, tfly, trest in reinders:
    best = max(best, distance(speed, tfly, trest, total))

print(best)


# PART 2
points = [0 for _ in range(len(reinders))]
positions = [0 for _ in range(len(reinders))]

for total_time in range(1, total+1):
    positions = [distance(speed, tfly, trest, total_time) for _, speed, tfly, trest in reinders]
    best_pos = max(positions)
    for i in range(len(reinders)):
        if positions[i] == best_pos:
            points[i] += 1

print(max(points))



