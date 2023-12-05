import sys
import re
import u as u
from collections import defaultdict
import math
import itertools

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
seeds = [int(n) for n in lines[0].split(': ')[1].split()]
mappings = []
mapping = []

for l in lines[2:]:

    if l == '':
        mappings.append(mapping)
        mapping = []
        continue

    if l[-4:] == 'map:':
        continue

    mapping.append(tuple(int(n) for n in l.split()))

mappings.append(mapping)

# TODO: should sort according to source?

best = 99999999999

for s in seeds:
    dest = s
    for mapping in mappings:
        for dest_start, source_start, range_length in mapping:
            if source_start <= dest < source_start + range_length:
                dest += dest_start - source_start
                break

    best = min(best, dest)

print(best)


# PART 2
# No brute force :'(
ranges = { (seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2) }

new_mappings = []
for mapping in mappings:
    new_mapping = []
    for dest_start, source_start, range_length in mapping:
        new_mapping.append((source_start, source_start + range_length - 1, dest_start - source_start))

    new_mappings.append(new_mapping)

mappings = new_mappings


m, M = 0, 9999999999999
new_mappings = []
for mapping in mappings:
    mapping.sort()
    mapping = [(-1, -1, 0)] + mapping + [(M, M, 0)]

    new_mapping = []
    for i in range(0, len(mapping)-1):
        new_mapping.append(mapping[i])

        if mapping[i][1] < mapping[i+1][0] - 1:
            new_mapping.append((mapping[i][1]+1, mapping[i+1][0]-1, 0))

    new_mappings.append(new_mapping)

mappings = new_mappings


res = set()
for __rl, __ru in ranges:
    rrr = { (__rl, __ru) }

    for mapping in mappings:
        new_rrr = set()

        for rl, ru in rrr:
            for sl, su, delta in mapping:
                m, M = max(rl, sl), min(ru, su)

                if m <= M:
                    new_rrr.add((m + delta, M + delta))

        rrr = new_rrr

    res = res.union(rrr)


best = 99999999999
for rl, ru in res:
    best = min(best, rl)

print(best)


