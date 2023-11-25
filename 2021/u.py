import re
from collections import defaultdict

# Regexes
all_lowercase = re.compile('^[a-z]+$')

def split_at_char(s, n):
    l = s[0:n]
    r = s[n:]
    return (l, r)


ortho_neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
all_neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def get_pos(arr, i, j, di, dj, default):
    if not (0 <= i + di < len(arr)):
        return default

    if not (0 <= j + dj < len(arr[i])):
        return default

    else:
        return arr[i+di][j+dj]


def get_visible(arr, i, j, di, dj):
    while (0 <= i + di < len(arr)) and (0 <= j + dj < len(arr[i])):
        i += di
        j += dj
        if arr[i][j] != '.':
            return arr[i][j]

    return '.'


# Assuming same size
def compare_2d_arrays(a1, a2):
    for i in range(0, len(a1)):
        for j in range(0, len(a1[0])):
            if a1[i][j] != a2[i][j]:
                return False

    return True


def __aps(res, rem):
    if len(rem) == 0:
        return res

    r, rem = rem[0], rem[1:]

    newres = []
    for v in res:
        newres.append(v)
        newres.append(v + r)

    return __aps(newres, rem)


def all_partial_sums(l):
    return __aps([0], l)


def is_all_lowercase(s):
    return all_lowercase.match(s) is not None


def frequencies(iterable):
    f = defaultdict(lambda: 0)
    for c in iterable:
        f[c] += 1
    return f


# If iterable is a dict it's already calculated frequencies
def most_common(iterable):
    if type(iterable) == dict or type(iterable) == defaultdict:
        f = iterable
    else:
        f = frequencies(iterable)

    M = min(list(f.values()))
    k0 = None
    for k, v in f.items():
        if v >= M:
            k0 = k
            M = v
    return k0, f[k0]


# If iterable is a dict it's already calculated frequencies
def least_common(iterable):
    if type(iterable) == dict or type(iterable) == defaultdict:
        f = iterable
    else:
        f = frequencies(iterable)

    m = max(list(f.values()))
    k0 = None
    for k, v in f.items():
        if v <= m:
            k0 = k
            m = v
    return k0, f[k0]





