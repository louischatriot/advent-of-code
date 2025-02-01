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
data = [int(n) for n in lines[0].split()]

def parse(data):
    if data[0] == 0:
        next_n = data[1]+2
        node = data[0:next_n]
        return (next_n, node)

    node = data[0:2]
    current = 2

    for _ in range(node[0]):
        __data = data[current:]  # Super dirty, should not clone the data and pass an index instead but fast enough here
        next_n, child = parse(__data)
        node.append(child)
        current += next_n

    for i in range(node[1]):
        node.append(data[current])
        current += 1

    return current, node


def get_score(tree):
    res = 0
    for i in range(tree[1]):
        res += tree[-i-1]

    for i in range(tree[0]):
        res += get_score(tree[2+i])

    return res


next_n, tree = parse(data)
res = get_score(tree)
print(res)


# PART 2
def get_value(node):
    if node[0] == 0:
        return sum(node[-i-1] for i in range(node[1]))

    res = 0
    for i in range(node[1]):
        metadata = node[-i-1]
        if metadata <= node[0]:
            res += get_value(node[1+metadata])

    return res

res = get_value(tree)
print(res)






