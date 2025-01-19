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
N = 256

def mix(l, lengths, base_current, base_skip):
    current = base_current
    for skip, length in enumerate(lengths):
        for i in range(length // 2):
            l[(current + i) % N], l[(current + length - 1 - i) % N] = l[(current + length - 1 - i) % N], l[(current + i) % N]

        current = (current + length + base_skip + skip) % N

    return l, current, (base_skip + skip + 1)

def get_hash(s):
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

    return hash

def to_bin(h):
    b = bin(int(f"0x{h}", 16))
    b = b[2:]
    while len(b) < 4:
        b = '0' + b

    return b


kw = lines[0]

nodes = set()
res = 0
for i in range(128):
    s = kw + f"-{i}"
    hash = get_hash(s)
    hash = ''.join([to_bin(c) for c in hash])

    for j, c in enumerate(hash):
        if c == '1':
            res += 1
            nodes.add((i, j))

print(res)


# PART 2
def get_group(start):
    explored = set()
    to_explore = deque()
    to_explore.append(start)

    while to_explore:
        node = to_explore.popleft()
        if node in explored:
            continue
        else:
            explored.add(node)

        i, j = node
        for di, dj in u.ortho_neighbours:
            ni, nj = i+di, j+dj
            if (ni, nj) in nodes:
                to_explore.append((ni, nj))

    return explored


res = 0
explored = set()
for node in nodes:
    if node in explored:
        continue

    res += 1
    group = get_group(node)
    explored = explored.union(group)

print(res)




