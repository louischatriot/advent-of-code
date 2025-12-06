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
    lines = [line[0:-1] for line in file]


# PART 1
data = [list(map(int, line.split())) for line in lines[0:-1]]
ops = lines[-1].split()
N = len(data)

res = 0
for j in range(len(data[0])):
    if ops[j] == '+':
        res += sum(data[i][j] for i in range(N))
    else:
        res += math.prod(data[i][j] for i in range(N))

print(res)


# PART 2
data = list()
N = len(lines) - 1
j = len(lines[0]) - 1
while j > 0:
    dl = list()
    while j >= 0:
        datum = ''
        for i in range(N):
            datum += lines[i][j]

        j -= 1

        try:
            datum = int(datum)
            dl.append(datum)
        except:
            break

    data.append(dl)

res = 0
for op, dl in zip(reversed(ops), data):
    if op == '+':
        res += sum(dl)
    else:
        res += math.prod(dl)

print(res)



