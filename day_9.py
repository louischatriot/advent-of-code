with open("inputs/day_9.data") as file:
    lines = [line.rstrip() for line in file]

movements = [(line[0], int(line[2:])) for line in lines]

def new_pos(t, h):
    tx, ty = t
    hx, hy = h

    if tx == hx:
        if ty + 1 < hy:
            ty += 1
        elif ty - 1 > hy:
            ty -= 1
    elif ty == hy:
        if tx + 1 < hx:
            tx += 1
        elif tx - 1 > hx:
            tx -= 1
    else:
        if abs(tx - hx) + abs(ty - hy) >= 3:
            tx += 1 if tx < hx else -1
            ty += 1 if ty < hy else -1

    return (tx, ty)

def deltas(d):
    dx, dy = 0, 0

    if d == 'R':
        dx = 1
    elif d == 'L':
        dx = -1
    elif d == 'U':
        dy = -1
    elif d == 'D':
        dy = 1
    else:
        raise ValueError("Unknown direction")

    return (dx, dy)



# Part 1

tx, ty, hx, hy = 0, 0, 0, 0
visited = set()
visited.add((tx, ty))

for d, n in movements:
    dx, dy = deltas(d)

    for _ in range(0, n):
        hx += dx
        hy += dy

        tx, ty = new_pos((tx, ty), (hx, hy))

        visited.add((tx, ty))

print(len(visited))


# Part 2

rope = [(0, 0)] * 10
visited = set()
visited.add(rope[-1])

for d, n in movements:
    dx, dy = deltas(d)

    for _ in range(0, n):
        rope[0] = (rope[0][0] + dx, rope[0][1] + dy)

        for i in range(1, len(rope)):
            rope[i] = new_pos(rope[i], rope[i-1])


        visited.add(rope[-1])

print(len(visited))









