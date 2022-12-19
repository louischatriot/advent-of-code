from time import time

with open("inputs/day_19_example.data") as file:
    lines = [line.rstrip() for line in file]


# I refuse to use regex to parse :)
blueprints = dict()
for line in lines:
    line = line[10:]

    blueprint_n, line = line.split(': ')
    blueprint_n = int(blueprint_n)

    line = line.split('. ')
    line[-1] = line[-1][0:len(line[-1])-1]
    line = [it[5:] for it in line]
    line = [it.split(' robot costs ') for it in line]

    robots_costs = dict()
    for r in line:
        kind, cost = r
        cost = cost.split(' and ')

        costs = dict()
        for c in cost:
            amt, ressource = c.split(' ')
            costs[ressource] = int(amt)

        robots_costs[kind] = costs

    blueprints[blueprint_n] = robots_costs


print(blueprints)


