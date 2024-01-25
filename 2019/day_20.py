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
portals = dict()
portal_names = set()

def add_portal(portals, name, i, j):
    key = f"{name}-1"
    if key in portals:
        key = f"{name}-2"

    portals[key] = (i, j)

    if name not in ['AA', 'ZZ']:
        portal_names.add(name)

left = re.compile('[A-Z]{2}\.')
right = re.compile('\.[A-Z]{2}')

for i, l in enumerate(lines):
    for m in left.finditer(l):
        add_portal(portals, m.group()[0:2], i, m.start() + 2)

    for m in right.finditer(l):
        add_portal(portals, m.group()[1:], i, m.start())

def get_matrix_from_lines(lines):
    matrix = [[c for c in l] for l in lines]
    # Padding
    J = max(len(l) for l in matrix)
    for l in matrix:
        for _ in range(len(l), J):
            l.append(' ')
    return matrix

matrix = get_matrix_from_lines(lines)
matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

for i, __l in enumerate(matrix):
    l = ''.join(__l)

    for m in left.finditer(l):
        add_portal(portals, m.group()[0:2], m.start() + 2, i)

    for m in right.finditer(l):
        add_portal(portals, m.group()[1:], m.start(), i)

coord_to_portal = dict()
for k, v in portals.items():
    coord_to_portal[v] = k

matrix = get_matrix_from_lines(lines)

def next_portals(portals, matrix, start):
    i, j = portals[start]

    res = []
    todo = [(i, j, 0)]
    done = set()

    while len(todo) > 0:
        i, j, d = todo.pop()

        if (i, j) in done:
            continue

        done.add((i, j))

        if (i, j) in coord_to_portal:
            res.append((coord_to_portal[(i, j)], d))

        for ni, nj, v in u.ortho_neighbours_iterator(matrix, i, j):
            if v != '.' or (ni, nj) in done:
                continue

            todo.append((ni, nj, d+1))

    return [t for t in res if t[0] != start]

nodes = list(portals.keys())
edges = defaultdict(lambda: [])

for node in nodes:
    for next_node, d in next_portals(portals, matrix, node):
        edges[node].append((next_node, d))

for name in portal_names:
    edges[f"{name}-1"].append((f"{name}-2", 1))
    edges[f"{name}-2"].append((f"{name}-1", 1))

start_node = 'AA-1'
end_node = 'ZZ-1'

res = u.do_dijkstra(nodes, edges, start_node, end_node)

print(res)












