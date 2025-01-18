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
lengths = [int(n) for n in lines[0].split(',')]
N = 256
if is_example:
    N = 5

l = [n for n in range(N)]

def mix(l, lengths, base_current, base_skip):
    current = base_current
    for skip, length in enumerate(lengths):
        for i in range(length // 2):
            l[(current + i) % N], l[(current + length - 1 - i) % N] = l[(current + length - 1 - i) % N], l[(current + i) % N]

        current = (current + length + base_skip + skip) % N

    return l, current, (base_skip + skip + 1)


l, current, skip = mix(l, lengths, 0, 0)
res = l[0] * l[1]
print(res)


# PART 2
s = lines[0]
lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]

l = [n for n in range(N)]
current, skip = 0, 0
for _ in range(64):
    l, current, skip = mix(l, lengths, current, skip)

dense = list()
i = 0
while i < len(l):
    e = l[i]
    for _ in range(15):
        i += 1
        e = e ^ l[i]

    dense.append(e)
    i += 1

hash = [hex(n) for n in dense]
hash = [s[2:] if len(s) == 4 else '0' + s[2:] for s in hash]
hash = ''.join(hash)

print(hash)

