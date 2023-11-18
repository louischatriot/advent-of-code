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
depart = int(lines[0])
buses = [int(b) for b in filter(lambda b: b!= 'x', lines[1].split(','))]

the_min = depart + max(buses)
bid = None

for b in buses:
    before = depart - depart  % b
    if before < depart:
        after = before + b
    else:
        after = before

    if after < the_min:
        bid = b
        the_min = after

res = (the_min - depart) * bid
print(res)


# PART 2
buses = []
for idx, b in enumerate(lines[1].split(',')):
    if b != 'x':
        buses.append((int(b), idx))

# Assuming step1 is the big one this is pretty fast
def integrate(start, step1, step2, delta2):
    while (start + delta2) % step2 != 0:
        start += step1

    return start, step1 * step2 // math.gcd(step1, step2)

step, res = buses[0]

for step2, delta2 in buses[1:]:
    res, step = integrate(res, step, step2, delta2)

print(res)
