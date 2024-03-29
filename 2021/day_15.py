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


# PART 2
bigmatrix = [[0 for _ in range(0, 5*M)] for _ in range(0, 5*N)]

for i in range(0, N):
    for j in range(0, M):
        for bigi in range(0, 5):
            for bigj in range(0, 5):
                nv = matrix[i][j] + bigi+bigj
                if nv > 9:
                    nv -= 9
                if nv > 9:
                    nv -= 9
                bigmatrix[N * bigi + i][M * bigj + j] = nv

matrix = bigmatrix


d_bound = sum([sum(l) for l in matrix]) + 1
N = len(matrix)
M = len(matrix[0])

unvisited = set()
for i in range(0, N):
    for j in range(0, M):
        unvisited.add((i, j))

# This Dijkstra is ugly, fix and package it for next times

dist_pq = u.PriorityQueue()
for i in range(0, N):
    for j in range(0, M):
        if i != 0 or j != 0:
            dist_pq.add_task((i, j), d_bound)

current = (0, 0)
current_dist = 0

while (N-1, M-1) in unvisited:
    i, j = current

    for di, dj in u.ortho_neighbours:
        if (i+di, j+dj) in unvisited:
            _, d1 = dist_pq.get_task((i+di, j+dj))
            d = min(d1, current_dist + matrix[i+di][j+dj])
            dist_pq.add_task((i+di, j+dj), d)

    unvisited.remove(current)

    current, current_dist = dist_pq.pop_task()

    if current == (N-1, M-1):
        print(current_dist)

    if current is None:
        break


