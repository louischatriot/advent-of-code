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


def gen_next_states(state, depth):
    # Moving last robot
    for dir, new_pos in nexts(rd_moves, state[-1]):
        yield (state[0], *state[1:-1], new_pos)

    # Pressing 'A'
    iz = None
    for i in range(depth, 0, -1):
        if state[i] != 'A':
            iz = i
            break

    if iz is not None:
        if iz > 1:

            if state[iz] in rd_moves[state[iz-1]]:
                yield state[0:iz-1] + tuple([rd_moves[state[iz-1]][state[iz]]]) + state[iz:]
        else:
            if state[1] in rn_moves[state[0]]:
                yield tuple([rn_moves[state[0]][state[1]]]) + state[1:]


def moves_between_digits(d_start, d_end, depth):
    start = tuple([d_start] + ['A'] * depth)
    end = tuple([d_end] + ['A'] * depth)

    visited = set()
    to_explore = collections.deque()
    to_explore.append((0, start))

    while to_explore:
        distance, state = to_explore.popleft()

        if state in visited:
            continue
        visited.add(state)

        if state == end:
            return distance

        for new_state in gen_next_states(state, depth):
            if new_state not in visited:
                to_explore.append((distance+1, new_state))


res = 0
current = 'A'
for code in lines:
    moves = 0

    for d1, d2 in u.pairwise(current + code):
        moves += moves_between_digits(d1, d2, 2) + 1

    current = code[-1]
    res += int(code[0:-1]) * moves

print(res)


# PART 2
# BFS will not cut it this time

matrix = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]

def moves_between_digits(d_start, d_end):
    for x, y in itertools.product(range(3), range(4)):
        if matrix[y][x] == d_start:
            xs, ys = x, y
        if matrix[y][x] == d_end:
            xe, ye = x, y

    if ys == ye:
        d = '<' * (xs - xe) if xs > xe else '>' * (xe - xs)
    elif ys > ye:
        d = '^' * (ys - ye)
        d += '<' * (xs - xe) if xs > xe else '>' * (xe - xs)
    else:
        if xs < xe:
            d = '>' * (xe - xs) + 'v' * (ye - ys)
        else:
            d = 'v' * (ye - ys) + '<' * (xs - xe)





    print(d)




moves_between_digits('6', '0')









