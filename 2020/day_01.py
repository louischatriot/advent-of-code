import sys

fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if len(sys.argv) > 1 else '') + '.data'

# with open("inputs/day_01.data") as file:
with open(fn) as file:
    lines = [line.rstrip() for line in file]

data = [int(l) for l in lines]
datad = {d for d in data}

for d in data:
    if (2020 - d) in datad:
        res = d * (2020 - d)
        break

# PART 1
print(res)

for i in range(0, len(data)):
    for j in range(i + 1, len(data)):
        if (2020 - data[i] - data[j]) in datad:
            res = data[i] * data[j] * (2020 - data[i] - data[j])
            break

# PART 2
print(res)




