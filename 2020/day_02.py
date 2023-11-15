import sys

fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if len(sys.argv) > 1 else '') + '.data'

# with open("inputs/day_01.data") as file:
with open(fn) as file:
    lines = [line.rstrip() for line in file]

# PART 1
res = 0
for _d in lines:
    d = _d.split(' ')
    d[1] = d[1][0]
    l, u = d[0].split('-')
    l = int(l)
    u = int(u)

    count = 0
    for c in d[2]:
        if c == d[1]:
            count += 1

    if l <= count <= u:
        res += 1

print(res)


# PART 2
res = 0
for _d in lines:
    d = _d.split(' ')
    d[1] = d[1][0]
    l, u = d[0].split('-')
    l = int(l)
    u = int(u)

    if (d[2][l-1] == d[1]) != (d[2][u-1] == d[1]):
        res += 1

print(res)

