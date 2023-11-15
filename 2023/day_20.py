from time import time

with open("inputs/day_20.data") as file:
    lines = [line.rstrip() for line in file]

data = [int(n) for n in lines]
N = len(data)


def get_list(data, positions):
    res = [None for _ in range(0, N)]

    for i, j in enumerate(positions):
        res[j] = data[i]

    return res


def mix(data, rounds=1):
    # positions[i] == j means that the ith number in data is in jth position
    positions = [i for i in range(0, N)]

    for _ in range(0, rounds):

        for i0, v in enumerate(data):
            log = (0 <= i0 <= 5) or True

            _from = positions[i0]
            _to = _from + v

            if _to < 0:
                _to = _to + (N-1) * (abs(_to) // (N-1) - 3)

                while _to < 0:
                    _to = _to + N - 1


            if _to >= N:
                _to = _to - (N-1) * (_to // (N-1) - 3)

                while _to >= N:
                    _to = _to - (N - 1)

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

    return get_list(data, positions)


# Part 1
# l = mix(data)
# i0 = l.index(0)
# res = l[(i0 + 1000) % N] + l[(i0 + 2000) % N] + l[(i0 + 3000) % N]
# print(res)


# Part 2
key = 811589153
data = [v * key for v in data]


l = mix(data, 10)
i0 = l.index(0)
res = l[(i0 + 1000) % N] + l[(i0 + 2000) % N] + l[(i0 + 3000) % N]
print(res)


