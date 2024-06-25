import sys
import re
import u as u
from collections import defaultdict, deque
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
discs = []
for i, line in enumerate(lines):
    contents = line[12:]
    contents = contents[:-1]
    cl, sp = contents.split(" positions; at time=0, it is at position ")
    cl, sp = int(cl), int(sp)
    sp = (sp + i + 1) % cl
    discs.append((cl, sp))

# Assuming clb and spb are the big ones
def merge(t, clb, spb, cl, sp):
    cycle = u.lcm(clb, cl)

    if (spb + t) % clb != 0:
        t += clb - ((spb + t) % clb)

    while (sp + t) % cl != 0:
        t += clb

    return (t, cycle, (-t) % cycle)


clb, spb = discs[0]
t = 0

for disc in discs[1:]:
    cl, sp = disc
    t, clb, spb = merge(t, clb, spb, cl, sp)

print(t)


# PART 2
t, clb, spb = merge(t, clb, spb, 11, 7)
print(t)




