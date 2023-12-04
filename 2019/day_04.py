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
low, up = lines[0].split('-')
low, up = int(low), int(up)

res = 0
N = 6
for n in range(low, up+1):
    sn = str(n)
    if any(sn[i] == sn[i+1] for i in range(0, N-1)) and all(sn[i] <= sn[i+1] for i in range(0, N-1)):
        res += 1

print(res)


# PART 2
res = 0
N = 6
for n in range(low, up+1):
    sn = str(n)
    if all(sn[i] <= sn[i+1] for i in range(0, N-1)):
        if (
            (sn[0] == sn[1] and sn[1] != sn[2]) or
            (sn[-1] == sn[-2] and sn[-2] != sn[-3]) or
            any(sn[i] == sn[i+1] and sn[i] != sn[i-1] and sn[i+1] != sn[i+2] for i in range(1, N-2))
        ):
            res += 1

print(res)






