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


# PART 1 & 2
turn = 0
lasts = dict()
last = None

for n in lines[0].split(','):
    v = int(n)
    if last is not None:
        lasts[last] = turn

    turn += 1
    last = v

res = None
while True:
    if last not in lasts:
        v = 0
    else:
        v = turn - lasts[last]

    lasts[last] = turn
    last = v

    turn += 1
    if turn >= 30000000:  # Or 2020 for part 1
        res = last
        break

print(res)
