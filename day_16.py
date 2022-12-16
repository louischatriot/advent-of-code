with open("inputs/day_16_example.data") as file:
    lines = [line.rstrip() for line in file]

valves = dict()

for line in lines:
    line = line[6:]
    name = line[0:2]
    line = line[17:]

    n, line = line.split(';')
    n = int(n)

    line = line[23:]
    if line[0] == ' ':
        line = line[1:]

    dests = line.split(' ')
    valves[name] = { 'flow': n, 'dests': dests }



print(valves)

