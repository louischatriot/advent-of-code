import sys
import re
import u as u
from collections import defaultdict
import math
import itertools

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
from intcode import Computer
program = [int(n) for n in lines[0].split(',')]
computer = Computer(program)

directions = {
    (0, -1): 1,
    (0, 1): 2,
    (-1, 0): 3,
    (1, 0): 4
}

opposite = {
    (0, -1): 2,
    (0, 1): 1,
    (-1, 0): 4,
    (1, 0): 3
}

def explore(node, explored):
    x, y = node

    for dx, dy in u.ortho_neighbours:
        xt, yt = x+dx, y+dy

        if (xt, yt) in explored:
            continue

        dir = directions[(dx, dy)]
        computer.run_until_input(dir)
        res = computer.run_until_output()

        if res == 2:
            explored[(xt, yt)] = 'O'
        elif res == 1:
            explored[(xt, yt)] = '.'
        elif res == 0:
            explored[(xt, yt)] = 'X'
        else:
            raise ValueError("Unexpected result")



        if res != 0:  # Robot moved, get it back at starting point
            explore((xt, yt), explored)

            dir = opposite[(dx, dy)]
            computer.run_until_input(dir)
            computer.run_until_output()  # Don't care about output


explored = dict()
explored[(0, 0)] = 'S'
explore((0, 0), explored)

"""
# Uncomment to get a nice map of the maze
mx, Mx, my, My = 9999999, -9999999, 9999999, -9999999
for x, y in explored:
    mx, Mx, my, My = min(mx, x), max(Mx, x), min(my, y), max(My, y)

matrix = [['.' for _ in range(mx, Mx+1)] for _ in range(my, My+1)]

for node, v in explored.items():
    x, y = node
    matrix[y-my][x-mx] = v

for l in matrix:
    print(' '.join(l))
"""

# Given the shape of the labyrinth I could get the distance using the recursion above
# but in the general case that does not work so let's do a BFS

xo, yo = None, None
for node, v in explored.items():
    if v == 'O':
        xo, yo = node

distances = dict()
distances[(0, 0)] = 0
to_explore = list()
to_explore.append((0, 0))

while len(to_explore) > 0:
    x, y = to_explore.pop(0)
    d = distances[(x, y)]

    for dx, dy in u.ortho_neighbours:
        xt, yt = x+dx, y+dy
        if (xt, yt) in distances or explored[(xt, yt)] == 'X':
            continue

        distances[(xt, yt)] = d + 1
        to_explore.append((xt, yt))

print(distances[(xo, yo)])


# PART 2
minutes = 0
empties = set()
for node, v in explored.items():
    if v == '.':
        empties.add(node)

to_explore = set()
to_explore.add((xo, yo))

while len(to_explore) > 0:
    new_to_explore = set()

    while len(to_explore) > 0:
        x, y = to_explore.pop()

        for dx, dy in u.ortho_neighbours:
            xt, yt = x+dx, y+dy
            if (xt, yt) in empties:
                new_to_explore.add((xt, yt))
                empties.remove((xt, yt))

    # print(new_to_explore)
    if len(new_to_explore) > 0:
        minutes += 1

    to_explore = new_to_explore

print(minutes)






