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

            elif 'a' <= v <= 'z':
                bfsed.add((ni, nj))
                res.append((ni, nj, distances[(i, j)] + 1, v))

    return res


def build_graph(matrix, start_node):
    nodes = set()
    edges = defaultdict(lambda: list())

    to_explore = [start_node]

    while len(to_explore) > 0:
        node, to_explore = to_explore[0], to_explore[1:]
        i, j, keys = unpack_node(node)

        if node in nodes:
            continue

        nodes.add(node)

        for ik, jk, d, k in get_nexts(matrix, i, j, keys):
            new_node = node_name(ik, jk, keys + k)
            if new_node in nodes:
                continue

            edges[node].append((new_node, d))
            to_explore.append(new_node)

    return (nodes, edges)


# This works well only because the labyrinth is only with size 1 corridors
def get_all_nexts(matrix, i, j):
    distances = { (i, j): 0 }
    on_path = defaultdict(lambda: set())
    res = list()

    to_bfs = [(i, j)]
    bfsed = set()

    while len(to_bfs) > 0:
        coord, to_bfs = to_bfs[0], to_bfs[1:]
        i, j = coord

        bfsed.add(coord)

        for ni, nj, v in u.ortho_neighbours_iterator(matrix, i, j):
            if (ni, nj) in bfsed:
                continue

            if v == '.':
                to_bfs.append((ni, nj))
                distances[(ni, nj)] = distances[(i, j)] + 1
                on_path[(ni, nj)] = on_path[(i, j)].union({})

            elif v == '#':
                bfsed.add((ni, nj))

            elif 'A' <= v <= 'Z':
                distances[(ni, nj)] = distances[(i, j)] + 1
                on_path[(ni, nj)] = on_path[(i, j)].union({ v.lower() })

                to_bfs.append((ni, nj))

            elif 'a' <= v <= 'z':
                distances[(ni, nj)] = distances[(i, j)] + 1
                on_path[(ni, nj)] = on_path[(i, j)].union({ v })

                to_bfs.append((ni, nj))
                res.append((ni, nj))

    _res = []
    for coord in res:
        d = distances[coord]
        v = matrix[coord[0]][coord[1]]
        keys = ''.join(sorted(list(on_path[coord].difference({v}))))
        _res.append((coord[0], coord[1], v, d, keys))

    return _res

def get_all_links(matrix, start_positions):
    _froms = [(i, j) for i, j in itertools.product(range(I), range(J)) if 'a' <= matrix[i][j] <= 'z']
    for coord in start_positions:
        _froms.append(coord)

    links = defaultdict(lambda: dict())

    for _from in _froms:
        for i, j, v, d, keys in get_all_nexts(matrix, _from[0], _from[1]):
            links[_from][(i, j)] = (v, d, keys)

    return links


def build_graph_faster(matrix, start_node):
    links = get_all_links(matrix, [(iz, jz)])

    nodes = set()
    edges = defaultdict(lambda: list())

    to_explore = [start_node]

    while len(to_explore) > 0:
        node, to_explore = to_explore[0], to_explore[1:]
        i, j, keys = unpack_node(node)

        if node in nodes:
            continue

        nodes.add(node)

        for _to, contents in links[(i, j)].items():
            ik, jk = _to
            the_key, d, on_path_keys = contents

            if all(k in keys for k in on_path_keys) and the_key not in keys:
                new_node = node_name(ik, jk, keys + the_key)

                if new_node in nodes:
                    continue

                edges[node].append((new_node, d))
                to_explore.append(new_node)

    return (nodes, edges)


start_node = node_name(iz, jz, '')
nodes, edges = build_graph_faster(matrix, start_node)

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


# PART 2
new_starts = []
for di, dj in u.all_neighbours_and_center:
    ni, nj = iz+di, jz+dj
    if di == 0 or dj == 0:
        v = '#'
    else:
        v = '.'
        new_starts.append((ni, nj))

    matrix[ni][nj] = v

for l in matrix:
    print(' '.join(l))

def node_name_robots(robots, keys):
    res = [f"{r[0]}-{r[1]}" for r in robots]
    res = '--'.join(res)
    res += '---' + ''.join(sorted(keys.lower()))

    return res

def unpack_node_robots(node):
    __robots, keys = node.split('---')
    __robots = __robots.split('--')
    robots = []
    for r in __robots:
        r = r.split('-')
        robots.append((int(r[0]), int(r[1])))

    return (robots, keys)

def update_robots(robots, idx0, ir, jr):
    return [(r[0], r[1]) if idx != idx0 else (ir, jr) for idx, r in enumerate(robots)]


def build_graph_robots(matrix, starts, links, all_keys, start_node, end_node):
    nodes = set()
    edges = defaultdict(lambda: list())

    to_explore = [start_node]

    while len(to_explore) > 0:
        node, to_explore = to_explore[0], to_explore[1:]

        if node in nodes:
            continue

        robots, keys = unpack_node_robots(node)
        nodes.add(node)

        for idx, robot in enumerate(robots):
            i, j = robot

            for _to, contents in links[(i, j)].items():
                ik, jk = _to
                the_key, d, on_path_keys = contents

                if all(k in keys for k in on_path_keys) and the_key not in keys:
                    if ''.join(sorted(keys + the_key)) == all_keys:
                        new_node = end_node
                        edges[node].append((new_node, d))

                    else:
                        new_node = node_name_robots(update_robots(robots, idx, ik, jk), keys + the_key)

                        if new_node in nodes:
                            continue

                        edges[node].append((new_node, d))
                        to_explore.append(new_node)

    return (nodes, edges)

all_keys = ''
for i, j in itertools.product(range(I), range(J)):
    if 'a' <= matrix[i][j] <= 'z':
        all_keys += matrix[i][j]
all_keys = ''.join(sorted(all_keys))

start_node = node_name_robots(new_starts, '')
end_node = "thats_all_folks"
links = get_all_links(matrix, new_starts)
nodes, edges = build_graph_robots(matrix, new_starts, links, all_keys, start_node, end_node)

nodes.add(end_node)

res = u.do_dijkstra(nodes, edges, start_node, end_node)
print(res)


