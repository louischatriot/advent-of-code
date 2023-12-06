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
times = list(map(int, lines[0].split(':')[1].split()))
distances = list(map(int, lines[1].split(':')[1].split()))

res = 1
for T, D in zip(times, distances):
    ways = 0
    best = T // 2
    while best * (T - best) > D:
        ways += 2
        best -= 1

    if T % 2 == 0:
        ways -= 1

    res *= ways

print(res)


# PART 2
T = int(lines[0].split(':')[1].replace(' ', ''))
D = int(lines[1].split(':')[1].replace(' ', ''))


ways = 0
best = T // 2
while best * (T - best) > D:
    ways += 2
    best -= 1

if T % 2 == 0:
    ways -= 1

print(ways)



