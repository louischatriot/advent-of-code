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
res = 0
cards = []
N = len(lines)
for l in lines:
    _, contents = l.split(': ')
    winning, numbers = contents.split(' | ')
    winning = { int(n) for n in winning.split() }
    numbers = [int(n) for n in numbers.split()]

    score = 0
    for n in numbers:
        if n in winning:
            if score == 0:
                score = 1
            else:
                score *= 2

    res += score
    cards.append((winning, numbers))

print(res)


# PART 2
mem = dict()
def cards_won(n):
    if n == N-1:
        return 1

    if n > N-1:
        return 0

    if n in mem:
        return mem[n]

    res = 1
    winning, numbers = cards[n]
    n_cards = sum([1 if m in winning else 0 for m in numbers])

    for i in range(0, n_cards):
        res += cards_won(n+i+1)

    mem[n] = res

    return res

res = 0
for n in range(0, N):
    res += cards_won(n)
print(res)




