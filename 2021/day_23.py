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
rooms = [[] for _ in range(0, 4)]

for i in [3, 2]:
    l = lines[i]
    l = l.replace(' ', '')
    if len(l) > 9:
        l = l[2:-2]
    l = l[1:-1].split('#')

    for idx, amph in enumerate(l):
        rooms[idx].append(amph)


print(rooms)





