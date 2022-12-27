from time import time
from math import gcd

with open("inputs/day_24.data") as file:
    lines = [line.rstrip() for line in file]

blizzards_start = list()


# My gooooooood
N = len(lines) - 2
M = len(lines[0]) - 2
start = (-1, 0)
end = (N, M-1)

for x, line in enumerate(lines):
    if line[4] == '#':
        continue   # I don't respect myself anymore

    for y, c in enumerate(line):
        if c != '.' and c != '#':
            blizzards_start.append((x-1, y-1, c))

R = N * M // gcd(N, M)
blizzards = []

blizzards.append({b for b in blizzards_start})

# Blizzard number R is the same as blizzard 0
for _ in range(0, R-1):
    s = set()
    for x, y, d in blizzards[-1]:
        dx = -1 if d == '^' else (1 if d == 'v' else 0)
        dy = -1 if d == '<' else (1 if d == '>' else 0)
        s.add(((x + dx) % N, (y + dy) % M, d))

    blizzards.append(s)


blizzards_pos = [{(b[0], b[1]) for b in bliz} for bliz in blizzards]


print("Blizzards set up, start part 1")
print(N, M)


done = set()
to_do = [(-1, 0, 0)]
deltas = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx == 0 or dy == 0]

while len(to_do) > 0:
    x, y, r = to_do.pop(0)

    if (x, y, r%R) in done:
        # print("caca")
        continue
    done.add((x, y, r%R))

    r += 1
    for dx, dy in deltas:
        if (0 <= x+dx < N and 0 <= y+dy < M and (x+dx, y+dy) not in blizzards_pos[r%R]) or (x+dx == -1 and y+dy == 0):
            to_do.append((x+dx, y+dy, r))
            if x+dx == N-1 and y+dy == M-1:
                print("PART 1 RESULT: ", r+1)   # One last step needed to escape the maze
                1/0





