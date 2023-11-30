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
rooms = [[] for _ in range(0, 4)]

for i in [3, 2]:
    l = lines[i]
    l = l.replace(' ', '')
    if len(l) > 9:
        l = l[2:-2]
    l = l[1:-1].split('#')

    for idx, amph in enumerate(l):
        rooms[idx].append(amph)

start_node = '-'.join([''.join(r) for r in rooms]) + '-.......'

target_idxs = { 'A': 0, 'B': 1, 'C': 2, 'D': 3 }
energies = { 'A': 1, 'B': 10, 'C': 100, 'D': 1000 }
N_ROOMS = 4

def get_room(node, idx, depth):
    return node[3 * idx + depth]

def get_hallway(node, hw_dest):
    return node[12 + hw_dest]

# node is not modified by setter functions
def set_room(node, idx, depth, value):
    point = 3 * idx + depth
    res = node[0:point] + value + node[point+1:]
    return res

def set_hallway(node, hw_dest, value):
    point = 12 + hw_dest
    res = node[0:point] + value + node[point+1:]
    return res

def distance(room_idx, room_depth, hw_dest):
    d = 2 - room_depth  # Moving to the hallway

    if hw_dest - 1 <= room_idx:  # Going left
        if hw_dest == 0:
            d -= 1

        d += 1 + 2 * (room_idx + 1 - hw_dest)

    else:
        if hw_dest == 6:
            d -= 1

        d += 1 + 2 * (hw_dest - room_idx - 2)

    return d


nodes = set()
nodes_to_do = set()
edges = defaultdict(lambda: [])

nodes_to_do.add(start_node)
end_state = 'AA-BB-CC-DD-.......'

while len(nodes_to_do) > 0:
    node = nodes_to_do.pop()

    if node in nodes:
        continue

    nodes.add(node)
    if node == end_state:
        continue

    # Hallway to destination room moves (always optimal)
    for hw in range(0, 7):
        amph = get_hallway(node, hw)

        if amph == '.':
            continue

        idx = target_idxs[amph]
        depth = 0 if get_room(node, idx, 0) == '.' else 1

        if depth == 1 and get_room(node, idx, 0) != amph:  # An amphipod is already in the room but it's not his destination
            continue

        if (
            (hw <= idx + 1 and all(get_hallway(node, hw_mid) == '.' for hw_mid in range(hw+1, idx+2))) or
            (hw > idx + 1 and all(get_hallway(node, hw_mid) == '.' for hw_mid in range(idx+2, hw)))
        ):
                new_state = set_hallway(node, hw, '.')
                new_state = set_room(new_state, idx, depth, amph)

                if new_state not in nodes:
                    nodes_to_do.add(new_state)

                d = distance(idx, depth, hw)
                edges[node].append((new_state, d * energies[amph]))


    # Leaving the rooms
    for idx in range(0, N_ROOMS):
        if get_room(node, idx, 0) == '.':  # Empty room
            continue

        # Can only move the top amphipod
        depth = 0 if get_room(node, idx, 1) == '.' else 1

        amph = get_room(node, idx, depth)

        # Already reached its destination? Attention if it's the shallow one need to check deep one also reached destination
        if target_idxs[amph] == idx:
            if depth == 0:
                continue
            else:
                if target_idxs[get_room(node, idx, 0)] == idx:
                    continue

        # Move to the hallway left
        hw_dest = idx + 1
        while hw_dest >= 0:
            if get_hallway(node, hw_dest) != '.':  # Can't move left further
                break

            new_state = set_hallway(node, hw_dest, amph)
            new_state = set_room(new_state, idx, depth, '.')

            if new_state not in nodes:
                nodes_to_do.add(new_state)

            d = distance(idx, depth, hw_dest)
            edges[node].append((new_state, d * energies[amph]))

            hw_dest -= 1

        # Move to the hallway right
        hw_dest = idx + 2
        while hw_dest <= 6:
            if get_hallway(node, hw_dest) != '.':  # Can't move right further
                break

            new_state = set_hallway(node, hw_dest, amph)
            new_state = set_room(new_state, idx, depth, '.')

            if new_state not in nodes:
                nodes_to_do.add(new_state)

            d = distance(idx, depth, hw_dest)
            edges[node].append((new_state, d * energies[amph]))

            hw_dest += 1


print(f"GRAPH BUILT {len(nodes)} nodes")
res = u.do_dijkstra(nodes, edges, start_node, 'AA-BB-CC-DD-.......')
print(res)


# PART 2
start_node = start_node[0] + 'DD' + start_node[1:4] + 'BC' + start_node[4:7] + 'AB' + start_node[7:10] + 'CA' + start_node[10:]

test_node = 'ABCD-EFGH-IJKL-MNOP-ZYXWVUT'

def get_room(node, idx, depth):
    return node[5 * idx + depth]

def get_hallway(node, hw_dest):
    return node[20 + hw_dest]

# node is not modified by setter functions
def set_room(node, idx, depth, value):
    point = 5 * idx + depth
    res = node[0:point] + value + node[point+1:]
    return res

def set_hallway(node, hw_dest, value):
    point = 20 + hw_dest
    res = node[0:point] + value + node[point+1:]
    return res

def distance(room_idx, room_depth, hw_dest):
    d = 4 - room_depth  # Moving to the hallway

    if hw_dest - 1 <= room_idx:  # Going left
        if hw_dest == 0:
            d -= 1

        d += 1 + 2 * (room_idx + 1 - hw_dest)

    else:
        if hw_dest == 6:
            d -= 1

        d += 1 + 2 * (hw_dest - room_idx - 2)

    return d


"""
# 0 1 _ 2 _ 3 _ 4 _ 5 6
#     0   1   2   3
# # # # # # # # # # # # #
# . . . . . . . . . . . #
# # # B # C # B # D # # #
    # A # D # C # A #
    # # # # # # # # #
  . . . . . . . . . . . #
"""


nodes = set()
nodes_to_do = set()
edges = defaultdict(lambda: [])

nodes_to_do.add(start_node)
end_state = 'AAAA-BBBB-CCCC-DDDD-.......'

while len(nodes_to_do) > 0:
    node = nodes_to_do.pop()

    if node in nodes:
        continue

    nodes.add(node)
    if node == end_state:
        continue

    # Hallway to destination room moves (always optimal)
    for hw in range(0, 7):
        amph = get_hallway(node, hw)

        if amph == '.':
            continue

        idx = target_idxs[amph]

        depth = None
        for dep in range(0, 4):
            if get_room(node, idx, dep) == '.':
                depth = dep
                break
            elif get_room(node, idx, dep) != amph:
                break

        if depth is None:  # Either the room is full, or it is not but there is a non-destination amphipod
            continue

        if (
            (hw <= idx + 1 and all(get_hallway(node, hw_mid) == '.' for hw_mid in range(hw+1, idx+2))) or
            (hw > idx + 1 and all(get_hallway(node, hw_mid) == '.' for hw_mid in range(idx+2, hw)))
        ):
                new_state = set_hallway(node, hw, '.')
                new_state = set_room(new_state, idx, depth, amph)

                if new_state not in nodes:
                    nodes_to_do.add(new_state)

                d = distance(idx, depth, hw)
                edges[node].append((new_state, d * energies[amph]))


    # Leaving the rooms
    for idx in range(0, N_ROOMS):
        if get_room(node, idx, 0) == '.':  # Empty room
            continue

        # Can only move the top amphipod
        depth = None
        for dep in range(3, -1, -1):
            if get_room(node, idx, dep) != '.':
                depth = dep
                break

        amph = get_room(node, idx, depth)

        # Already reached its destination? Attention, deeper ones need to be correct or this one needs to move
        if target_idxs[amph] == idx:
            if depth == 0:
                continue
            else:
                if all([target_idxs[get_room(node, idx, dep)] == idx for dep in range(0, depth)]):
                    continue

        # Move to the hallway left
        hw_dest = idx + 1
        while hw_dest >= 0:
            if get_hallway(node, hw_dest) != '.':  # Can't move left further
                break

            new_state = set_hallway(node, hw_dest, amph)
            new_state = set_room(new_state, idx, depth, '.')

            if new_state not in nodes:
                nodes_to_do.add(new_state)

            d = distance(idx, depth, hw_dest)
            edges[node].append((new_state, d * energies[amph]))

            hw_dest -= 1

        # Move to the hallway right
        hw_dest = idx + 2
        while hw_dest <= 6:
            if get_hallway(node, hw_dest) != '.':  # Can't move right further
                break

            new_state = set_hallway(node, hw_dest, amph)
            new_state = set_room(new_state, idx, depth, '.')

            if new_state not in nodes:
                nodes_to_do.add(new_state)

            d = distance(idx, depth, hw_dest)
            edges[node].append((new_state, d * energies[amph]))

            hw_dest += 1

print(f"GRAPH BUILT {len(nodes)} nodes")
res = u.do_dijkstra(nodes, edges, start_node, end_state)
print(res)



