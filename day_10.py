with open("inputs/day_10.data") as file:
    lines = [line.rstrip() for line in file]

series = [1]

for line in lines:
    series.append(series[-1])

    if line[0:4] == 'addx':
        v = int(line[5:])
        series.append(series[-1] + v)

# Part 1
res = 0
for i in [20, 60, 100, 140, 180, 220]:
    res += i * series[i - 1]

print(res)
