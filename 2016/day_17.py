import sys
import re
import u as u
from collections import defaultdict, deque
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
passcode = lines[0]
start_name = '|0-0'
N = 3

def h(x, y):
    return 2 * N - x - y

visited = dict()
to_visit = u.PriorityQueue()
to_visit.add_task(start_name, 0)

while True:
    task, priority = to_visit.pop_task()
    path, coords = task.split('|')
    x, y = coords.split('-')
    x, y = int(x), int(y)

    if x == N and y == N:
        print(path)
        sys.exit(0)

    hash = u.generate_md5(passcode + path)

    for dx, dy, dir, c in zip([-1, 1, 0, 0], [0, 0, -1, 1], ['U', 'D', 'L', 'R'], hash[0:4]):
        if 0 <= x + dx <= N and 0 <= y + dy <= N and 'b' <= c <= 'f':
            to_visit.add_task(f"{path}{dir}|{x+dx}-{y+dy}", len(path) + 1 + h(x+dx, y+dy))

