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


# Part 2

screen = ['', '', '', '', '', '']

for i in range(1, len(series)):
    l = (i - 1) // 40
    p = (i - 1) - 40 * l

    if series[i - 1] - 1 <= p <= series[i - 1] + 1:
        screen[l] += '#'
    else:
        screen[l] += '.'

screen = '\n'.join(screen)
print(screen)

