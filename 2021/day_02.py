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
pos, depth = 0, 0
for l in lines:
    direction, value = l.split(' ')
    value = int(value)

    if direction == 'forward':
        pos += value

    if direction == 'down':
        depth += value

    if direction == 'up':
        depth -= value

print(pos * depth)


# PART 2
pos, depth, aim = 0, 0, 0
for l in lines:
    direction, value = l.split(' ')
    value = int(value)

    if direction == 'forward':
        pos += value
        depth += aim * value

    if direction == 'down':
        aim += value

    if direction == 'up':
        aim -= value

print(pos * depth)

