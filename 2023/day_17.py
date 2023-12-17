import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import numpy as np

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
matrix = [[int(c) for c in l] for l in lines]
I, J = len(matrix), len(matrix[0])

def node_name(i, j, dir):
    return f"{i}-{j}-{dir}"

dirs = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

next_dirs = {
    'left': ['up', 'down'],
    'right': ['up', 'down'],
    'up': ['left', 'right'],
    'down': ['left', 'right']
}

nodes = set()
edges = defaultdict(lambda: [])

# Set to 0 and 3 for part 1
# Set to 4 and 11 for part 2
MIN_BLOCK = 4
MAX_BLOCK = 11
for i, j in itertools.product(range(I), range(J)):
    for dir, delta in dirs.items():
        di, dj = delta
        _from = node_name(i, j, dir)
        nodes.add(_from)

        distance = 0
        ni, nj = i, j

        for _ in range(1, MIN_BLOCK):
            ni, nj = ni+di, nj+dj
            if not (0 <= ni < I and 0 <= nj < J):
                break
            distance += matrix[ni][nj]

        for _ in range(MIN_BLOCK, MAX_BLOCK):
            ni, nj = ni+di, nj+dj
            if not (0 <= ni < I and 0 <= nj < J):
                break

            distance += matrix[ni][nj]

            for next_dir in next_dirs[dir]:
                _to = node_name(ni, nj, next_dir)
                edges[_from].append((_to, distance))

nodes.add('start')
for dir in dirs:
    edges['start'].append((node_name(0, 0, dir), 0))

nodes.add('end')
for dir in dirs:
    edges[node_name(I-1, J-1, dir)].append(('end', 0))


res = u.do_dijkstra(nodes, edges, 'start', 'end')
print(res)




