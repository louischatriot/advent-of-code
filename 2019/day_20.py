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
def get_matrix_from_lines(lines):
    matrix = [[c for c in l] for l in lines]
    # Padding
    J = max(len(l) for l in matrix)
    for l in matrix:
        for _ in range(len(l), J):
            l.append(' ')
    return matrix

portals = dict()
portal_names = set()

def add_portal(portals, name, i, j, I, J):
    if i in [2, I-3] or j in [2, J-3]:
        key = f"{name}-1"
    else:
        key = f"{name}-2"

    if key in portals:
        raise ValueError("Can't have the same key twice")

    portals[key] = (i, j)

    if name not in ['AA', 'ZZ']:
        portal_names.add(name)

left = re.compile('[A-Z]{2}\.')
right = re.compile('\.[A-Z]{2}')

matrix = get_matrix_from_lines(lines)
I, J = len(matrix), len(matrix[0])

for i, __l in enumerate(matrix):
    l = ''.join(__l)

    for m in left.finditer(l):
        add_portal(portals, m.group()[0:2], i, m.start() + 2, I, J)

    for m in right.finditer(l):
        add_portal(portals, m.group()[1:], i, m.start(), I, J)

matrix = get_matrix_from_lines(lines)
matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

for i, __l in enumerate(matrix):
    l = ''.join(__l)

    for m in left.finditer(l):
        add_portal(portals, m.group()[0:2], m.start() + 2, i, I, J)

    for m in right.finditer(l):
        add_portal(portals, m.group()[1:], m.start(), i, I, J)

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


# PART 2
DEPTH = 50

nodes = list()
edges = defaultdict(lambda: [])

for name in portals.keys():
    for dep in range(DEPTH):
        nodes.append(f"{name}--{dep}")

for node in portals.keys():
    for next_node, d in next_portals(portals, matrix, node):
        for dep in range(DEPTH):
            edges[f"{node}--{dep}"].append((f"{next_node}--{dep}", d))

for name in portal_names:
    if name not in ['AA', 'ZZ']:
        for dep in range(DEPTH):
            edges[f"{name}-2--{dep}"].append((f"{name}-1--{dep+1}", 1))
            edges[f"{name}-1--{dep+1}"].append((f"{name}-2--{dep}", 1))

start_node = 'AA-1--0'
end_node = 'ZZ-1--0'
res = u.do_dijkstra(nodes, edges, start_node, end_node)
print(res)




