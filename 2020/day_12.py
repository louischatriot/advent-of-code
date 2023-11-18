import sys
import re
import u as u
from collections import defaultdict

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
d = 'E'
x = 0
y = 0
nexts = {
    'L': {'N': 'W', 'S': 'E', 'E': 'N', 'W': 'S'},
    'R': {'N': 'E', 'S': 'W', 'E': 'S', 'W': 'N'}
}

for l in lines:
    i = l[0]
    amt = int(l[1:])

    if i == 'F':
        i = d

    if i == 'N':
        y += amt

    if i == 'S':
        y -= amt

    if i == 'W':
        x -= amt

    if i == 'E':
        x += amt

    if i in {'L', 'R'}:
        for _ in range(0, amt // 90):
            d = nexts[i][d]

res = abs(x) + abs(y)
print(res)


# PART 2
x = 10
y = 1
xs = 0
ys = 0

for l in lines:
    i = l[0]
    amt = int(l[1:])

    if i == 'F':
        xs += amt * x
        ys += amt * y

    if i == 'N':
        y += amt

    if i == 'S':
        y -= amt

    if i == 'W':
        x -= amt

    if i == 'E':
        x += amt

    for _ in range(0, amt // 90):  # That's dirty
        if i == 'L':
            x, y = -y, x

        if i == 'R':
            x, y = y, -x


    print('==================', l)
    print(xs, ys)
    print(x, y)


res = abs(xs) + abs(ys)
print(res)






