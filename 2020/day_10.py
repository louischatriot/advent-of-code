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
adapters = [int(l) for l in lines]
adapters.append(0)
adapters.append(max(adapters) + 3)
adapters = sorted(adapters)
diffs = {1: 0, 2: 0, 3: 0}

for i in range(1, len(adapters)):
    diffs[adapters[i] - adapters[i-1]] += 1

res = diffs[1] * diffs[3]
print(res)


# PART 2
end = adapters[-1]
s_adapters = set(adapters)
# Naive recursive approach works but too slow
def count(start):
    if start == end:
        return 1

    res = 0

    for d in [1, 2, 3]:
        if start + d in s_adapters:
            res += count(start + d)

    return res

# res = count(0)
# print(res)

components = []
current = set()

for n in adapters:
    M = max(current) if len(current) > 0 else 0

    if n == M+3:
        components.append(current)
        current = set()
        current.add(n)
    else:
        current.add(n)

def count(component, start):
    if start == max(component):
        return 1

    res = 0

    for d in [1, 2, 3]:
        if start + d in component:
            res += count(component, start + d)

    return res

res = 1
for component in components:
    res *= count(component, min(component))

print(res)




