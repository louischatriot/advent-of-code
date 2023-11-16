import sys
import re
import u as u
from collections import defaultdict

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]

# PART 1
preamble = 5 if is_example else 25
numbers = [int(l) for l in lines]
res = None
for i in range(preamble, len(numbers)):
    if all(numbers[i] != numbers[i-d1] + numbers[i-d2] for d1 in range(1, preamble+1) for d2 in range(d1+1, preamble+1)):
        res = numbers[i]

print(res)


# PART 2
invalid = res
MAX = max(numbers) + 1
for i in range(0, len(numbers)):
    m = MAX
    M = -1
    c = invalid

    for j in range(i, len(numbers)):
        n = numbers[j]
        c -= n
        m = min(m, n)
        M = max(M, n)
        if c == 0:
            print(m+M)
            sys.exit(0)

        if c < 0:
            break



