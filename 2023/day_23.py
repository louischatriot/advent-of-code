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

edges = defaultdict(lambda: list())
nodes = set()

nodes.add(node_name(start))
paths_to_do = [start]
explored = set()

# The input is happily well formed!
while len(paths_to_do) > 0:
    print("==========================================")
    print(edges)
    print(paths_to_do)

    path_start = paths_to_do.pop(0)
    current = path_start
    d = 0

    explored.add(start)

    print("PATH START", path_start)


    while True:
        i, j = current

        s = sum(1 if matrix[ni][nj] in ['.', authorized_slopes[(ni-i, nj-j)]] and (ni, nj) not in explored else 0 for ni, nj, v in u.ortho_neighbours_iterator(matrix, i, j))

        if s == 1:
            nic, njc = None, None
            for ni, nj, v in u.ortho_neighbours_iterator(matrix, i, j):
                if v in ['.', authorized_slopes[(ni-i, nj-j)]] and (ni, nj) not in explored:
                    nic, njc = ni, nj

            d += 1
            explored.add(current)
            current = (nic, njc)
            continue

        else:  # Reached an intersection
            for ni, nj, v in u.ortho_neighbours_iterator(matrix, i, j):
                if v != '#' and (ni, nj) not in explored and v == authorized_slopes[(ni-i, nj-j)]:
                    edges[node_name(path_start)].append((node_name((ni, nj)), d+1))
                    paths_to_do.append((ni, nj))
                    explored.add(current)

            break

print("=====================================")
print("=====================================")

for s, e in edges.items():
    print("======================================")
    print(s)
    for __e in e:
        print(__e)




