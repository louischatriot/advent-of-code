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
template = lines[0]
rules = [l.split(' -> ') for l in lines[2:]]
rules = {r[0]: r[1] for r in rules}

R = 10
for r in range(0, R):
    to_insert = ''
    for i in range(0, len(template) - 1):
        to_insert += rules[template[i:i+2]]

    new_template = ''
    for i in range(0, len(template) - 1):
        new_template += template[i] + to_insert[i]
    new_template += template[-1]

    template = new_template

_, M = u.most_common(template)
_, m = u.least_common(template)

print(M-m)


# PART 2
template = lines[0]

# Linked list approach is also too slow
# end = [template[-1], None]
# next_node = end
# for c in reversed(template[0:-1]):
    # node = [c, next_node]
    # next_node = node

# start = node

# R = 20
# for r in range(0, R):
    # current = start
    # while current != end:
        # next_one = current[1]

        # key = current[0] + next_one[0]
        # new_node = [rules[key], next_one]
        # current[1] = new_node

        # current = next_one


mem = dict()

def frequencies(pair, rounds):
    if (pair, rounds) in mem:
        return mem[(pair, rounds)]

    if rounds == 0:
        return u.frequencies(pair)

    res = defaultdict(lambda: 0)

    between = rules[pair]
    a, b = pair[0] + between, between + pair[1]
    a, b = frequencies(a, rounds-1), frequencies(b, rounds-1)

    for k, v in a.items():
        res[k] += v

    for k, v in b.items():
        res[k] += v

    res[between] -= 1

    mem[(pair, rounds)] = res

    return res


R = 40

res = defaultdict(lambda: 0)
for c1, c2 in zip(template[0:-1], template[1:]):
    for k, v in frequencies(c1 + c2, R).items():
        res[k] += v

for c in template[1:-1]:
    res[c] -= 1

_, M = u.most_common(res)
_, m = u.least_common(res)
print(M-m)










