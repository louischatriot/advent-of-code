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
claimed = defaultdict(lambda: 0)
for line in lines:
    id, claim = line.split(" @ ")
    topleft, size = claim.split(": ")
    l, t = topleft.split(',')
    l, t = int(l), int(t)
    w, h = size.split('x')
    w, h = int(w), int(h)

    for y, x in itertools.product(range(l, l+w), range(t, t+h)):
        claimed[(x, y)] += 1

res = sum(1 if claimed[p] >= 2 else 0 for p in claimed)
print(res)


# PART 2
# Ugly and slow, but not interested enough to do better
for line1 in lines:
    id1, claim1 = line1.split(" @ ")
    topleft1, size1 = claim1.split(": ")
    l1, t1 = topleft1.split(',')
    l1, t1 = int(l1), int(t1)
    w1, h1 = size1.split('x')
    w1, h1 = int(w1), int(h1)

    nope = False

    for line2 in lines:
        if line2 == line1:
            continue

        id2, claim2 = line2.split(" @ ")
        topleft2, size2 = claim2.split(": ")
        l2, t2 = topleft2.split(',')
        l2, t2 = int(l2), int(t2)
        w2, h2 = size2.split('x')
        w2, h2 = int(w2), int(h2)

        nope = False
        # if any(l1 <= x2 < l1 + w1 and t1 <= y2 < t1 + h1 for x2, y2 in itertools.product(range(l2, l2+w2), range(t2, t2+h2))):  # That was the hardcore version
        if any(l1 <= x2 < l1 + w1 and t1 <= y2 < t1 + h1 for x2, y2 in [(l2, t2), (l2+w2-1, t2), (l2, t2+h2-1), (l2+w2-1, t2+h2-1)]) or any(l2 <= x1 < l2 + w2 and t2 <= y1 < t2 + h2 for x1, y1 in [(l1, t1), (l1+w1-1, t1), (l1, t1+h1-1), (l1+w1-1, t1+h1-1)]):
            nope = True
            break

    if not nope:
        print(id1)


