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



