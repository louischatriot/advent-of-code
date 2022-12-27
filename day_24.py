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
deltas = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx == 0 or dy == 0]


print("Blizzards set up")


# Assuming the end is in the grid :)
def steps(start_round, start, end):
    xs, ys = start
    to_do = [(xs, ys, start_round)]
    xe, ye = end
    done = set()

    while len(to_do) > 0:
        x, y, r = to_do.pop(0)
        if (x, y, r%R) in done:
            continue
        done.add((x, y, r%R))

        r += 1
        for dx, dy in deltas:
            if (0 <= x+dx < N and 0 <= y+dy < M and (x+dx, y+dy) not in blizzards_pos[r%R]) or (x+dx == xs and y+dy == ys):
                to_do.append((x+dx, y+dy, r))
                if x+dx == xe and y+dy == ye:
                    return r+1-start_round   # One last step needed to escape the maze


# Part 1
res = steps(0, (-1, 0), (N-1, M-1))
print("PART 1:", res)


# Part 2
r1 = steps(0, (-1, 0), (N-1, M-1))
print(r1)

r2 = steps(r1, (N, M-1), (0, 0))
print(r2)

r3 = steps(r1+r2, (-1, 0), (N-1, M-1))
print(r3)

print("PART 2 TOTAL:", r1 + r2 + r3)




