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
def next_rd(pos):
    for dir, new_pos in rd_moves[pos].items():
        yield dir, new_pos


    # if pos == '^':
        # yield '>', 'A'
        # yield 'v', 'v'
    # elif pos == 'A':
        # yield '<', '^'
        # yield 'v', '>'
    # elif pos == '<':
        # yield '>', 'v'
    # elif pos == 'v':
        # yield '<', '<'
        # yield '>', '>'
        # yield '^', '^'
    # elif pos == '>':
        # yield '^', 'A'
        # yield '<', 'v'


start = ('A', 'A', 'A')
target = lines[0]
visited = set()
to_explore = collections.deque()
to_explore.append((0, start))

while to_explore:
    distance, state = to_explore.popleft()

    if state in visited:
        continue
    visited.add(state)

    rn, rd1, rd2 = state

    # Just moving the closest robot
    for dir, new_pos in next_rd(rd2):
        new_state = (rn, rd1, new_pos)

        if new_state not in visited:
            to_explore.append((distance+1, new_state))


    # ACTION!





