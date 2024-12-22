import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import collections
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
rounds = 2000

def next_secret(n):
    n = n ^ (n << 6)
    n = n % 16777216

    n = (n >> 5) ^ n
    n = n % 16777216

    n = n ^ (n << 11)
    n = n % 16777216

    return n

EXAMPLE = None  # To use the longer example

if EXAMPLE is not None:
    lines = [123]


# Uncomment for part 2 ; WTF Eric oO
if is_example:
    lines = [1, 2, 3, 2024]

seqs = dict()
for line in lines:
    n = int(line)

    seq = list()
    next_n = n
    for _ in range(rounds+1):
        seq.append(next_n)
        next_n = next_secret(next_n)

    assert len(seq) == rounds + 1  # Initial n then 2000 rounds

    seqs[n] = seq


res = sum(seqs[n][-1] for n in seqs)
print(res)


# PART 2
prices = dict()
diffs = dict()
for n in seqs:
    prices[n] = [a % 10 for a in seqs[n]]
    diffs[n] = [b - a for a, b in u.pairwise(prices[n])]

    assert len(prices[n]) == rounds + 1
    assert len(diffs[n]) == rounds

patterns = defaultdict(lambda: dict())
for n in seqs:
    seq = seqs[n]
    price = prices[n]
    diff = diffs[n]

    for i in range(rounds-3):
        pattern = tuple(diff[i:i+4])

        if n not in patterns[pattern]:
            patterns[pattern][n] = price[i+4]

best = 0
for pattern, values in patterns.items():
    bananas = sum(v for n, v in values.items())

    if bananas > best:
        best = bananas

print(best)

