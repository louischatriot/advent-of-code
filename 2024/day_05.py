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
rules = set()
orderings = list()
do_ordering = False

for line in lines:
    if line == '':
        do_ordering = True
        continue

    if do_ordering:
        orderings.append(list(map(int, line.split(','))))
    else:
        rules.add(line)

# I knew this would be badly inefficient but it turned out to be even worse than expected, see below alternative
# def reorder(ordering, rules):
    # N = len(ordering)

    # for i in range(N-1):
        # for j in range(i+1, N):
            # n, m = ordering[i], ordering[j]

            # if f"{m}|{n}" in rules:
                # return reorder(ordering[0:i] + [m] + ordering[i+1:j] + [n] + ordering[j+1:], rules)

    # return ordering


# More efficient approach below
import functools
def reorder(ordering, rules):
    return sorted(ordering, key=functools.cmp_to_key(lambda a, b: -1 if f"{a}|{b}" in rules else 1))


res1 = 0
res2 = 0

# So inefficient!
for ordering in orderings:
    reordered = reorder(ordering, rules)

    if ''.join(map(str, reordered)) == ''.join(map(str, ordering)):
        res1 += ordering[len(ordering) // 2]
    else:
        res2 += reordered[len(reordered) // 2]


    # Ugh ...
    # ok = True

    # for i, n in enumerate(ordering[0:-1]):
        # for m in ordering[i+1:]:
            # if f"{m}|{n}" in rules:
                # ok = False

    # if ok:
        # res1 += ordering[len(ordering) // 2]
    # else:
        # reordered = reorder(ordering, rules)
        # res2 += reordered[len(reordered) // 2]

print(res1)
print(res2)



