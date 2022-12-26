from time import time
from math import gcd

with open("inputs/day_24_example.data") as file:
    lines = [line.rstrip() for line in file]

blizzards_start = list()


# My gooooooood
N = len(lines) - 2
M = len(lines[0]) - 2
start = (-1, 0)
end = (N, M-1)

for x, line in enumerate(lines):
    if line[4] == '#':
        continue   # I don't respect myself anymore

    for y, c in enumerate(line):
        if c != '.' and c != '#':
            blizzards_start.append((x-1, y-1, c))

R = N * M // gcd(N, M)
blizzards = []

blizzards.append({b for b in blizzards_start})

# Blizzard number R-1 is the same as blizzard 0
for _ in range(0, R-1):
    s = set()
    for x, y, d in blizzards[-1]:
        dx = -1 if d == '^' else (1 if d == 'v' else 0)
        dy = -1 if d == '<' else (1 if d == '>' else 0)
        s.add(((x + dx) % N, (y + dy) % M, d))

    blizzards.append(s)


blizzards_pos = [{(b[0], b[1]) for b in bliz} for bliz in blizzards]


class Node():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.nexts = []
        self.path = None

    # d can be w for wait
    def add_next(self, node, d):
        self.nexts.append((node, d))

    def get_coords(self):
        return (self.x, self.y)

    def __str__(self):
        return f"<NODE> {self.x}, {self.y} - round {r}"


start_node = Node(start[0], start[1], 0)

next = Node(0, 0, 1)
start_node.add_next(next, 'v')


last_round = [next]



# This is incomplete for certain cases where we need to come back to a node that couldn't be reached after one R of blizzards
for r in range(2, R-1):
    this_round = []

    for node in last_round:
        x, y = node.get_coords()

        if x > 0 and (x-1, y) not in blizzards_pos[r]:
            next = Node(x-1, y, r)
            node.add_next(next, '^')
            this_round.append(next)

        if x < N-1 and (x+1, y) not in blizzards_pos[r]:
            next = Node(x+1, y, r)
            node.add_next(next, 'v')
            this_round.append(next)

        if y > 0 and (x, y-1) not in blizzards_pos[r]:
            next = Node(x, y-1, r)
            node.add_next(next, '<')
            this_round.append(next)

        if y < M-1 and (x, y+1) not in blizzards_pos[r]:
            next = Node(x, y+1, r)
            node.add_next(next, '>')
            this_round.append(next)

        if (x, y) not in blizzards_pos[r]:
            next = Node(x, y, r)
            node.add_next(next, 'w')
            this_round.append(next)

    last_round = this_round

# for n, d in start_node.nexts:
    # print(str(n), d)


# BFS
done = set()
to_do = list()
to_do.append(start_node)
start_node.path = ''



while len(to_do) > 0:
    node = to_do.pop(0)

    if node.path in done:
        continue

    for n, d in node.nexts:
        n.path = node.path + d
        to_do.append(n)

        if n.x == N-1 and n.y == M-1:
            print(n.path)

    done.add(node)



