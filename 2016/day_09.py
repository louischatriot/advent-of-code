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
data = iter(lines[0])
res = ''
pattern = ''
in_pattern = False

while True:
    c = next(data, None)
    if c is None:
        break
    elif c == '(':
        in_pattern = True
        pattern = ''
    elif in_pattern is False:
        res += c
    elif c != ')':
        pattern += c
    else:
        in_pattern = False
        scan, repeat = pattern.split('x')
        scan, repeat = int(scan), int(repeat)
        to_repeat = ''.join([next(data) for _ in range(scan)])
        res += to_repeat * repeat

print(len(res))


# PART 2
def length(s):

    # print(s)
    # print("====================")

    res = 0
    pattern = None

    for i, c in enumerate(s):
        if c == '(' and pattern is None:
            pattern = ''
        elif c == ')' and pattern is not None:
            scan, repeat = pattern.split('x')
            scan, repeat = int(scan), int(repeat)
            to_reapeat = s[i+1:i+1+scan]
            s = s[i+1+scan:]
            break
        else:
            if pattern is None:
                res += 1
            else:
                pattern += c

    # print(res)
    # print(pattern)
    # print(to_reapeat)
    # print(s)

    if pattern is None:
        return res
    else:
        return res + repeat * length(to_reapeat) + length(s)




res = length(lines[0])
print(res)




