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
    lines = [line.rstrip() for line in file]


# PART 1
nodes = []
for line in lines[2:]:
    contents = line[15:].split()
    x, y = contents[0].split('-')
    x, y = int(x[1:]), int(y[1:])
    nodes.append(((x, y), int(contents[1][0:-1]), int(contents[2][0:-1]), int(contents[3][0:-1])))

res = 0
for n in nodes:
    for m in nodes:
        ncoord, _, nused, navail = n
        mcoord, _, mused, mavail = m

        nx, ny = ncoord
        mx, my = mcoord

        if nx != mx or ny != my:
            if nused <= mavail:  # Symetric case checked when n and m are swapped
                if nused > 0:
                    res += 1

print(res)


# PART 2
import json

M, N = -1, -1

for n in nodes:
    coord, _, _, _ = n
    x, y = coord
    M, N = max(M, x), max(N, y)

M, N = M+1, N+1

# Simply print the grid to see the walls and the hole as in the example
# Assume you can always move the hole and tada that's actually the right answer
# The more general problem is actually intractable at a reasonable size for a BFS (see below)
# An A* would be better but still rely on structure i.e. first get an large enough empty next
# to the target data, then move it
start_grid = [[None for _ in range(M)] for _ in range(N)]
for n in nodes:
    coord, tot, used, _ = n
    x, y = coord
    start_grid[y][x] = (tot, used)

for y in range(N):
    l = []

    for x in range(M):
        c = '.'

        if x == 0 and y == 0:
            c = 'O'
        elif x == M-1 and y == 0:
            c = 'T'
        elif start_grid[y][x][0] > 100:
            c = 'X'
        elif start_grid[y][x][1] == 0:
            c = '_'

        l.append(c)

    print('   '.join(l))
    print('')


# Problem space is too large for the BFS to find the solution
sys.exit(0)

start_grid = [[None for _ in range(M)] for _ in range(N)]

def clone_grid(grid):
    res = [[None for _ in range(M)] for _ in range(N)]
    for x, y in itertools.product(range(M), range(N)):
        res[y][x] = grid[y][x]
    return res

for n in nodes:
    coord, tot, used, _ = n
    x, y = coord
    start_grid[y][x] = (tot, used)

start_state = [(M-1, 0), start_grid]

to_explore = list()
to_explore.append((start_state, 0))
explored = set()

while len(to_explore) > 0:
    print(len(to_explore))

    state, distance = to_explore.pop(0)
    signature = json.dumps(state)
    if signature in explored:
        continue
    else:
        explored.add(signature)

    for y in range(N):
        for x in range(M):
            for dx, dy in u.ortho_neighbours:
                if not (0 <= x+dx < M and 0 <= y+dy < N):
                    continue

                ct, cu = state[1][y][x]
                nt, nu = state[1][y+dy][x+dx]

                if nt < cu + nu:  # Not enough free space to move the data
                    continue

                new_grid = clone_grid(state[1])
                new_grid[y][x] = (ct, 0)
                new_grid[y+dy][x+dx] = (nt, nu + cu)

                tx, ty = state[0]
                if tx == x and ty == y:  # This is the target data we are moving
                    new_target = (x+dx, y+dy)
                else:
                    new_target = state[0]

                if new_target[0] == 0 and new_target[1] == 0:
                    print(distance + 1)
                    sys.exit(0)

                new_state = [new_target, new_grid]
                to_explore.append((new_state, distance + 1))












