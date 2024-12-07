import itertools
import heapq
import re
from collections import defaultdict
import math
import numpy
import hashlib

VERY_BIG = 9999999999

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


# Assumes square matrix
def diagonals(matrix):
    N = len(matrix)
    for dn in range(N):
        yield [matrix[d][dn-d] for d in range(dn+1)]

    for dn in range(N-1):
        yield [matrix[N-1-dn+d][N-1-d] for d in range(dn+1)]

    for dn in range(N):
        yield [matrix[N-1-dn+d][d] for d in range(dn+1)]

    for dn in range(N-1):
        yield [matrix[d][N-1-dn+d] for d in range(dn+1)]


def transpose(matrix):
    N, M = len(matrix), len(matrix[0])
    res = [[None for _ in range(N)] for _ in range(M)]
    for i, j in itertools.product(range(N), range(M)):
        res[j][i] = matrix[i][j]

    return res


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



def bfs_matrix(matrix, i, j, wall='#', empty='.', stop_at_non_empty=True):
    N, M = len(matrix), len(matrix[0])

    to_explore=[((i, j), 0)]
    res = defaultdict(lambda: 9999999999)  # Oh oh oh
    explored = set()

    while len(to_explore) > 0:
        coords, distance = to_explore.pop(0)
        i0, j0 = coords

        if (i0, j0) in explored:
            continue

        for i, j, v in ortho_neighbours_iterator(matrix, i0, j0):
            if (i, j) in explored or v == wall:
                continue

            if v == empty:
                to_explore.append(((i, j), distance+1))
            else:
                res[(i, j)] = min(distance+1, res[(i, j)])
                if not stop_at_non_empty:
                    to_explore.append(((i, j), distance+1))

        explored.add((i0, j0))

    res = [(n, res[n]) for n in res.keys()]
    return res




class Graph:
    def __init__(self):
        self.nodes = list()
        self.edges = defaultdict(lambda: dict())

    def add_node(self, node):
        # O(n) but not an issue for the small AoC graphs
        if node not in self.nodes:
            self.nodes.append(node)

    def add_directed_node(self, a, b, distance):
        self.add_node(a)
        self.add_node(b)

        if b in self.edges[a]:
            raise ValueError("Trying to add the same edge twice")

        self.edges[a][b] = distance

    # Get best paths between two nodes
    # If full is True we get all best path between two nodes
    # If full is False only the minimum set of edges i.e. if c is between a and b, no a to b edge
    def create_from_matrix(self, matrix, wall='#', empty='.', full=False):
        nodes = list()

        for ix, jx in itertools.product(range(len(matrix)), range(len(matrix[0]))):
            if matrix[ix][jx] not in [wall, empty]:
                nodes.append((ix, jx, matrix[ix][jx]))

        for ia, ja, a in nodes:
            for coords, distance in bfs_matrix(matrix, ia, ja, wall, empty, not full):
                ib, jb = coords
                b = matrix[ib][jb]
                self.add_directed_node(a, b, distance)

    # Get all best paths between two nodes
    def create_full_from_matrix(self, matrix, wall='#', empty='.'):
        pass


    def print(self):
        print("=============================================================")
        print(f"NODES: {', '.join(self.nodes)}")
        for n in self.nodes:
            print(f"-- {n} => {', '.join([m + ' (' + str(d) + ')' for m, d in self.edges[n].items()])}")
        print("=============================================================")

    def clone(self):
        g = Graph()

        for n in self.nodes:
            g.add_node(n)
            for m, d in self.edges[n].items():
                g.add_directed_node(n, m, d)

        return g

    def remove_node(self, node):
        # My chosen data structure is really not the right one I am ashamed
        # but too lazy to change and for small graphs performance does not change much
        prevs = list()

        for m in self.nodes:
            if m != node:
                for nn, d in self.edges[m].items():
                    if nn == node:
                        prevs.append((m, d))

        for p, dp in prevs:
            del self.edges[p][node]

            for n, dn in self.edges[node].items():
                if n != p:  # Assume we don't want to create cycles
                    if n in self.edges[p]:
                        self.edges[p][n] = min(self.edges[p][n], dp + dn)
                    else:
                        self.edges[p][n] = dp + dn

        self.nodes = [n for n in self.nodes if n != node]
        del self.edges[node]

    def get_shortest_path_covering_all_nodes(self, start = None):
        if start is None:
            start = self.nodes[0]

        if len(self.nodes) == 1:
            return 0, [start]

        best_d = 999999999  # Uh uh uh
        best_path = None

        for n, d in self.edges[start].items():
            g = self.clone()
            g.remove_node(start)
            dist, path = g.get_shortest_path_covering_all_nodes(n)

            if dist + d < best_d:
                best_d = dist + d
                best_path = [start] + path

        return best_d, best_path

    # Super basic version, less efficient but on small inputs it works
    def tsp(self, start, return_home = False):
        res = VERY_BIG
        for l in itertools.permutations(self.nodes):
            if l[0] != start:
                continue

            path = [n for n in l]

            if return_home is True:
                path.append(start)

            res = min(res, sum([self.edges[a][b] for a, b in pairwise(path)]))

        return res










