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

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

# PART 1
res = 0
for l in lines:
    seq = [int(n) for n in l.split()]

    endings = [seq[-1]]

    while not all(n == 0 for n in seq):
        seq = [b-a for a, b in pairwise(seq)]
        endings.append(seq[-1])

    nv = sum(endings)
    res += nv

print(res)


# PART 2
res = 0
for l in lines:
    seq = [int(n) for n in l.split()]

    begs = [seq[0]]

    while not all(n == 0 for n in seq):
        seq = [b-a for a, b in pairwise(seq)]
        begs.append(seq[0])

    n = 0
    for v in reversed(begs[0:-1]):
        n = v - n

    res += n

print(res)






