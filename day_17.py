from time import time

with open("inputs/day_17.data") as file:
    lines = [line.rstrip() for line in file]

jets = lines[0]


rocks = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)]
]

# There will be a cycle of lcm(R, N) somewhere
R = len(rocks)
J = len(jets)

def get_new_line():
    return ['|', '.', '.', '.', '.', '.', '.', '.', '|']


height = 1
rounds = 1875

matrix = [ ['+', '—', '—', '—', '—', '—', '—', '—', '+'] ]

r = 0
j = 0
while True:

    # This code is for part 2, to identify the first set up, loop size, and
    # deduct the end sequence, height from start and end sequence and how many loops
    # Too lazy to code it I used Gsheets to do the math

    # if (j - 1) % J == 0:
        # print(r, r % R, height)

    # if r % R == 0 and j % J == 0 and r != 0:
        # break


    rock = rocks[r % R]
    r += 1

    for _ in range(0, height + 7 - len(matrix)):
        matrix.append(get_new_line())

    px, py = 3, height + 3

    while True:
        jet = jets[j % J]
        j += 1
        check = 1 if jet == '>' else -1

        if all([matrix[py + ry][px + rx + check] == '.' for rx, ry in rock]):
            px += check

        if all([matrix[py- 1 + ry][px + rx] == '.' for rx, ry in rock]):
            py -= 1
        else:
            for rx, ry in rock:
                matrix[py + ry][px + rx] = '#'
                height = max(height, py + ry + 1)

            break


    if r >= rounds:
        break



print("HEIGHT", height - 1)
# print('\n'.join([' '.join(l) for l in reversed(matrix)]))
