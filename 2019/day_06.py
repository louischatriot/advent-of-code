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
nodes = dict()
for l in lines:
    parent_name, child_name = l.split(')')

    if parent_name in nodes:
        parent = nodes[parent_name]
    else:
        parent = [parent_name, None]
        nodes[parent_name] = parent

    if child_name in nodes:
        child = nodes[child_name]
    else:
        child = [child_name, None]
        nodes[child_name] = child

    child[1] = parent

def n_links(node):
    if node[1] is None:
        return 0

    return 1 + n_links(node[1])

res = 0
for _, node in nodes.items():
    res += n_links(node)

print(res)


# PART 2
def get_path(node):
    if node[1] is None:
        return [node[0]]

    return get_path(node[1]) + [node[0]]

pyou = get_path(nodes['YOU'])
psan = get_path(nodes['SAN'])

i = 0
for y, s in zip(pyou, psan):
    if y == s:
        i+= 1
    else:
        break

res = len(pyou) + len(psan) - 2 * i - 2
print(res)



