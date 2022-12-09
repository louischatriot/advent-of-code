with open("inputs/day_9.data") as file:
    lines = [line.rstrip() for line in file]

movements = [(line[0], int(line[2:])) for line in lines]


# Part 1

tx, ty, hx, hy = 0, 0, 0, 0
visited = set()
visited.add((tx, ty))

for d, n in movements:
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

    for _ in range(0, n):
        hx += dx
        hy += dy

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

        visited.add((tx, ty))


print(len(visited))



