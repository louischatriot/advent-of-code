with open("inputs/day_1.data") as file:
    lines = [line.rstrip() for line in file]

dwarfs = []
current = 0
for l in lines:
    if l == "":
        dwarfs.append(current)
        current = 0
    else:
        current += int(l)

dwarfs = sorted(dwarfs)

# Part 1
print(dwarfs[-1])

# Part 2
print(dwarfs[-1] + dwarfs[-2] + dwarfs[-3])


