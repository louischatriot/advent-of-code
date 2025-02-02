import sys
import re
import u as u
from collections import defaultdict
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
carts_shapes = ['>', '<', 'v', '^']
under_start = { '>': '-', '<': '-', '^': '|', 'v': '|' }

left_next = { '>': '^', '^': '<', '<': 'v', 'v': '>' }
right_next = { v: k for k, v in left_next.items() }
straight_next = { '>': '>', '<': '<', '^': '^', 'v': 'v' }
__next = [left_next, straight_next, right_next]

def turn(cart):
    _, _, dir, cycle = cart
    cart[2] = __next[cycle % 3][dir]
    cart[3] += 1

corners = ['/', '\\']
corners_next = {
    '/': { '>': '^', '^': '>', '<': 'v', 'v': '<'},
    '\\': { '>': 'v', 'v': '>', '<': '^', '^': '<' }
}

movements = { '>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0) }

N, M = len(lines), len(lines[0])
matrix = []
carts = list()

for y in range(N):
    line = lines[y]
    l = list()

    for x in range(M):
        c = line[x]
        if c in carts_shapes:
            carts.append([y, x, c, 0])
            c = under_start[c]

        l.append(c)

    matrix.append(l)


def print_everything(matrix, carts):
    __carts = dict()
    for y, x, d, _ in carts:
        __carts[(y, x)] = d

    print("=============================================")
    for y in range(N):
        l = list()
        for x in range(M):
            c = matrix[y][x] if (y, x) not in __carts else __carts[(y, x)]
            l.append(c)

        print(''.join(l))

    print("=============================================")


carts_pos = set()
for y, x, _, _ in carts:
    carts_pos.add((y, x))

end = False
while not end:
    carts = sorted(carts)
    for cart in carts:
        y, x, d, _ = cart
        dy, dx = movements[d]
        ny, nx = y+dy, x+dx
        cart[0] = ny
        cart[1] = nx

        c = matrix[ny][nx]

        if c in corners:
            cart[2] = corners_next[c][d]
        elif c == '+':
            turn(cart)

        # Check collision
        if (ny, nx) in carts_pos:
            print("PART 1 FIRST COLLISION", nx, ny)
            end = True
            break
        else:
            carts_pos.remove((y, x))
            carts_pos.add((ny, nx))



# PART 2
matrix = []
carts = list()

for y in range(N):
    line = lines[y]
    l = list()

    for x in range(M):
        c = line[x]
        if c in carts_shapes:
            carts.append([y, x, c, 0])
            c = under_start[c]

        l.append(c)

    matrix.append(l)


end = False
while not end:
    carts = sorted(carts)

    to_remove = list()

    for cart in carts:
        # Don't move a cart marked for collision
        if cart in to_remove:
            continue

        y, x, d, _ = cart
        dy, dx = movements[d]
        ny, nx = y+dy, x+dx

        # Will there be a collision
        if len([c for c in carts if c[0] == ny and c[1] == nx]) == 1:
            to_remove.append(cart)
            cart2 = [c for c in carts if c[0] == ny and c[1] == nx][0]
            to_remove.append(cart2)

        # Update pos
        cart[0] = ny
        cart[1] = nx

        # Turn if needed
        c = matrix[ny][nx]
        if c in corners:
            cart[2] = corners_next[c][d]
        elif c == '+':
            turn(cart)

    # Inefficient but oh well
    for cart in to_remove:
        carts = [c for c in carts if c != cart]

    if len(carts) == 1:
        break


cart = carts[0]
print("PART 2 LAST CART", cart[1], cart[0])



