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
import functools

@functools.cache
def n_stones(n, blinks):
    if blinks == 0:
        return 1

    if n == 0:
        return n_stones(1, blinks-1)

    s = str(n)
    if len(s) % 2 == 0:
        return n_stones(int(s[0:len(s)//2]), blinks-1) + n_stones(int(s[len(s)//2:]), blinks-1)
    else:
        return n_stones(n * 2024, blinks-1)

res = 0
blinks = 75
for n in map(int, lines[0].split()):
    res += n_stones(n, blinks)

print(res)

