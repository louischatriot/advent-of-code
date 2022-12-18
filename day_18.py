from time import time

with open("inputs/day_18_example.data") as file:
    lines = [line.rstrip() for line in file]


cubes = [tuple([int(c) for c in l.split(',')]) for l in lines]




# Part 1

res = 0

for c in cubes:
    free_sides = 6

    for cc in cubes:
        if c == cc:
            continue

        if (abs(c[0] - cc[0]) == 1 and c[1] == cc[1] and c[2] == cc[2]) or (abs(c[1] - cc[1]) == 1 and c[0] == cc[0] and c[2] == cc[2]) or (abs(c[2] - cc[2]) == 1 and c[1] == cc[1] and c[0] == cc[0]):
               free_sides -= 1

    res += free_sides

print(res)



# Part 2





