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
banks = [int(n) for n in lines[0].split()]

def sig(banks):
    return '/'.join(list(map(str, banks)))

seen = dict()
seen[sig(banks)] = 0
N = len(banks)
res = 1

while True:
    M = max(banks)
    i = banks.index(M)
    banks[i] = 0

    for d in range(M):
        banks[(i+1+d) % N] += 1

    s = sig(banks)
    if s in seen:
        print("PART 2:", res - seen[s])
        break
    else:
        seen[s] = res
        res += 1

print("PART 1:", res)




