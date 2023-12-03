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
def is_part(c):
    return not ('0' <= c <= '9' or c == '.')

numbers = set()
res = 0
for i, l in enumerate(lines):
    j = 0
    while j < len(l):
        if not '0' <= l[j] <= '9':
            j += 1
            continue

        j0 = j
        n = ''
        while j < len(l) and '0' <= l[j] <= '9':
            n += l[j]
            j += 1

        # Here the number is between j0 (incl) and j (excl)
        n = int(n)
        numbers.add(((i, j0), (i, j-1), n))

        if (
            (j0-1 >= 0 and is_part(l[j0 - 1])) or
            (j < len(l) and is_part(l[j])) or
            (i-1 >= 0 and any(   [is_part(lines[i-1][jj]) for jj in range(max(0, j0-1), min(len(l), j+1))   ]  )) or
            (i+1 < len(lines) and any([is_part(lines[i+1][jj]) for jj in range(max(0, j0-1), min(len(l), j+1))  ]  ))
        ):
            res += n

print(res)


# PART 2
res = 0
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == '*':
            adjs = set()

            for di, dj in u.all_neighbours:
                if not ((0 <= i+di < len(lines)) and (0 <= j+dj < len(l))):
                    continue

                for lb, ub, n in numbers:
                    if lb[0] != i+di:
                        continue

                    if lb[1] <= j+dj <= ub[1]:
                        adjs.add(n)

            if len(adjs) == 2:
                res += adjs.pop() * adjs.pop()

print(res)





