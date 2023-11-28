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


# 0 1 _ 2 _ 3 _ 4 _ 5 6
#     0   1   2   3
# # # # # # # # # # # # #
# . . . . . . . . . . . #
# # # B # C # B # D # # #
    # A # D # C # A #
    # # # # # # # # #




# PART 1
rooms = [[] for _ in range(0, 4)]

for i in [3, 2]:
    l = lines[i]
    l = l.replace(' ', '')
    if len(l) > 9:
        l = l[2:-2]
    l = l[1:-1].split('#')

    for idx, amph in enumerate(l):
        rooms[idx].append(amph)

start_node = '-'.join([''.join(r) for r in rooms]) + '-WXCVBNM'   # '-.......'
nodes = set()
nodes_to_do = [start_node]
edges = dict()


print(start_node)

target_idxs = { 'A': 0, 'B': 1, 'C': 2, 'D': 3 }

def get_room(node, idx, depth):
    return node[3 * idx + depth]

def get_hallway(node, hw_dest):
    return node[12 + hw_dest]

def set_room(node, idx, depth, value):
    node[3 * idx + depth] = value
    return node

def set_hallway(node, hw_dest, value):
    node[12 + hw_dest] = value
    return node





1/0


while len(nodes_to_do) > 0:
    node, nodes_to_do = nodes_to_do[0], nodes_to_do[1:]

    nodes.add(node)
    rooms, hallway = node[0:11].split('-'), node[12:]

    for idx, r in enumerate(rooms):
        if r[0] == '.':  # Empty room
            continue

        if r[1] == '.':  # Deep one can move
            if target_idxs[r[1]] == idx:  # Already in place
                continue

            # Move into hallway
            hw_dest = idx + 1
            while hw_dest >= 0:
                if hallway[hw_dest] != '.':  # Can't move left further
                    break

                new_state = 5

                hw_dest -= 1
















