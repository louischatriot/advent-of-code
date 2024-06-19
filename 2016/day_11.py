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
import copy
import time

if is_example:
    start_state = { 'E': 1, 1: {'HM', 'LM'}, 2: {'HG'}, 3: {'LG'}, 4: set() }
    end_state = { 'E': 4, 1: set(), 2: set(), 3: set(), 4: {'HM', 'LM', 'HG', 'LG'} }
else:
    PART_2 = True

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
    return sum((4 - f) * len(node[f]) for f in range(1, 5))


# Below is a really ugly A star, I really need to fix my string based implementation of PQ
end_name = to_node_name(end_state)
targets = [None, [2], [1, 3], [2, 4], [3]]

s = time.time()
print("===================================")


visited = dict()
to_visit = u.PriorityQueue()
to_visit.add_task(f"{to_node_name(start_state)}|||||0", 0)

while True:
    task, priority = to_visit.pop_task()
    node_name, length = task.split('|||||')
    length = int(length)

    if node_name in visited:
        continue
    visited[node_name] = length

    if node_name == end_name:
        print(length)
        print(time.time() - s)
        break

    floor, floors = node_name.split('>>>>>')
    floor = int(floor)
    floors = floors.split('==')[0:4]
    floors = [None] + [set(f.split('-')) if len(f) > 0 else set() for f in floors]

    for target_floor in targets[floor]:
        for comb in itertools.chain(itertools.combinations(floors[floor], 2), itertools.combinations(floors[floor], 1)):
            new_node = dict()
            new_node['E'] = target_floor

            for f in range(1, 5):
                new_node[f] = {o for o in floors[f]}

            new_node[floor] = new_node[floor] - set(comb)
            new_node[target_floor] = new_node[target_floor].union(set(comb))

            if is_valid(new_node):
                to_visit.add_task(f"{to_node_name(new_node)}|||||{length + 1}", length + 1 + h(new_node))




