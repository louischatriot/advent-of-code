import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import numpy as np

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
def get_hash(s):
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res

res = 0
for s in lines[0].split(','):
    res += get_hash(s)

print(res)


