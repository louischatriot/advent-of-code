import sys
import re
import u as u
from collections import defaultdict
import math

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
gamma, epsilon, p = 0, 0, 0
for j in reversed(range(0, len(lines[0]))):
    ones, zeroes = 0, 0
    for l in lines:
        if l[j] == '1':
            ones += 1
        else:
            zeroes += 1

    if ones > zeroes:
        gamma += 2**p
    else:
        epsilon += 2**p

    p += 1

print(gamma * epsilon)


# PART 2
oxygen = [l for l in lines]
for j in range(0, len(lines[0])):
    ones, zeroes = 0, 0
    for l in oxygen:
        if l[j] == '1':
            ones += 1
        else:
            zeroes += 1

    if ones >= zeroes:
        oxygen = [l for l in oxygen if l[j] == '1']
    else:
        oxygen = [l for l in oxygen if l[j] == '0']

    if len(oxygen) == 1:
        break

co2 = [l for l in lines]
for j in range(0, len(lines[0])):
    ones, zeroes = 0, 0
    for l in co2:
        if l[j] == '1':
            ones += 1
        else:
            zeroes += 1

    if zeroes <= ones:
        co2 = [l for l in co2 if l[j] == '0']
    else:
        co2 = [l for l in co2 if l[j] == '1']

    if len(co2) == 1:
        break

no, nc = 0, 0
for idx, c in enumerate(reversed(oxygen[0])):
    if c == '1':
        no += 2**idx
for idx, c in enumerate(reversed(co2[0])):
    if c == '1':
        nc += 2**idx

print(no * nc)






