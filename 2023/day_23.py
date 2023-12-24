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
matrix = [[c for c in l] for l in lines]
I, J = len(matrix), len(matrix[0])

def node_name(node):
    return f"{node[0]}-{node[1]}"

def parse_node(name):
    node = name.split('-')
    return (int(node[0]), int(node[1]))

start = (0, 1)
end = (I-1, J-2)

authorized_slopes = {
    (1, 0): 'v',
    (-1, 0): '^',
    (0, 1): '>',
    (0, -1): '<',
}

# This assumes no incompatible slopes along any path
def get_next(matrix, i, j, explored):
    d = 0

    while True:
        if (i, j) == end:
            break

        s = sum(1 if v != '#' and (ni, nj) not in explored else 0 for ni, nj, v in u.ortho_neighbours_iterator(matrix, i, j))

        if s != 1:
            break

        nic, njc = None, None
        for ni, nj, v in u.ortho_neighbours_iterator(matrix, i, j):
            if v in ['.', authorized_slopes[(ni-i, nj-j)]] and (ni, nj) not in explored:
                nic, njc = ni, nj

        explored.add((i, j))
        i, j = nic, njc
        d += 1

    return ((i, j), d)


def get_nexts(matrix, i, j):
    res = []

    for ni, nj, v in u.ortho_neighbours_iterator(matrix, i, j):
        if v in ['.', authorized_slopes[(ni-i, nj-j)]]:
            dest, d = get_next(matrix, ni, nj, { (i, j) })
            res.append((dest, d+1))

    return res


edges = defaultdict(lambda: set())
nodes = set()
distances = defaultdict(lambda: dict())
to_explore = [start]

while len(to_explore) > 0:
    current = to_explore.pop(0)

    # TODO: probably incorrect actually, need to check if other paths
    if current in nodes:
        continue

    nodes.add(current)

    for dest, d in get_nexts(matrix, *current):
        distances[node_name(current)][node_name(dest)] = d
        edges[node_name(current)].add(node_name(dest))

        if dest != end:
            to_explore.append(dest)

nodes.add(end)

print(nodes)

for beg, dests in edges.items():
    print("=========", beg)
    print(dests)


L = u.topological_sort(nodes, edges)

print(L)


