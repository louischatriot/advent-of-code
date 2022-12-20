from time import time

with open("inputs/day_20_example.data") as file:
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

print(data)
print(positions)

print("===========================")
print("===========================")


for i0, v in enumerate(data):
    print("===============================", i0, v)
    _from = positions[i0]
    _to = _from + v

    # print("from ", _from, " to ", _to)


    if v == 0:
        pass

    elif v > 0:
        if _to < N:
            for i in range(0, N):
                if _from < positions[i] <= _to:
                    positions[i] -= 1

        else:
            _to = _to - N + 1
            for i in range(0, N):
                if _to <= positions[i] < _from:
                    positions[i] += 1


    elif v < 0:
        if _to > 0:
            for i in range(0, N):
                if _to <= positions[i] < _from:
                    positions[i] += 1

        else:
            _to = _to + N - 1
            print("%%%%")
            print(_to)
            for i in range(0, N):
                if _from < positions[i] <= _to:
                    positions[i] -= 1

    positions[i0] = _to
    print("POS ", positions)



    l = get_list(data, positions)
    print(l)



