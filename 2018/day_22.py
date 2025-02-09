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
    lines = [line[0:-1] for line in file]


# PART 1
depth = int(lines[0].split(': ')[1])
tx, ty = lines[1].split(': ')[1].split(',')
tx, ty = int(tx), int(ty)

X, Y = tx * 5, ty * 5  # Big enough to contain optimal path

geo = [[None for _ in range(X)] for _ in range(Y)]
ero = [[None for _ in range(X)] for _ in range(Y)]

E = 20183

geo[0][0] = 0
geo[ty][tx] = 0

ero[0][0] = (geo[0][0] + depth) % E
ero[ty][tx] = (geo[ty][tx] + depth) % E

for x in range(1, X):
    geo[0][x] = 16807 * x
    ero[0][x] = (geo[0][x] + depth) % E

for y in range(1, Y):
    geo[y][0] = 48271 * y
    ero[y][0] = (geo[y][0] + depth) % E

for y in range(1, Y):
    for x in range(1, X):
        if x == tx and y == ty:
            continue

        geo[y][x] = ero[y-1][x] * ero[y][x-1]
        ero[y][x] = (geo[y][x] + depth) % E


res = sum(ero[y][x] % 3 for x, y in itertools.product(range(tx+1), range(ty+1)))
print(res)


# PART 2
import heapq

NEITHER, TORCH, GEAR = 0, 1, 2  # These numbers correspond to the forbidden region for the gear
EQUIPMENTS = [NEITHER, TORCH, GEAR]
SWITCH_TIME = 7
MOVING_TIME = 1

start = (0, 0, TORCH)
end = (tx, ty, TORCH)

frontier = list()
distances = defaultdict(lambda: float('inf'))
visited = set()

heapq.heappush(frontier, (0, start))
distances[start] = 0

while frontier:
    _, node = heapq.heappop(frontier)

    if node in visited:
        continue
    else:
        visited.add(node)

    if node == end:
        print(distances[node])
        break

    x, y, equipment = node

    def edges():
        for dx, dy in u.ortho_neighbours:
            nx, ny = x+dx, y+dy
            if 0 <= nx < X and 0 <= ny < Y:
                if ero[ny][nx] % 3 != equipment:
                    yield (MOVING_TIME, nx, ny, equipment)

        for neq in EQUIPMENTS:
            if neq != ero[y][x] % 3:
                yield (SWITCH_TIME, x, y, neq)

    for d, nx, ny, neq in edges():
        new_node = (nx, ny, neq)

        if distances[node] + d < distances[new_node]:
            distances[new_node] = distances[node] + d

            # Surprisingly using A* with Manhattan distance to target is not faster than Dijkstra
            # f = distances[new_node] + abs(tx - nx) + abs(ty - ny)
            f = distances[new_node]

            heapq.heappush(frontier, (f, new_node))









