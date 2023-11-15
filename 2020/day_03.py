import sys

fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if len(sys.argv) > 1 else '') + '.data'

# with open("inputs/day_01.data") as file:
with open(fn) as file:
    lines = [line.rstrip() for line in file]

# PART 1
p = 0
L = len(lines[0])
t = 0
for l in lines:
    if l[p] == '#':
        t += 1
    p = (p + 3) % L

print(t)


# PART 2
res = 1
for (dx, dy) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    y = 0
    x = 0
    L = len(lines[0])
    t = 0

    while y < len(lines):
        if lines[y][x] == '#':
            t += 1
        x = (x + dx) % L
        y += dy

    res *= t

print(res)




