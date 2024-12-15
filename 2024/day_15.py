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
doing_robots = True
matrix = list()
instructions = ''

for line in lines:
    if line == '':
        doing_robots = False
        continue

    if doing_robots:
        matrix.append(line)
    else:
        instructions += line

walls = set()
boxes = set()
robot = (None, None)
N, M = len(matrix), len(matrix[0])
for i, l in enumerate(matrix):
    for j, c in enumerate(l):
        if c == '@':
            robot = (i, j)
        elif c == '#':
            walls.add((i, j))
        elif c == 'O':
            boxes.add((i, j))

def print_matrix(N, M, walls, boxes, robot, expanded = False):
    matrix = [['.' for _ in range(M)] for _ in range(N)]
    for i, j in walls:
        matrix[i][j] = '#'
    for i, j in boxes:
        if expanded:
            matrix[i][j] = '['
            matrix[i][j+1] = ']'
        else:
            matrix[i][j] = 'O'

    matrix[robot[0]][robot[1]] = '@'

    print('')
    for l in matrix:
        print(' '.join(l))
    print('')


for c in instructions:
    di, dj = u.directions[c]
    i, j = robot
    first = (i + di, j + dj)
    last = None

    if first not in walls and first not in boxes:
        robot = first
        continue

    while True:
        i, j = i+di, j+dj
        if (i, j) in walls:
            last = None
            break
        elif (i, j) in boxes:
            pass
        else:  # Empty
            last = (i, j)
            break

    if last:
        robot = first
        boxes.remove(first)
        boxes.add(last)


res = sum(100 * i + j for i, j in boxes)
print(res)


# PART 2 - Set approach is a pain here, let's switch to matrix
# Lots of ugly boilerplate below ...
walls = set()
boxes = set()
robot = (None, None)
N, M = len(matrix), len(matrix[0])
for i, l in enumerate(matrix):
    for j, c in enumerate(l):
        if c == '@':
            robot = (i, j)
        elif c == '#':
            walls.add((i, j))
        elif c == 'O':
            boxes.add((i, j))

print_matrix(N, M, walls, boxes, robot)

M = M * 2
new_walls = set()
for i, j in walls:
    new_walls.add((i, 2 * j))
    new_walls.add((i, 2 * j + 1))
walls = new_walls

new_boxes = set()
for i, j in boxes:
    new_boxes.add((i, 2 * j))
boxes = new_boxes

robot = (robot[0], 2 * robot[1])

matrix = [['.' for _ in range(M)] for _ in range(N)]
for i, j in walls:
    matrix[i][j] = '#'
for i, j in boxes:
    matrix[i][j] = '['
    matrix[i][j+1] = ']'

matrix[robot[0]][robot[1]] = '@'

def new_print_matrix(matrix):
    print('')
    for l in matrix:
        print(' '.join(l))
    print('')


new_print_matrix(matrix)

for c in instructions:
    di, dj = u.directions[c]
    i, j = robot

    if matrix[i+di][j+dj] == '.':
        robot = (i+di, j+dj)
        matrix[i][j] = '.'
        matrix[i+di][j+dj] = '@'
        continue

    if matrix[i+di][j+dj] == '#':
        continue

    if di == 0:
        jt = j
        while True:
            i, j = i+di, j+dj
            if matrix[i][j] == '#':
                jt = None
                break
            elif matrix[i][j] == '.':
                jt = j
                break

        if jt is not None:
            for __j in range(jt, robot[1], -dj):
                matrix[i][__j] = matrix[i][__j-dj]

            matrix[i][robot[1]] = '.'
            robot = (i, robot[1]+dj)

        continue

    # Moving stuff vertically
    to_move = set()
    frontier = collections.deque()

    if matrix[i+di][j] == '[':
        to_move.add((i+di, j))
        frontier.append((i+di, j))
        frontier.append((i+di, j+1))


    elif matrix[i+di][j] == ']':
        to_move.add((i+di, j-1))
        frontier.append((i+di, j-1))
        frontier.append((i+di, j))

    else:
        raise ValueError("wat")

    while frontier:
        i, j = frontier.popleft()

        if matrix[i+di][j] == '[':
            to_move.add((i+di, j))
            frontier.append((i+di, j))
            frontier.append((i+di, j+1))

        elif matrix[i+di][j] == ']':
            to_move.add((i+di, j-1))
            frontier.append((i+di, j-1))
            frontier.append((i+di, j))

        elif matrix[i+di][j] == '#':
            to_move = set()
            break

    if to_move:
        for i, j in to_move:
            matrix[i][j] = '.'
            matrix[i][j+1] = '.'

        for i, j in to_move:
            matrix[i+di][j] = '['
            matrix[i+di][j+1] = ']'

        matrix[robot[0]][robot[1]] = '.'
        matrix[robot[0]+di][robot[1]] = '@'
        robot = (robot[0]+di, robot[1])



res = 0
for i, j in itertools.product(range(N), range(M)):
    if matrix[i][j] == '[':
        res += 100 * i + j

print(res)




