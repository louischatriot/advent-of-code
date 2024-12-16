import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import collections
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1 - Building an aggregated graph, actually unnecessary ...
# That makes the Dijkstra 2x faster but it was fast enough already and the graph building does take time
g = u.Graph()
N, M = len(lines), len(lines[0])
mit = itertools.product(range(N), range(M))
matrix = [[c for c in l] for l in lines]
start, end = None, None

for i, j in mit:
    if matrix[i][j] == 'S':
        start = (i, j)
        matrix[i][j] = '.'
    elif matrix[i][j] == 'E':
        end = (i, j)
        matrix[i][j] = '.'


def node_name(pos, dir):
    i, j = pos
    di, dj = dir
    return f"<{i};{j} | {di};{dj}>"

to_explore = collections.deque()
to_explore.append((start, (0, 1)))  # Start facing east
visited = set()

while to_explore:
    pos, dir = to_explore.popleft()
    i, j = pos
    di, dj = dir
    name = node_name(pos, dir)

    if name in visited:
        continue

    direcshuns = list()
    for ndi, ndj in u.ortho_neighbours:
        if matrix[i+ndi][j+ndj] == '.' and not (ndi + di == 0 and ndj + dj == 0):
            direcshuns.append((ndi, ndj))

    new_states = list()
    for ndi, ndj in direcshuns:
        new_states.append((pos, (ndi, ndj)))

        if ndi != di or ndj != dj:
            g.update_directed_edge(name, node_name(pos, (ndi, ndj)), 1000)

    for pos, dir in new_states:
        i, j = pos
        di, dj = dir
        m = 1
        while matrix[i+m*di+di][j+m*dj+dj] == '.' and matrix[i+m*di-di][j+m*dj-dj] == '.' and sum(1 if matrix[i + m*di + ndi][j + m*dj + ndj] == '.' else 0 for ndi, ndj in u.ortho_neighbours) == 2:
            m += 1

        new_pos = (i+m*di, j+m*dj)
        new_name = node_name(new_pos, dir)

        if new_name not in visited:
            g.update_directed_edge(node_name(pos, dir), new_name, m)
            to_explore.append((new_pos, dir))

    visited.add(name)


for dir in u.ortho_neighbours:
    g.add_directed_edge(node_name(end, dir), 'end', 0)


start_node = node_name(start, (0, 1))

res = g.dijkstra(start_node, 'end')
print(res)




# PART 1 and 2 - Alternate
import heapq

N, M = len(lines), len(lines[0])
mit = itertools.product(range(N), range(M))
matrix = [[c for c in l] for l in lines]
start, end = None, None

for i, j in mit:
    if matrix[i][j] == 'S':
        start = (i, j)
        matrix[i][j] = '.'
    elif matrix[i][j] == 'E':
        end = (i, j)
        matrix[i][j] = '.'


BIG = 9999999999999
queue = []
distances = defaultdict(lambda: BIG)
visited = set()

heapq.heappush(queue, (0, start, (0, 1)))
distances[(start, (0, 1))] = 0
best_predecessors = dict()

THE_END = None

while True:
    distance, pos, dir = heapq.heappop(queue)

    if (pos, dir) in visited:
        continue
    visited.add((pos, dir))

    if pos == end:
        print(distance)
        THE_END = (pos, dir)
        break

    i, j = pos
    di, dj = dir

    def edges():
        for ndi, ndj in u.ortho_neighbours:
            if matrix[i+ndi][j+ndj] != '.' or (di, dj) == (-ndi, -ndj):
                continue

            d = 1 if (ndi, ndj) == (di, dj) else 1001
            yield d, (i+ndi, j+ndj), (ndi, ndj)

    for d, new_pos, new_dir in edges():
        new_state = (new_pos, new_dir)

        if distances[new_state] == distance + d:
            best_predecessors[new_state].append((pos, dir))

        elif distances[new_state] > distance + d:
            best_predecessors[new_state] = [(pos, dir)]
            distances[new_state] = distance + d

            heapq.heappush(queue, (distances[new_state], *new_state))


spots = set()

def get_spots(preds, spots, current):
    spots.add(current[0])

    if current in preds:
        for pred in preds[current]:
            get_spots(preds, spots, pred)

get_spots(best_predecessors, spots, THE_END)
print(len(spots))









