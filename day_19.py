from time import time

with open("inputs/day_19.data") as file:
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
        blueprints[blueprint_n]['max_useful'][robot] = max([blueprints[blueprint_n]['bp'][rr].get(robot, 0) for rr in blueprints[blueprint_n]['bp'].keys()])
        if robot == 'geode':
            blueprints[blueprint_n]['max_useful'][robot] = 200   # We do want as many geode robots as possible



def can_build(bp, resources, robot):
    for r in bp[robot]:
        if resources.get(r, 0) < bp[robot][r]:
            return False
    return True


def time_until_next_robot(bp, resources, robots):
    _resources = {k:v for k,v in resources.items()}
    for res in range(0, bp['ore']['ore'] + 1):   # We know we have at least one ore robot so we have an upper bound to the time to next robot
        if any(can_build(bp, _resources, robot) for robot in bp):
            return res

        for r, amt in robots.items():
            _resources[r] += amt



def time_until_can_build(bp, resources, robots, robot):
    if can_build(bp, resources, robot):
        return 0

    if any([robots[r] == 0 and resources[r] < bp[robot][r] for r in bp[robot]]):
        return -1

    _resources = {k:v for k,v in resources.items()}
    res = 0
    while True:
        if can_build(bp, _resources, robot):
            return res
        else:
            for r, amt in robots.items():
                _resources[r] += amt
            res += 1


def get_robots_from_builds(builds):
    robots = dict()
    for robot in blueprints[1]['bp']:
        robots[robot] = 0
    for robot, t in builds:
        robots[robot] += 1
    return robots



def dfs_simple(blueprint, resources, robots, remaining_time):
    if remaining_time == 1:
        return resources['geode'] + robots['geode']

    # Case = not building anything anymore
    score = resources['geode'] + remaining_time * robots['geode']

    bp = blueprint['bp']
    max_useful = blueprint['max_useful']

    # Building list of robots that we may want to build
    to_build = [robot for robot in robots if robots[robot] < max_useful[robot]]
    to_build_time = []
    for robot in to_build:
        if not all([resources[r] >= bp[robot][r] or robots[r] > 0 for r in bp[robot]]):
            continue

        t = 0
        while not all(resources[r] + robots[r] * t >= bp[robot][r] for r in bp[robot]):
            t += 1

        if t < remaining_time:
            to_build_time.append((robot, t))

    # Case = building one robot
    for robot, t in to_build_time:
        _resources = {k:v for k,v in resources.items()}
        _robots = {k:v for k,v in robots.items()}

        # Build robot
        for r in bp[robot]:
            _resources[r] -= bp[robot][r]

        # New robot not yet built here, hence using robots not _robots
        for r, amt in robots.items():
            _resources[r] += amt * (t + 1)

        _robots[robot] += 1

        _score = dfs_simple(blueprint, _resources, _robots, remaining_time - t - 1)

        if _score > score:
            score = _score

    # Return best path
    return score




# Part 1 and 2

bp_test = blueprints[1]
print(bp_test)

start = time()


res = 0

for bpi, blueprint in blueprints.items():

    start_resources = {r:0 for r in bp_test['bp']}
    start_robots = {r:0 if r != 'ore' else 1 for r in bp_test['bp']}
    score = dfs_simple(blueprint, start_resources, start_robots, 32)

    print("================================")
    print(bpi)
    print(score)

    res += bpi * score

print("==> Duration", time() - start)
print(res)

