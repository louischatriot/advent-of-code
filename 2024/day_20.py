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


# PART 1
N, M = len(lines), len(lines[0])
matrix = [[c for c in line] for line in lines]

# Finding start and end
for i, j in itertools.product(range(N), range(M)):
    if matrix[i][j] == 'S':
        start = (i, j)
        break

for i, j in itertools.product(range(N), range(M)):
    if matrix[i][j] == 'E':
        end = (i, j)
        break

# Brute force is really long in part 1 and intractable in part 2
# def bfs_matrix(matrix, __start, __end):
    # N, M = len(matrix), len(matrix[0])

    # if type(__start) == tuple:
        # start = __start
    # else:
        # for i, j in itertools.product(range(N), range(M)):
            # if matrix[i][j] == __start:
                # start = (i, j)
                # break

    # if type(__end) == tuple:
        # end = __end
    # else:
        # for i, j in itertools.product(range(N), range(M)):
            # if matrix[i][j] == __end:
                # end = (i, j)
                # break

    # visited = set()
    # to_explore = collections.deque()
    # to_explore.append((start, 0))

    # while to_explore:
        # node, distance = to_explore.popleft()

        # if node in visited:
            # continue
        # visited.add(node)

        # if node == end:
            # return distance

        # i, j = node
        # for di, dj in u.ortho_neighbours:
            # ni, nj = i+di, j+dj
            # if 0 <= ni < N and 0 <= nj < M:
                # if matrix[ni][nj] != '#' and (ni, nj) not in visited:
                    # to_explore.append(((ni, nj), distance+1))

    # return -1

# for i, j in itertools.product(range(1, N-1), range(1, M-1)):
    # if matrix[i][j] == '#':
        # matrix[i][j] = '.'
        # t = bfs_matrix(matrix, 'S', 'E')
        # if t < base:
            # BBB += base - t
            # if base - t >= target_save:
                # res += 1

        # matrix[i][j] = '#'


# BFS from the start
from_start = [[9999999999 for _ in range(M)] for _ in range(N)]
visited = set()
to_explore = collections.deque()
to_explore.append((start, 0))

while to_explore:
    node, distance = to_explore.popleft()

    if node in visited:
        continue
    visited.add(node)
    i, j = node
    from_start[i][j] = distance

    for di, dj in u.ortho_neighbours:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M:
            if matrix[ni][nj] != '#' and (ni, nj) not in visited:
                to_explore.append(((ni, nj), distance+1))

# BFS from the end
from_end = [[9999999999 for _ in range(M)] for _ in range(N)]
visited = set()
to_explore = collections.deque()
to_explore.append((end, 0))

while to_explore:
    node, distance = to_explore.popleft()

    if node in visited:
        continue
    visited.add(node)
    i, j = node
    from_end[i][j] = distance

    for di, dj in u.ortho_neighbours:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M:
            if matrix[ni][nj] != '#' and (ni, nj) not in visited:
                to_explore.append(((ni, nj), distance+1))


base = from_start[end[0]][end[1]]
target_save = 100

def get_cheats(MAX_SIZE):
    res = 0

    for si, sj in itertools.product(range(1, N-1), range(1, M-1)):
        if matrix[si][sj] == '#':
            continue

        for ei in range(max(1, si - MAX_SIZE), min(N-1, si + MAX_SIZE + 1)):
            for dj in range(-MAX_SIZE+abs(si-ei), MAX_SIZE-abs(si-ei)+1):
                ej = sj+dj
                if 1 <= ej < M-1 and matrix[ei][ej] != '#':
                    cheated = from_start[si][sj] + from_end[ei][ej] + abs(si - ei) + abs(sj - ej)
                    if cheated < base:
                        if base - cheated >= target_save:
                            res += 1

    return res


# PART 1 and 2
print(get_cheats(2))
print(get_cheats(20))



