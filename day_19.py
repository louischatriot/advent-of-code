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

    blueprints[blueprint_n] = dict()
    blueprints[blueprint_n]['bp'] = robots_costs
    blueprints[blueprint_n]['max_useful'] = dict()
    for robot in blueprints[blueprint_n]['bp']:
        print(blueprints[blueprint_n]['bp'][robot])



        blueprints[blueprint_n]['max_useful'][robot] = max([blueprints[blueprint_n]['bp'][rr].get(robot, 0) for rr in blueprints[blueprint_n]['bp'].keys()])


print(blueprints)

1/0




def can_build(blueprint, resources, robot):
    for r in blueprint[robot]:
        if resources.get(r, 0) < blueprint[robot][r]:
            return False
    return True


def time_until_next_robot(blueprint, resources, robots):
    _resources = {k:v for k,v in resources.items()}
    for res in range(0, blueprint['ore']['ore'] + 1):   # We know we have at least one ore robot so we have an upper bound to the time to next robot
        if any(can_build(blueprint, _resources, robot) for robot in blueprint):
            return res

        for r, amt in robots.items():
            _resources[r] += amt



def time_until_can_build(blueprint, resources, robots, robot):
    _resources = {k:v for k,v in resources.items()}
    res = 0






# Part 1
def dfs(blueprint, resources, robots, remaining_time):
    # print("====================================", remaining_time, resources, robots)


    if remaining_time == 0:
        return resources, robots

    # if resources['geode'] >= 7:
        # print(remaining_time, resources['geode'])


    # That should not work, actually, as we can construct more geode robots
    # if remaining_time + resources['geode'] <= 9:
        # return resources, robots

    t = time_until_next_robot(blueprint, resources, robots)
    t = min(t, remaining_time)

    # Produce during these t units of time
    _resources = {k:v for k,v in resources.items()}
    for r, amt in robots.items():
        _resources[r] += amt * t
    resources = _resources

    if remaining_time - t == 0:
        return resources, robots

    # Not building anything
    _resources = {k:v for k,v in resources.items()}
    # _robots = {k:v for k,v in robots.items()}
    for r, amt in robots.items():
        _resources[r] += amt

    __res, __rob = dfs(blueprint, _resources, robots, remaining_time - t - 1)


    score = __res['geode']
    resources_optim = __res
    robots_optim = __rob


    # Building one robot (not handling case where multiple robots are built at once, not sure it's possible from the docs)
    for robot in blueprint:
        # CHECK FOR MAX USEFUL HERE
        if can_build(blueprint, resources, robot):
            _resources = {k:v for k,v in resources.items()}
            _robots = {k:v for k,v in robots.items()}

            for r in blueprint[robot]:
                _resources[r] -= blueprint[robot][r]

            _robots[robot] += 1

            for r, amt in _robots.items():
                _resources[r] += amt

            __res, __rob = dfs(blueprint, _resources, _robots, remaining_time - t - 1)
            if __res['geode'] > score:
                resources_optim = __res
                robots_optim = __rob

    return resources_optim, robots_optim



bp_test = {
    'ore': {'ore': 2},
    'clay': {'ore': 2},
    'obsidian': {'clay': 2, 'ore': 1},
    'geode': {'obsidian': 1},
}

bp_test = blueprints[1]


start = time()

res, rob = dfs(bp_test, {r:0 for r in blueprints[1]}, {r:0 if r != 'ore' else 1 for r in blueprints[1]}, 24)

print("================================")
print(res)
print(rob)

print("==> Duration", time() - start)


