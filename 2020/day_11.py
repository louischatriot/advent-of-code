import sys
import re
import u as u
from collections import defaultdict

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
arrangement = [[c for c in l] for l in lines]
neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def get_next(arrangement):
    res = [['.' for j in range(0, len(arrangement[0]))] for i in range(0, len(arrangement))]

    for i in range(0, len(arrangement)):
        for j in range(0, len(arrangement[i])):
            if arrangement[i][j] == 'L' and not any([u.get_pos(arrangement, i, j, di, dj) == '#' for (di, dj) in neighbours]):
                res[i][j] = '#'
            elif arrangement[i][j] == '#' and sum([1 if u.get_pos(arrangement, i, j, di, dj) == '#' else 0 for (di, dj) in neighbours]) >= 4:
                res[i][j] = 'L'
            else:
                res[i][j] = arrangement[i][j]

    return res

def get_last(arrangement, fn):
    arr = fn(arrangement)

    while not u.compare_2d_arrays(arr, arrangement):
        arrangement = arr
        arr = fn(arr)

    return arr

arr = get_last(arrangement, get_next)
res = sum([sum([1 if c == '#' else 0 for c in a]) for a in arr])
print(res)


# PART 2
# Could have used get next above but oh well
def get_next_visible(arrangement):
    res = [['.' for j in range(0, len(arrangement[0]))] for i in range(0, len(arrangement))]

    for i in range(0, len(arrangement)):
        for j in range(0, len(arrangement[i])):
            if arrangement[i][j] == 'L' and not any([u.get_visible(arrangement, i, j, di, dj) == '#' for (di, dj) in neighbours]):
                res[i][j] = '#'
            elif arrangement[i][j] == '#' and sum([1 if u.get_visible(arrangement, i, j, di, dj) == '#' else 0 for (di, dj) in neighbours]) >= 5:
                res[i][j] = 'L'
            else:
                res[i][j] = arrangement[i][j]

    return res

arr = get_last(arrangement, get_next_visible)
res = sum([sum([1 if c == '#' else 0 for c in a]) for a in arr])
print(res)


