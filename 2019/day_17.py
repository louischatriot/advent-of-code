import sys
import re
import u as u
from collections import defaultdict
import math
import itertools

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
from intcode import Computer
program = [int(n) for n in lines[0].split(',')]
computer = Computer(program)

data = []
l = []
while True:
    out = computer.run_until_output()
    if out is None:
        break
    else:
        if out == 10 and len(l) > 0:
            data.append(l)
            l = []
        else:
            l.append(chr(out))

for l in data:
    print(''.join(l))

I, J = len(data), len(data[0])

si, sj = None, None
for i, l in enumerate(data):
    for j, c in enumerate(l):
        if c != '.' and c != '#':
            si, sj = i, j


res = 0
intersections = set()
for i, j in itertools.product(range(I), range(J)):
    neighbs = [v for v in u.ortho_neighbours_iterator(data, i, j)]
    if sum(1 if v[2] == '#' else 0 for v in neighbs) == 4 and data[i][j] == '#':
        intersections.add((i, j))
        res += i * j

print(res)




# explored = set()
# to_explore = list()
# to_explore.append((si, sj))


# def go_to_next_intersection(data, iz, jz, explored):
    # i, j = iz, jz

    # while True:
        # neighbs = [v for v in u.ortho_neighbours_iterator(data, i, j)]

        # if sum(1 if v[2] == '#' else 0 for v in neighbs) == 4:
            # break

        # ladder = next(filter(lambda v: v[2] == '#' and (v[0], v[1]) not in explored, neighbs))
        # explored.add((i, j))
        # i, j = ladder[0], ladder[1]

    # explored.add((i, j))

    # return (i, j)



# while len(to_explore) > 0:
# for _ in range(0, 4):
    # iz, jz = to_explore.pop(0)

    # print("============", iz, jz, to_explore)

    # if (iz, jz) not in explored:
        # i, j = go_to_next_intersection(data, iz, jz, explored)
        # intersections.add((i, j))  # Could also store the edge if part 2 asks for hamiltonian path

        # # print(intersections)

        # neighbs = [v for v in u.ortho_neighbours_iterator(data, i, j)]
        # for neighb in neighbs:
            # if (neighb[0], neighb[1]) not in explored:
                # to_explore.append((neighb[0], neighb[1]))

        # explored.add((iz, jz))
        # explored.add((i, j))

    # print("Intersections", intersections)
    # print(len(explored))

    # # print(len(to_explore))
    # # print(len(intersections))
    # # print(intersections)

        # # print(len(explored))









