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
parser = re.compile('[0-9]{4}')
row, col = None, None

for m in parser.finditer(lines[0]):
    if row is None:
        row = int(m.group())
    else:
        col = int(m.group())

n = row + col - 1
n = n * (n - 1) // 2
n = n + col

first = 20151125
m = 252533
mod = 33554393

res = u.fast_modular_exp(m, n-1, mod)
res = (first * res) % mod 

print(res)


