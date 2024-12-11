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
data = []
idx = 0
for i, c in enumerate(lines[0]):
    if i % 2 == 0:
        for _ in range(int(c)):
            data.append(idx)
        idx += 1
    else:
        for _ in range(int(c)):
            data.append('.')


def dot_iterator(data):
    for i, c in enumerate(data):
        if c == '.':
            yield i

def block_iterator(data):
    for i, c in enumerate(reversed(data)):
        if c != '.':
            yield len(data) - 1 - i


defrag = [c for c in data]
for i, j in zip(dot_iterator(data), block_iterator(data)):
    if i >= j:
        break
    defrag[i], defrag[j] = defrag[j], defrag[i]

res = sum(i * c if c != '.' else 0 for i, c in enumerate(defrag))
print(res)


# PART 2
files, empties = list(), list()
idx = 0
fn = 0
for i, c in enumerate(lines[0]):
    if i % 2 == 0:
        files.append((idx, int(c), fn))
        fn += 1
        idx += int(c)
    else:
        if int(c) > 0:
            empties.append((idx, int(c)))
            idx += int(c)

for fi, fl, fn in reversed(files):
    for idx, e in enumerate(empties):
        ei, el = e
        if fi < ei:
            break

        if el >= fl:
            for i in range(ei, ei+fl):
                data[i] = fn
            for i in range(fi, fi+fl):
                data[i] = '.'

            if el == fl:
                empties = empties[0:idx] + empties[idx+1:]
            else:
                empties = empties[0:idx] + [(ei+fl, el-fl)] + empties[idx+1:]

            break

res = sum(i * c if c != '.' else 0 for i, c in enumerate(data))
print(res)


