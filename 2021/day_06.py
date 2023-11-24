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
fishes = { l: 0 for l in range(0, 9) }
N = 256
for f in list(map(int,lines[0].split(','))):
    fishes[f] += 1

for _ in range(0, N):
    res = { l: 0 for l in range(0, 9) }

    for f in range(1, 9):
        res[f-1] = fishes[f]

    res[6] += fishes[0]
    res[8] = fishes[0]

    fishes = res

print(sum([v for k, v in fishes.items()]))

