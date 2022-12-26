from time import time

with open("inputs/day_24_example.data") as file:
    lines = [line.rstrip() for line in file]

blizzards = []


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
            blizzards.append((x-1, y-1, c))




print(start)
print(end)

print("=================")
print(N, M)


for b in blizzards:
    print(b)


