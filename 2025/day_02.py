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
res = 0

for ran in lines[0].split(','):
    l, u = ran.split('-')
    l, u = int(l), int(u)

    for _id in range(l, u+1):
        id = str(_id)
        if len(id) % 2 == 0:
            if id[0:len(id)//2] == id[len(id)//2:]:
                res += int(id)

print(res)


# PART 2
res = 0

def invalid(id):
    for l in range(1, len(id)//2 + 1):
        if len(id) % l == 0:
            if id == id[0:l] * (len(id) // l):
                return True

    return False


for ran in lines[0].split(','):
    l, u = ran.split('-')
    l, u = int(l), int(u)

    for _id in range(l, u+1):
        id = str(_id)
        if invalid(id):
            res += int(id)

print(res)


