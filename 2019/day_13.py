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

outs = []
out = None
while True:
    out = computer.run_until_output()
    if out is None:
        break

    outs.append(out)

tiles = set()
for i in range(0, len(outs) // 3):
    tiles.add((outs[3 * i], outs[3 * i + 1], outs[3 * i + 2]))

res = 0
mx, Mx, my, My = 9999999, -9999999, 9999999, -9999999
for x, y, tile_id in tiles:
    if tile_id == 2:
        res += 1
    mx, Mx = min(mx, x), max(Mx, x)
    my, My = min(my, y), max(My, y)


print(res)


# PART 2
matrix = [[' ' for _ in range(mx, Mx+1)] for _ in range(my, My+1)]
for x, y, tile_id in tiles:
    v = ' '
    if tile_id == 0:
        v = '.'
    elif tile_id == 1:
        v = 'X'
    elif tile_id == 2:
        v = 'w'
    elif tile_id == 3:
        v = '_'
    elif tile_id == 4:
        v = 'o'

    matrix[y][x] = v

for l in matrix:
    print(' '.join(l))






