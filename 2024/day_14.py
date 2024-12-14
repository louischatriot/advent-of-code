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
    lines = [line.rstrip() for line in file]


# PART 1
N, M = 103, 101
if is_example:
    N, M = 7, 11

robots = list()
for line in lines:
    p, v = line.split()
    p = list(map(int, p[2:].split(',')))
    v = list(map(int, v[2:].split(',')))
    robot = { 'p': p, 'v': v }
    robots.append(robot)


def print_robots(robots, N, M):
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    for robot in robots:
        x, y = robot['p']
        matrix[y][x] += 1

    print('')
    print('\n'.join(' '.join(map(lambda n: '.' if n == 0 else str(n), l)) for l in matrix))
    print('')


def double_robots(robots):
    pos = set()
    for robot in robots:
        x, y = robot['p']
        if (x, y) in pos:
            return True

        pos.add((x, y))

    return False


def count_quadrants(robots, N, M):
    qs = [0, 0, 0, 0]
    for robot in robots:
        x, y = robot['p']
        if y < N // 2 and x < M // 2:
            qs[0] += 1

        if y < N // 2 and x > M // 2:
            qs[1] += 1

        if y > N // 2 and x < M // 2:
            qs[2] += 1

        if y > N // 2 and x > M // 2:
            qs[3] += 1

    return qs

steps = 100

for robot in robots:
    x, y = robot['p']
    vx, vy = robot['v']
    x = (x + vx * steps) % M
    y = (y + vy * steps) % N
    robot['p'] = [x, y]

print(math.prod(count_quadrants(robots, N, M)))


# PART 2
counter = steps
steps = 1

while True:
    for robot in robots:
        x, y = robot['p']
        vx, vy = robot['v']
        x = (x + vx * steps) % M
        y = (y + vy * steps) % N
        robot['p'] = [x, y]

    counter += steps

    if not double_robots(robots):  # Seriously AoC WOW
        print(counter)
        print_robots(robots, N, M)
        sys.exit(0)








