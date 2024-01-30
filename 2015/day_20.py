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
N = int(lines[0])
SIEVE_MAX = 1000000  # Found after a bit of sizing up

# Inspired from Erathostène's sieve
l = [0 for _ in range(SIEVE_MAX)]
for i in range(1, SIEVE_MAX):
    for k in range(i, SIEVE_MAX, i):
        l[k] += 10 * i

for k, v in enumerate(l):
    if v > N:
        print(k)
        break


# PART 2
MAX_HOUSES = 50
l = [0 for _ in range(SIEVE_MAX)]
for i in range(1, SIEVE_MAX):
    for k in range(i, (MAX_HOUSES + 1) * i, i):
        if k < SIEVE_MAX:
            l[k] += 11 * i

for k, v in enumerate(l):
    if v > N:
        print(k)
        break








# PART 1
# Initial approach, very empiric and slow as it relies on divisors
sys.exit(0)

N = int(lines[0])
target = N // 10
primes = u.primes_until_n(target + 1)


M = -1

for house in range(1, 100):  # Increase range to find a good max for the ratio
    d = u.sum_of_divisors(house, primes)
    M = max(M, d / house)


start = math.floor(target / 4.05)  # Determined where to look with the code above to find where super divisible numbers can be found

M = 725760  # Empiric, decreased bit by bit before I wouldn't find more
M = 718200
M = 693000
M = 665280  # Got this upon second submission so not that bad a strategy (???)

for house in range(M-100, M+1):  # Increase range to finally have confidence we do have the max
    d = u.sum_of_divisors(house, primes)

    if d >= target:
        print(house)
        break


# PART 2




