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
import re
muls = re.compile('mul\([0-9]{1,3},[0-9]{1,3}\)')

def get_muls(s):
    res = 0

    for m in re.findall(muls, s):
        a, b = m.split(',')
        a = int(a[4:])
        b = int(b[0:-1])
        res += a * b

    return res

res = sum(get_muls(line) for line in lines)
print(res)


# PART 2
res = 0
line = ''.join(lines)  # Technically there could be some edge cases here but oh well
for p in line.split('do()'):
    res += get_muls(p.split("don't()")[0])

print(res)

