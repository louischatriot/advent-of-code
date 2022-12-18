from time import time

with open("inputs/day_18.data") as file:
    lines = [line.rstrip() for line in file]


cubes = [tuple([int(c) for c in l.split(',')]) for l in lines]

cube_check = set()
for c in cubes:
    cube_check.add(c)




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

xs = [c[0] for c in cubes]
xmin, xmax = min(xs) - 1, max(xs) + 1

ys = [c[1] for c in cubes]
ymin, ymax = min(ys) - 1, max(ys) + 1

zs = [c[2] for c in cubes]
zmin, zmax = min(zs) - 1, max(zs) + 1

res = 0

fringe = [(xmin, ymin, zmin)]
checked = set()


while len(fringe) > 0:
    cube = fringe.pop(0)

    if cube in checked:
        continue

    x, y, z = cube
    checked.add(cube)

    for cc in [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]:
        if not (xmin <= cc[0] <= xmax and ymin <= cc[1] <= ymax and zmin <= cc[2] <= zmax):
            continue

        if cc in cube_check:
            res += 1
        else:
            if cc not in checked:
                fringe.append(cc)



print(res)


