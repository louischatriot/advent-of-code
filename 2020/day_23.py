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
cups = [int(c) for c in lines[0]]
L = len(cups)
ci = 0


# Keep current left of list, makes everything simpler
cups = cups[ci:] + cups[0:ci]


def play_rounds(cups, rounds):
    for _ in range(0,rounds):
        current = cups[0]
        pickup = cups[1:4]

        if current == 1:
            destination = max(cups)
        else:
            destination = current - 1

        for _ in range(0, 3):
            if destination in pickup:
                destination = destination - 1
                if destination == 0:
                    destination = max(cups)

        di = cups.index(destination)
        cups = [current] + cups[4:di+1] + pickup + cups[di+1:]

        ci = 1
        cups = cups[ci:] + cups[0:ci]

    return cups


cups = play_rounds(cups, 100)
pivot = cups.index(1)
cups = cups[pivot:] + cups[0:pivot]

res = ''.join([str(c) for c in cups[1:]])
print(res)


# PART 2
# As expected this is way too slow
# cups = [int(c) for c in lines[0]] + [n for n in range(10, 1000001)]
# L = len(cups)
# ci = 0
# cups = cups[ci:] + cups[0:ci]
# cups = play_rounds(cups, 10000000)

def print_chain(chain, length):
    res = ''
    current = chain

    for _ in range(0, length):
        res += str(current[0]) + ' - '
        current = current[2]

    print("CHAIN ", res)



N = 1000000
# N = 20
# N = 9
nodes = dict()
all_nodes = [int(c) for c in lines[0]] + [n for n in range(len(lines[0])+1, N+1)]

previous_node = [all_nodes[0], None, None]
first_node = previous_node
nodes[all_nodes[0]] = first_node

for n in all_nodes[1:]:
    node = [n, previous_node, None]
    nodes[n] = node

    previous_node[2] = node
    node[1] = previous_node
    previous_node = node

previous_node[2] = first_node
first_node[1] = previous_node

# First current node is the first in the list
current = nodes[all_nodes[0]]

for _ in range(0, 10000000):
    pickup = [current[2][0], current[2][2][0], current[2][2][2][0]]
    pickup_start = current[2]
    pickup_end = current[2][2][2]
    after_pickup = current[2][2][2][2]

    dest_n = current[0]
    while dest_n in [current[0]] + pickup:
        dest_n -= 1
        if dest_n == 0:
            dest_n = N

    destination = nodes[dest_n]
    after_destination = destination[2]

    # Repair the chain
    current[2] = after_pickup
    after_pickup[1] = current

    destination[2] = pickup_start
    pickup_start[1] = destination
    pickup_end[2] = after_destination
    after_destination[1] = pickup_end

    current = current[2]


print_chain(nodes[1], 5)




