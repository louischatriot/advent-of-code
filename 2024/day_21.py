import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import collections
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
rd_moves = {  # { pos: { dir: new_pos } }
    '^': { '>': 'A', 'v': 'v' },
    'A': { '<': '^', 'v': '>' },
    '<': { '>': 'v' },
    'v': { '<': '<', '^': '^', '>': '>' },
    '>': { '^': 'A', '<': 'v' }
}

rn_moves = {
    '7': { '>': '8', 'v': '4' },
    '8': { '<': '7', '>': '9', 'v': '5' },
    '9': { '<': '8', 'v': '6' },
    '4': { '^': '7', 'v': '1', '>': '5' },
    '5': { '<': '4', '>': '6', '^': '8', 'v': '2' },
    '6': { '^': '9', 'v': '3', '<': '5' },
    '1': { '^': '4', '>': '2' },
    '2': { '<': '1', '>': '3', '^': '5', 'v': '0' },
    '3': { '^': '6', 'v': 'A', '<': '2' },
    '0': { '^': '2', '>': 'A' },
    'A': { '<': '0', '^': '3' }
}

# Yields dir, new_pos
def nexts(moves, pos):
    for dir, new_pos in moves[pos].items():
        yield dir, new_pos


start = ('A', 'A', 'A')
target = lines[0]
visited = set()
to_explore = collections.deque()
to_explore.append((0, start))
end = ('0', 'A', 'A')

def gen_next_states(state):
    pos0, pos1, pos2 = state

    # Moving robot 2
    for dir, new_pos2 in nexts(rd_moves, pos2):
        yield (pos0, pos1, new_pos2)

    # Press 'A', moving robot 1
    if pos2 != 'A':
        if pos2 in rd_moves[pos1]:
            yield (pos0, rd_moves[pos1][pos2], pos2)

    # Press 'A', moving robot 0
    if pos2 == 'A' and pos1 != 'A':
        if pos1 in rn_moves[pos0]:
            yield (rn_moves[pos0][pos1], pos1, pos2)


while to_explore:
    distance, state = to_explore.popleft()

    if state in visited:
        continue
    visited.add(state)

    if state == end:
        print(distance)
        1/0

    for new_state in gen_next_states(state):
        if new_state not in visited:
            to_explore.append((distance+1, new_state))













