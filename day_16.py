from time import time

with open("inputs/day_16.data") as file:
    lines = [line.rstrip() for line in file]

valves = dict()
time_until_eruption = 30
good_valves = 0


for line in lines:
    line = line[6:]
    name = line[0:2]
    line = line[17:]

    n, line = line.split(';')
    n = int(n)

    line = line[23:]
    if line[0] == ' ':
        line = line[1:]

    dests = line.split(', ')
    valves[name] = { 'flow': n, 'dests': dests }
    if n > 0:
        good_valves += 1


paths = dict()

for start in valves:
    paths[start] = {start: 0}
    fringe = [start]
    while len(fringe) > 0:
        c = fringe.pop(0)
        for v in valves[c]['dests']:
            if v not in paths[start]:
                paths[start][v] = paths[start][c] + 1
                fringe.append(v)

for start in paths:
    paths[start] = {v: c for v, c in paths[start].items() if valves[v]['flow'] > 0}

paths = {v: c for v, c in paths.items() if v == 'AA' or valves[v]['flow'] > 0}





def get_score(opened):
    res = 0
    for d in opened:
        res += opened[d] * valves[d]['flow']
    return res


# Part 1, DFS

def search(opened, pos, remaining_time):
    if remaining_time <= 1 or len(opened) >= good_valves:
        return opened, get_score(opened)

    score = get_score(opened)
    res = opened

    for v, t in paths[pos].items():
        if v not in opened and remaining_time - t - 1 > 0:
            _opened = { k: v for k, v in opened.items() }
            _opened[v] = remaining_time - t - 1

            o, s = search(_opened, v, remaining_time - t - 1)
            if s > score:
                score = s
                res = o

    return res, score



start = time()

res = search(dict(), "AA", 30)
print(res)

print(time() - start)

print("=================================")
print("=================================")
print("=================================")

# Part 1, BFS


def current_time(opened):
    res = 0
    for v, t in opened.items():
        res = max(res, t)
    return res

def get_score_forward(opened):
    res = 0
    for v, t in opened.items():
        res += (30 - t) * valves[v]['flow']
    return res


# start = time()


# to_test = []
# fringe = [(dict(), 'AA')]

# score = 0
# res = None


# while len(fringe) > 0:
    # opened, pos = fringe.pop()

    # # if get_score_forward(opened) > score:
        # # score = get_score_forward(opened)
        # # res = opened
    # to_test.append(opened)

    # for v, t in paths[pos].items():
        # if v not in opened and current_time(opened) + t + 1 <= 30:
            # _opened = { k: v for k, v in opened.items() }
            # _opened[v] = current_time(_opened) + t + 1
            # fringe.append((_opened, v))



# score = max([get_score_forward(o) for o in to_test])
# for res in to_test:
    # if get_score_forward(res) == score:
        # print(score)
        # print(res)

# print(time() - start)



# Part 2, DFS

def search_two(opened, targeth, targete, ttth, ttte, remaining_time):
    if remaining_time <= 1 or len(opened) >= good_valves:
        return opened, get_score(opened)

    score = get_score(opened)
    res = opened

    if ttth == 0 and ttte > 0:
        for v, t in paths[targeth].items():
            if v not in opened and remaining_time - t - 1 > 0:
                _opened = { k: v for k, v in opened.items() }
                _opened[v] = remaining_time - t - 1

                quantum = min(ttte, t+1)

                o, s = search_two(_opened, v, targete, t+1 - quantum, ttte - quantum, remaining_time - quantum)
                if s > score:
                    score = s
                    res = o

    if ttth > 0 and ttte == 0:
        for v, t in paths[targete].items():
            if v not in opened and remaining_time - t - 1 > 0:
                _opened = { k: v for k, v in opened.items() }
                _opened[v] = remaining_time - t - 1

                quantum = min(ttth, t+1)

                o, s = search_two(_opened, targeth, v, ttth - quantum, t+1 - quantum, remaining_time - quantum)
                if s > score:
                    score = s
                    res = o

    if ttth == 0 and ttte == 0:
        for vh, th in paths[targeth].items():
            if vh not in opened and remaining_time - th - 1 > 0:

                for ve, te in paths[targete].items():
                    if ve not in opened and ve != vh and remaining_time - te - 1 > 0:

                        _opened = { k: v for k, v in opened.items() }
                        _opened[vh] = remaining_time - th - 1
                        _opened[ve] = remaining_time - te - 1

                        quantum = min(th+1, te+1)

                        o, s = search_two(_opened, vh, ve, th+1 - quantum, te+1 - quantum, remaining_time - quantum)
                        if s > score:
                            score = s
                            res = o



    return res, score



start = time()


res, score = search_two(dict(), "AA", "AA", 0, 0, 26)


print("===========================")
print("===========================")
print(res)
print(score)





print(time() - start)
