import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line[0:-1] for line in file]


# PART 1
carts_shapes = ['>', '<', 'v', '^']
under_start = { '>': '-', '<': '-', '^': '|', 'v': '|' }

left_next = { '>': '^', '^': '<', '<': 'v', 'v': '>' }
right_next = { v: k for k, v in left_next.items() }
straight_next = { '>': '>', '<': '<', '^': '^', 'v': 'v' }
__next = [left_next, straight_next, right_next]

def turn(cart):
    _, _, dir, cycle = cart
    cart[2] = __next[cycle % 3][dir]
    cycle += 1

corners = ['/', '\\']
corners_next = {
    '/': { '>': '^', '^': '>', '<': 'v', 'v': '<'},
    '\\': { '>': 'v', 'v': '>', '<': '^', '^': '<' }
}

movements = { '>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0) }

N, M = len(lines), len(lines[0])
matrix = []
carts = list()

for y in range(N):
    line = lines[y]
    l = list()

    for x in range(M):
        c = line[x]
        if c in carts_shapes:
            carts.append([y, x, c, 0])
            c = under_start[c]

        l.append(c)

    matrix.append(l)


def print_everything(matrix, carts):
    __carts = dict()
    for y, x, d, _ in carts:
        __carts[(y, x)] = d

    print("=============================================")
    for y in range(N):
        l = list()
        for x in range(M):
            c = matrix[y][x] if (y, x) not in __carts else __carts[(y, x)]
            l.append(c)

        print(''.join(l))

    print("=============================================")



print_everything(matrix, carts)






