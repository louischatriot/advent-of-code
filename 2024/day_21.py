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
        yield dir, (state[0], *state[1:-1], new_pos)

    # Pressing 'A'
    iz = None
    for i in range(depth, 0, -1):
        if state[i] != 'A':
            iz = i
            break

    if iz is not None:
        if iz > 1:
            if state[iz] in rd_moves[state[iz-1]]:
                yield 'A', state[0:iz-1] + tuple([rd_moves[state[iz-1]][state[iz]]]) + state[iz:]
        else:
            if state[1] in rn_moves[state[0]]:
                yield 'A', tuple([rn_moves[state[0]][state[1]]]) + state[1:]


def moves_between_digits(d_start, d_end, depth):
    start = tuple([d_start] + ['A'] * depth)
    end = tuple([d_end] + ['A'] * depth)

    state = (0, '', start)

    visited = set()
    to_explore = collections.deque()
    to_explore.append(state)

    while to_explore:
        distance, path, state = to_explore.popleft()

        if state in visited:
            continue
        visited.add(state)

        if state == end:
            return path, distance

        for dir, new_state in gen_next_states(state, depth):
            if new_state not in visited:
                to_explore.append((distance+1, path + dir, new_state))


res = 0
current = 'A'
for code in lines:
    moves = 0

    path = ''
    for d1, d2 in u.pairwise(current + code):
        __path, distance = moves_between_digits(d1, d2, 3)
        moves += distance + 1
        path += __path

    current = code[-1]
    res += int(code[0:-1]) * moves

print(res)


# PART 2
# BFS will not cut it this time

moves = {
    'A': { '^': '<', 'v': '<v', '<': 'v<<', '>': 'v' },
    '^': { 'A': '>', 'v': 'v', '<': 'v<', '>': '>v' },
    'v': { 'A': '>^', '^': '^', '<': '<', '>': '>' },
    '<': { 'v': '>', '>': '>>', '^': '>^', 'A': '>>^' },
    '>': { 'A': '^', 'v': '<', '<': '<<', '^': '<^' }
}

moves['A']['<'] = ['v<<', '<v<']
moves['^']['>'] = ['>v', 'v>']
moves['v']['A'] = ['>^', '^>']
moves['<']['A'] = ['>>^', '>^>']
moves['>']['^'] = ['^<', '<^']

import functools

@functools.cache
def receive(seq, depth):

    if depth == 0:
        return len(seq)

    if seq == 'A':
        return 1

    current = 'A'
    res = 0

    for c in seq:
        if current == c:
            res += 1
        else:
            __moves = moves[current][c]
            if type(__moves) == str:
                __moves = [__moves]

            res += min(receive(move + 'A', depth - 1) for move in __moves)
            current = c

    return res



matrix = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]

def get_num_paths(xs, ys, xe, ye, path):
    if (xs, ys) == (xe, ye):
        yield path
        return

    dx = -1 if xe < xs else (1 if xe > xs else 0)
    dy = -1 if ye < ys else (1 if ye > ys else 0)

    if (xs + dx, ys) != (0, 3) and dx != 0:
        for p in get_num_paths(xs + dx, ys, xe, ye, path + ('<' if dx < 0 else '>')):
            yield p

    if (xs, ys + dy) != (0, 3) and dy != 0:
        for p in get_num_paths(xs, ys + dy, xe, ye, path + ('^' if dy < 0 else 'v')):
            yield p


def get_paths_between_digits(d_start, d_end):
    for x, y in itertools.product(range(3), range(4)):
        if matrix[y][x] == d_start:
            xs, ys = x, y
        if matrix[y][x] == d_end:
            xe, ye = x, y

    for path in get_num_paths(xs, ys, xe, ye, ''):
        yield path + 'A'


def get_score(code):
    res = 99999999999999999999999999999999  # Fuck it

    for a, b, c, d in itertools.product(*[get_paths_between_digits(i, j) for i, j in u.pairwise('A' + code)]):
        path = a + b + c + d
        res = min(res, receive(path, 25))

    return res

res = 0
current = 'A'
for code in lines:
    res += int(code[0:-1]) * get_score(code)

print(res)





