from time import time

with open("inputs/day_20.data") as file:
    lines = [line.rstrip() for line in file]

data = [int(n) for n in lines]
N = len(data)

# positions[i] == j means that the ith number in data is in jth position
positions = [i for i in range(0, N)]

def get_list(data, positions):
    res = [None for _ in range(0, N)]

    for i, j in enumerate(positions):
        res[j] = data[i]

    return res


for i0, v in enumerate(data):
    log = (0 <= i0 <= 5) or True

    _from = positions[i0]
    _to = _from + v

    while _to < 0:
        _to = _to + N - 1

    while _to >= N:
        _to = _to - N + 1

    if v != 0:
        if _from < _to:
            for i in range(0, N):
                if _from < positions[i] <= _to:
                    positions[i] -= 1

        else:
            for i in range(0, N):
                if _to <= positions[i] < _from:
                    positions[i] += 1

    positions[i0] = _to



l = get_list(data, positions)

i0 = l.index(0)

res = l[(i0 + 1000) % N] + l[(i0 + 2000) % N] + l[(i0 + 3000) % N]

print(res)


















