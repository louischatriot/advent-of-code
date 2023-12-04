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
res = 0
for l in lines:
    n = int(l)
    n //= 3
    n -= 2
    res += n

print(res)


# PART 2
mem = dict()
def get_fuel(n):
    if n <= 0:
        return 0

    if n in mem:
        return mem[n]

    fuel = n//3 - 2

    if fuel <= 0:
        return 0

    res = fuel + get_fuel(fuel)
    mem[n] = res  # Actually not that useful
    return res

res = 0
for l in lines:
    res += get_fuel(int(l))

print(res)


