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

for l in matrix:
    print(' '.join(l))

iz, jz = None, None
for i, j in itertools.product(range(I), range(J)):
    if matrix[i][j] == '@':
        iz, jz = i, j
        break

matrix[iz][jz] = '.'

def node_name(i, j, keys):
    return f"{i}-{j}--{''.join(sorted(keys.lower()))}"

def unpack_node(node):
    coord, keys = node.split('--')
    i, j = coord.split('-')
    i, j = int(i), int(j)
    return (i, j, keys)

def get_nexts(matrix, i, j, keys):
    distances = { (i, j): 0 }
    to_bfs = [(i, j)]
    bfsed = set()
    res = list()

    while len(to_bfs) > 0:
        coord, to_bfs = to_bfs[0], to_bfs[1:]
        i, j = coord

        bfsed.add(coord)

        for ni, nj, v in u.ortho_neighbours_iterator(matrix, i, j):
            if (ni, nj) in bfsed:
                continue

            if v == '.' or v.lower() in keys:
                to_bfs.append((ni, nj))
                distances[(ni, nj)] = distances[(i, j)] + 1

            elif v == '#' or 'A' <= v <= 'Z':
                bfsed.add((ni, nj))
                pass

            elif 'a' <= v <= 'z':
                bfsed.add((ni, nj))
                res.append((ni, nj, distances[(i, j)] + 1, v))

    return res


# res = get_nexts(matrix, 4, 8, '')

# print(res)



# 1/0


nodes = set()
edges = defaultdict(lambda: list())

start_node = node_name(iz, jz, '')
to_explore = [start_node]

while len(to_explore) > 0:
    node, to_explore = to_explore[0], to_explore[1:]
    i, j, keys = unpack_node(node)
    nodes.add(node)

    # print(len(nodes))

    for ik, jk, d, k in get_nexts(matrix, i, j, keys):
        new_node = node_name(ik, jk, keys + k)
        if new_node in nodes:
            continue

        edges[node].append((new_node, d))
        to_explore.append(new_node)


all_keys = ''
for i, j in itertools.product(range(I), range(J)):
    if 'a' <= matrix[i][j] <= 'z':
        all_keys += matrix[i][j]

all_keys = ''.join(sorted(all_keys))

end_node = "thats_all_folks"
nodes.add(end_node)

for i, j in itertools.product(range(I), range(J)):
    if 'a' <= matrix[i][j] <= 'z':
        edges[node_name(i, j, all_keys)].append((end_node, 0))

res = u.do_dijkstra(nodes, edges, start_node, end_node)
print(res)












