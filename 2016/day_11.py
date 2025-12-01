import sys
import re
import u as u
from collections import defaultdict, deque
import math
import itertools
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1 & 2
import time

if is_example:
    start_state = { 'E': 1, 1: {'HM', 'LM'}, 2: {'HG'}, 3: {'LG'}, 4: set() }
    end_state = { 'E': 4, 1: set(), 2: set(), 3: set(), 4: {'HM', 'LM', 'HG', 'LG'} }
else:
    PART_2 = False

    start_state = { 'E': 1, 1: {'PG', 'TG', 'TM', 'MG', 'RG', 'RM', 'CG', 'CM'}, 2: {'PM', 'MM'}, 3: set(), 4: set() }
    end_state = { 'E': 4, 1: set(), 2: set(), 3: set(), 4: {'PG', 'TG', 'TM', 'MG', 'RG', 'RM', 'CG', 'CM', 'PM', 'MM'} }

    if PART_2 is True:
        new_objs = {'EG', 'EM', 'DG', 'DM'}
        start_state[1] = start_state[1].union(new_objs)
        end_state[4] = end_state[4].union(new_objs)

def to_node_name(node):
    res = f"{node['E']}>>>>>"

    for floor in range(1, 5):
        res += '-'.join(sorted(node[floor])) + "=="

    return res

def is_valid(node):
    for floor in range(1, 5):
        objs = node[floor]
        gens, chips = set(), set()
        for obj in objs:
            if obj[1] == 'G':
                gens.add(obj[0])
            else:
                chips.add(obj[0])

        if len(chips) == 0 or len(gens) == 0:
            continue

        if len(chips - gens) > 0:
            return False

    return True

def clone_node(node):
    # return copy.deepcopy(node)  # Leaving this here: deepcopy is freaking slow

    res = { 'E': node['E'] }
    for floor in range(1, 5):
        res[floor] = { o for o in node[floor] }

    return res

def h(node):
    # return 0
    res = 0
    for f in range(1, 4):
        res += len(node[f]) * (4 - f)

    # res -= 10 * len(node[4])

    return res

    # print(node)
    return sum((4 - f) * len(node[f]) for f in range(1, 5))


# Below is a really ugly A star, I really need to fix my string based implementation of PQ
# Using better data types would probably make it much faster


import heapq

class PriorityEntry(object):

    def __init__(self, priority, data):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority



end_name = to_node_name(end_state)
targets = [None, [2], [1, 3], [2, 4], [3]]

visited = dict()
to_visit = []
heapq.heappush(to_visit, PriorityEntry(0, (0, start_state)))



print("=================")

print(end_state)
print(len(end_state[4]))

while True:
    entry = heapq.heappop(to_visit)
    length, node = entry.data

    node_name = to_node_name(node)

    if node_name in visited:
        continue
    visited[node_name] = length

    if node_name == end_name:
        print(length)
        break

    floor = node['E']

    for target_floor in targets[floor]:
        for comb in itertools.chain(itertools.combinations(node[floor], 2), itertools.combinations(node[floor], 1)):
            new_node = dict()
            new_node['E'] = target_floor

            for f in range(1, 5):
                new_node[f] = {o for o in node[f]}

            new_node[floor] = new_node[floor] - set(comb)
            new_node[target_floor] = new_node[target_floor].union(set(comb))

            if is_valid(new_node):
                heapq.heappush(to_visit, PriorityEntry(length + 1 + h(new_node), (length + 1, new_node)))




