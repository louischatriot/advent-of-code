with open("inputs/day_14.data") as file:
    lines = [line.rstrip() for line in file]

def line_to_checkpoints(line):
    line = line.split(' -> ')
    line = [cp.split(',') for cp in line]
    line = [(int(cp[0]), int(cp[1])) for cp in line]
    return line

lines = [line_to_checkpoints(line) for line in lines]


sand_x = 500
sand_y = 0
min_x = max_x = sand_x
min_y = max_y = sand_y

for l in lines:
    for cp in l:
        min_x = min(min_x, cp[0])
        max_x = max(max_x, cp[0])
        min_y = min(min_y, cp[1])
        max_y = max(max_y, cp[1])


N = max_y - min_y + 1
M = max_x - min_x + 1

N += 1
M += 2 * N
min_x -= N

# Indexed y, x
cave = [['.' for _ in range(0, M)] for _ in range(0, N)]
cave += [['#' for _ in range(0, M)]]
N += 1

for l in lines:
    if len(l) == 1:
        cave[l[0][1]][l[0][0]] = '#'
        continue

    for i in range(0, len(l) - 1):
        cps = l[i]
        cpe = l[i+1]

        if cps[0] == cpe[0]:
            delta = 1 if cpe[1] > cps[1] else -1
            current_y = cps[1]
            while True:
                cave[current_y - min_y][cps[0] - min_x] = '#'
                if current_y == cpe[1]:
                    break
                current_y += delta

        else:
            delta = 1 if cpe[0] > cps[0] else -1
            current_x = cps[0]
            while True:
                cave[cps[1] - min_y][current_x - min_x] = '#'
                if current_x == cpe[0]:
                    break
                current_x += delta

# print("===================================")
# print("===================================")
# print('\n'.join([' '.join(l) for l in cave]))



# Assumes everthing is empty when outside of coordinates
def get_contents(cave, cy, cx):
    if cy < 0 or cy >= N:
        return '.'

    if cx < 0 or cx >= M:
        return '.'

    return cave[cy][cx]

# Part 1 and 2

sands = 0
while True:
    finished = False
    cx = sand_x - min_x
    cy = sand_y - min_y

    while True:
        if not (0 <= cy < N and 0 <= cx < M):
            finished = True
            break

        if get_contents(cave, cy+1, cx) == '.':
            cy += 1
        elif get_contents(cave, cy+1, cx-1) == '.':
            cy += 1
            cx -= 1
        elif get_contents(cave, cy+1, cx+1) == '.':
            cy += 1
            cx += 1
        else:
            if cx == sand_x - min_x and cy == sand_y - min_y:
                finished = True

            sands += 1
            cave[cy][cx] = 'o'
            break

    if finished:
        break

print(sands)

print("===================================")
print("===================================")
# print('\n'.join([' '.join(l) for l in cave]))









