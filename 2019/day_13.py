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

program = [int(n) for n in lines[0].split(',')]
program[0] = 2
computer = Computer(program)

res = 0
ball_x = 20
paddle_x = 20
while True:
    opcode = computer.run_until_io()

    if opcode is None:
        print(res)
        break

    if opcode[3:] == '03':
        v = 0
        if paddle_x < ball_x:
            v = 1
        if paddle_x > ball_x:
            v = -1
        computer.run_until_input(v)

    elif opcode[3:] == '04':
        x = computer.run_until_output()
        y = computer.run_until_output()
        v = computer.run_until_output()

        if x == -1 and y == 0:
            res = v

        if v == 4:
            ball_x = x

        if v == 3:
            paddle_x = x


    else:
        raise ValueError("WTF")




