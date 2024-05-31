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
BIG = 999999999
res = 0
real_rooms = []

for line in lines:
    checksum = line[-6: -1]
    sid = int(line[-10: -7])
    room = line[0:-11]

    d = defaultdict(lambda: 0)
    for c in room:
        if c != '-':
            d[c] += 1

    l = []
    for k, v in d.items():
        l.append((- BIG * v + ord(k), k))

    l = sorted(l)
    l = ''.join(list(map(lambda i: i[1], l[0:5])))

    if l == checksum:
        res += sid
        real_rooms.append((room, sid))

print(res)


# PART 2
for room, sid in real_rooms:
    # print(room, sid)

    true_name = ''

    for c in room:
        if c == '-':
            true_name += '-'
        else:
            nc = ord(c) - ord('a')
            nc += sid
            nc %= 26
            nc += ord('a')
            true_name += chr(nc)

    print(true_name, sid)   # And run with a grep north





