import sys
import re
import u as u
from collections import defaultdict, deque
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
data = lines[0]
DISK = 20 if is_example else 272

def expand(data):
    d2 = ''.join(['1' if c == '0' else '0' for c in reversed(data)])
    return data + '0' + d2

def checksum(data):
    if len(data) % 2 == 1:
        return data

    return checksum(''.join('1' if data[2*i] == data[2*i+1] else '0' for i in range(len(data) // 2)))


while len(data) < DISK:
    data = expand(data)

data = data[0:DISK]

res = checksum(data)
print(res)


# PART 2
data = lines[0]
DISK = 20 if is_example else 35651584

while len(data) < DISK:
    data = expand(data)

data = data[0:DISK]

res = checksum(data)
print(res)


