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

from intcode import Computer


# PART 2
def run_once(x, y):
    program = [int(n) for n in lines[0].split(',')]
    computer = Computer(program)

    computer.run_until_input(x)
    computer.run_until_input(y)
    return computer.run_until_output()

def get_line(y):
    cx = y * 39 // 49  # Given shape of beam it must be in it
    v = run_once(cx, y)
    if v != 1:
        raise ValueError("Wrong center")

    l, h = 0, cx
    while l < h - 1:
        pivot = (l + h) // 2
        v = run_once(pivot, y)
        if v == 1:
            h = pivot
        else:
            l = pivot

    assert run_once(l, y) == 0
    assert run_once(h, y) == 1
    xl = h

    l, h = cx, 3000  # 3000 arbitrary but "high enough"
    while l < h - 1:
        pivot = (l + h) // 2
        v = run_once(pivot, y)
        if v == 1:
            l = pivot
        else:
            h = pivot

    assert run_once(l, y) == 1
    assert run_once(h, y) == 0
    xr = l

    return (xl, xr)


def contains_square(y):
    xl1, xr1 = get_line(y)
    xl2, xr2 = get_line(y+99)

    return xr1 - xl2 >= 99


yl, yh = 0, 1500  # 1500 arbitrary, large enough
while yl < yh - 1:
    pivot = (yl + yh) // 2
    if contains_square(pivot):
        yh = pivot
    else:
        yl = pivot

assert contains_square(yl) is False
assert contains_square(yh) is True

xl2, _ = get_line(yh+99)
print("PART 2:", 10000 * xl2 + yh)


# PART 1
X, Y = 50, 50
matrix = [['.' for x in range(X)] for y in range(Y)]

res = 0

for x, y in itertools.product(range(X), range(Y)):
    v = run_once(x, y)

    if v == 1:
        res += 1
        matrix[y][x] = '#'

for l in matrix:
    print(' '.join(l))

print("PART 1:", res)


