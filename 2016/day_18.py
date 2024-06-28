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
line = ['.'] + [c for c in lines[0]] + ['.']
N = 400000
if is_example:
    N = 10

def is_trap(l, c, r):
    if l == '^' and c == '^' and r == '.':
        return True

    if r == '^' and c == '^' and l == '.':
        return True

    if l == '^' and c == '.' and r == '.':
        return True

    if r == '^' and c == '.' and l == '.':
        return True

    return False



print(' '.join(line[1:-1]))
res = sum(1 if c == '.' else 0 for c in line[1:-1])


for _ in range(0, N-1):
    line = ['.'] + ['^' if is_trap(line[i-1], line[i], line[i+1]) else '.' for i in range(1, len(line)-1)] + ['.']

    # print(' '.join(line[1:-1]))
    res += sum(1 if c == '.' else 0 for c in line[1:-1])


print(res)




