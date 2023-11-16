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
bp = re.compile('^([a-z ]+) bags contain ([a-z ,0-9]+)\.$')
cp = re.compile('^([0-9]+) ([a-z ]+) bags?$')
bags = dict()

for l in lines:
    if l[-28:] == ' bags contain no other bags.':
        bags[l[0:-28]] = dict()
        continue

    m = bp.match(l)
    bag = m[1]
    bags[bag] = dict()

    for contents in m[2].split(', '):
        mc = cp.match(contents)
        bags[bag][mc[2]] = int(mc[1])

full_bags = dict()
res = 0
for bag, stuff in bags.items():
    contents = defaultdict(lambda: 0)
    todo = [(bag, 1)]

    while len(todo) > 0:
        k, v = todo[0]
        todo = todo[1:]

        contents[k] += v

        for kk, vv in bags[k].items():
            todo.append((kk, vv * v))

    # Just in case
    full_bags[bag] = contents

    if 'shiny gold' in contents:
        res += 1

print(res - 1)  # Not counting the shiny gold bag itself


# PART 2
contents = full_bags['shiny gold']  # I knew it would be useful :)
res = sum(v for _, v in contents.items()) - 1  # Removing the shiny gold bag itself
print(res)







