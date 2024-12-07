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
ops = ['+', '*']

def calc(numbers, oplist):
    res = numbers[0]
    for n, op in zip(numbers[1:], oplist):
        if op == '+':
            res = res + n
        elif op == '*':
            res = res * n
        elif op == '||':
            res = int(str(res) + str(n))  # Clean.
        else:
            raise ValueError("Unknown operator")

    return res


res = 0

for line in lines:
    target, numbers = line.split(': ')
    target = int(target)
    numbers = list(map(int, numbers.split()))

    if any(target == calc(numbers, oplist) for oplist in itertools.product(ops, repeat=len(numbers)-1)):
        res += target

print(res)


# PART 2
ops.append('||')
res = 0

for line in lines:
    target, numbers = line.split(': ')
    target = int(target)
    numbers = list(map(int, numbers.split()))

    if any(target == calc(numbers, oplist) for oplist in itertools.product(ops, repeat=len(numbers)-1)):
        res += target

print(res)






