import itertools
import heapq
import re
from collections import defaultdict
import math

# Regexes
all_lowercase = re.compile('^[a-z]+$')

def split_at_char(s, n):
    l = s[0:n]
    r = s[n:]
    return (l, r)

hex_to_binary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111' }

ortho_neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
all_neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
all_neighbours_and_center = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

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


# Tasks are strings
REMOVED = '<removed-item>'
class PriorityQueue:

    def __init__(self):
        self.pq = []
        self.entry_finder = {}

    def get_task(self, task):
        entry = self.entry_finder[task]
        return (task, entry[0])

    def add_task(self, task, priority):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        entry = [priority, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, task = heapq.heappop(self.pq)
            if task != REMOVED:
                del self.entry_finder[task]
                return (task, priority)

        return None, None


# TODO: implement using best_predecessors to also give the path itself
def do_dijkstra(nodes, edges, start_node, end_node):
    # Should take sum of all distances to be sure
    upper_bound = 99999999999999
    distances = PriorityQueue()
    unvisited = set()
    best_predecessors = dict()

    for node in nodes:
        if node == start_node:
            distances.add_task(node, 0)
        else:
            distances.add_task(node, upper_bound)

        unvisited.add(node)

    while True:
        current, current_dist = distances.pop_task()

        if current == end_node:
            return current_dist

        for new_state, d in edges[current]:

            if new_state in unvisited:
                _, dist = distances.get_task(new_state)
                dist = min(dist, d + current_dist)
                distances.add_task(new_state, dist)

                best_predecessors[new_state] = current

        unvisited.remove(current)


def lcm(a, b):
    return a * b // math.gcd(a, b)


# nodes set ; edges dict of start, set of ends
# https://en.wikipedia.org/wiki/Topological_sorting
def topological_sort(nodes, edges):
    incoming_edges = defaultdict(lambda: set())

    for start, ends in edges.items():
        for end in ends:
            incoming_edges[end].add(start)

    L = list()

    # S initially all nodes with no incoming edges
    S = set()
    removed_edges = set()  # So as not to modify edges
    for node in nodes:
        if node not in incoming_edges:
            S.add(node)

    while len(S) > 0:
        node = S.pop()
        L.append(node)

        for m in edges[node]:
            if (node, m) in removed_edges:
                continue

            incoming_edges[m].remove(node)
            removed_edges.add((node, m))

            if len(incoming_edges[m]) == 0:
                S.add(m)
                del incoming_edges[m]

    return L










