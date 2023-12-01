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
res = 0
for l in lines:
    n = ''
    for c in l:
        if '0' <= c <= '9':
            n += c
            break

    for c in reversed(l):
        if '0' <= c <= '9':
            n += c
            break

    res += int(n)

print(res)


# PART 2
digits = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }
res = 0
for l in lines:
    n = ''
    done = False
    for i, c in enumerate(l):
        if '0' <= c <= '9':
            n += c
            break
        else:
            for k, v in digits.items():
                if l[i:i+len(k)] == k:
                    n += v
                    done = True
                    break
        if done:
            break

    done = False
    for i, c in enumerate(reversed(l)):
        if '0' <= c <= '9':
            n += c
            break
        else:
            for k, v in digits.items():
                if l[len(l)-i-1:len(l)-i-1+len(k)] == k:
                    n += v
                    done = True
                    break
        if done:
            break

    res += int(n)

print(res)



