from time import time

with open("inputs/day_22.data") as file:
    lines = [line.rstrip() for line in file]


class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbours = dict()

    def __str__(self):
        return f"<{self.type}> {self.x + 1},{self.y + 1}"

    def set_type(self, t):
        self.type = t

    def set_neighbour(self, direction, neighbour):
        self.neighbours[direction] = neighbour

    def get_neighbour(self, direction):
        return self.neighbours[direction]


_path = lines[-1]
path = []
num = ''
for c in _path:
    if c in ['L', 'R']:
        path.append(int(num))
        path.append(c)
        num = ''
    else:
        num += c
path.append(int(num))

lines = lines[0:-2]


start = None
N = len(lines)
M = max([len(l) for l in lines])
matrix = [[None for _ in range(0, M)] for _ in range(0, N)]


for x, l in enumerate(lines):
    line_nodes = []

    for y, c in enumerate(l):
        if c == ' ':
            continue

        n = Node(x, y)
        n.set_type('wall' if c == '#' else 'empty')
        line_nodes.append(n)
        matrix[x][y] = n

        if start is None:
            start = n

    # Linking the line
    for i in range(0, len(line_nodes)):
        n1 = line_nodes[i-1]
        n2 = line_nodes[i]
        n1.set_neighbour('right', n2)
        n2.set_neighbour('left', n1)

for y in range(0, M):
    xs, xe = None, None

    for x in range(0, N):
        if matrix[x][y] is not None:
            xe = x
            if xs is None:
                xs = x

    # Linking the column
    for x in range(xs+1, xe+1):
        n1 = matrix[x-1][y]
        n2 = matrix[x][y]
        n1.set_neighbour('bottom', n2)
        n2.set_neighbour('top', n1)

    n1 = matrix[xe][y]
    n2 = matrix[xs][y]
    n1.set_neighbour('bottom', n2)
    n2.set_neighbour('top', n1)


dirs = dict()
dirs['L'] = { 'left': 'bottom', 'bottom': 'right', 'right': 'top', 'top': 'left' }
dirs['R'] = { 'left': 'top', 'top': 'right', 'right': 'bottom', 'bottom': 'left' }



# Part 1
current = start
dir = 'right'

for i in path:
    if i in ['L', 'R']:
        dir = dirs[i][dir]
    else:
        for _ in range(0, i):
            next = current.get_neighbour(dir)
            if next.type == 'empty':
                current = next

print(current)
print(dir)


# Answer for part 1 is ==> 1000 * 126 + 4 * 87 + 2


