import sys
import re
import u as u
from collections import defaultdict
import math

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
matrix = [[int(c) for c in l] for l in lines]
d_bound = sum([sum(l) for l in matrix]) + 1
N = len(matrix)
M = len(matrix[0])

unvisited = set()
for i in range(0, N):
    for j in range(0, M):
        unvisited.add((i, j))

distances = [[d_bound for _ in range(0, M)] for _ in range(0, N)]
distances[0][0] = 0
current = (0, 0)

while (N-1, M-1) in unvisited:
    i, j = current

    for di, dj in u.ortho_neighbours:
        if (i+di, j+dj) in unvisited:
            distances[i+di][j+dj] = min(distances[i+di][j+dj], distances[i][j] + matrix[i+di][j+dj])

    unvisited.remove(current)

    dist = d_bound
    for node in unvisited:
        if distances[node[0]][node[1]] < dist:  # Should really stop with the matrix representations of graphs
            dist = distances[node[0]][node[1]]
            current = node


print(distances[N-1][M-1])




