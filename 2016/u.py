import itertools
import heapq
import re
from collections import defaultdict
import math
import numpy
import hashlib

# Regexes
all_lowercase = re.compile('^[a-z]+$')

def split_at_char(s, n):
    l = s[0:n]
    r = s[n:]
    return (l, r)

hex_to_binary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111' }

letters = [chr(i) for i in range(97, 123)]

ortho_neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
all_neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
all_neighbours_and_center = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

def ortho_neighbours_iterator(data, i, j):
    I, J = len(data), len(data[0])

    for di, dj in ortho_neighbours:
        if 0 <= i+di < I and 0 <= j+dj < J:
            yield (i+di, j+dj, data[i+di][j+dj])


def neighbours_not_center_iterator(data, i, j):
    I, J = len(data), len(data[0])

    for di, dj in all_neighbours:
        if 0 <= i+di < I and 0 <= j+dj < J:
            yield (i+di, j+dj, data[i+di][j+dj])


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

    def length(self):
        return len(self.pq)


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


def fast_modular_exp(b, exp, m):
    res = 1
    while exp > 1:
        if exp & 1:
            res = (res * b) % m
        b = b ** 2 % m
        exp >>= 1
    return (b * res) % m


def primes_until_n(n):
    n += 1
    sieve = numpy.ones(n//2, dtype=bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return [2] + list(2*numpy.nonzero(sieve)[0][1::]+1)


def get_prime_factors(n, primes = None):
    if primes is None:
        primes = primes_until_n(math.floor(math.sqrt(n)) + 1)

    res = []

    for p in primes:
        if p > n:
            break

        while n % p == 0:
            res.append(p)
            n = n // p

    return res


# Would be much more efficient to use a Erathostène's sieve like approach to calculate many of those sums
# See 2015 day 20
def sum_of_divisors(n, primes = None):
    prime_factors = get_prime_factors(n, primes)

    res = set()

    for L in range(len(prime_factors) + 1):
        for subset in itertools.combinations(prime_factors, L):
            res.add(math.prod(subset))

    return sum(res)


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def generate_md5(contents):
    h = hashlib.new('md5')
    contents = bytes(contents, 'ascii')
    h.update(contents)
    return h.hexdigest()


class DoubleLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = self
        self.prev = self

    def __str__(self):
        return f"<DLL> {self.value} ; previous {self.prev.value} ; next {self.next.value}"

    def add_after(self, dll):
        self.prev = dll
        dll.next = self

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev



def bfs_matrix_until_non_empty(matrix, i, j, wall='#', empty='.'):
    N, M = len(matrix), len(matrix[0])

    to_explore=[((i, j), 0)]
    res = list()
    explored = set()
    explored.add((i, j))

    while len(to_explore) > 0:
        coords, distance = to_explore.pop()
        i0, j0 = coords

        for i, j, v in ortho_neighbours_iterator(matrix, i0, j0):
            if (i, j) in explored or v == wall:
                continue

            if v == empty:
                to_explore.append(((i, j), distance+1))
            else:
                res.append(((i, j), distance+1))

        explored.add((i0, j0))

    return res


class Graph:
    def __init__(self):
        self.nodes = list()
        self.edges = dict()

    def add_node(self, node):
        # O(n) but not an issue for the small AoC graphs
        if node not in self.nodes:
            self.nodes.append(node)
            self.edges[node] = list()

    def add_undirected_edge(self, a, b, distance):
        self.add_node(a)
        self.add_node(b)

        # O(n) also but oh well
        for n, _ in self.edges[a]:
            if n == b:
                raise ValueError("Trying to add the same edge twice")

        for n, _ in self.edges[b]:
            if n == a:
                raise ValueError("Trying to add the same edge twice")

        self.edges[a].append((b, distance))
        self.edges[b].append((a, distance))

    def add_directed_node(self, a, b, distance):
        self.add_node(a)
        self.add_node(b)

        for n, _ in self.edges[a]:
            if n == b:
                raise ValueError("Trying to add the same edge twice")

        self.edges[a].append((b, distance))
            
    def create_from_matrix(self, matrix, start, wall='#', empty='.'):
        i, j = -1, -1
        nodes = list()
        for ix, jx in itertools.product(range(len(matrix)), range(len(matrix[0]))):
            if matrix[ix][jx] == start:
                i, j = ix, jx
            
            if matrix[ix][jx] not in [wall, empty]:
                nodes.append((ix, jx, matrix[ix][jx]))


        for ia, ja, a in nodes:
            for coords, distance in bfs_matrix_until_non_empty(matrix, ia, ja, wall, empty):
                ib, jb = coords
                b = matrix[ib][jb]

                self.add_directed_node(a, b, distance)

    def print(self):
        print(f"NODES: {', '.join(self.nodes)}")
        for n in self.nodes:
            print(f"-- {n} => {', '.join([m + ' (' + str(d) + ')' for m, d in self.edges[n]])}")













