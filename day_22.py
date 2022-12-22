from time import time

with open("inputs/day_22_example.data") as file:
    lines = [line.rstrip() for line in file]


class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbours = dict()
        self.neighdirs = dict()

    def __str__(self):
        return f"<{self.type}> {self.x + 1},{self.y + 1}"

    def set_type(self, t):
        self.type = t

    def set_neighbour(self, direction, neighbour):
        self.neighbours[direction] = neighbour

    def get_neighbour(self, direction):
        return self.neighbours[direction]

    def set_neighdir(self, direction, neighbour, new_direction = None):
        self.neighdirs[direction] = (neighbour, new_direction)

    def get_neighdir(self, direction):
        return self.neighdirs[direction]


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

dirs = dict()
dirs['L'] = { 'left': 'bottom', 'bottom': 'right', 'right': 'top', 'top': 'left' }
dirs['R'] = { 'left': 'top', 'top': 'right', 'right': 'bottom', 'bottom': 'left' }


# Part 1
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
print("===================================")
print("===================================")

# Answer for part 1 is ==> 1000 * 126 + 4 * 87 + 2


# Part 2

# Part 1
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

    # Linking the line, no wrap
    for i in range(1, len(line_nodes)):
        n1 = line_nodes[i-1]
        n2 = line_nodes[i]
        n1.set_neighdir('right', n2)
        n2.set_neighdir('left', n1)

for y in range(0, M):
    xs, xe = None, None

    for x in range(0, N):
        if matrix[x][y] is not None:
            xe = x
            if xs is None:
                xs = x

    # Linking the column, no wrap
    for x in range(xs+1, xe+1):
        n1 = matrix[x-1][y]
        n2 = matrix[x][y]
        n1.set_neighdir('bottom', n2)
        n2.set_neighdir('top', n1)


# Handle cube wrapping
opposites = {'top': 'bottom', 'bottom': 'top', 'right': 'left', 'left': 'right'}

def wrap(matrix, coords_1, coords_2, dir_12, dir_21):
    for c1, c2 in zip(coords_1, coords_2):
        n1 = matrix[c1[0]][c1[1]]
        n2 = matrix[c2[0]][c2[1]]

        n1.set_neighdir(dir_12, n2, opposites[dir_21])
        n2.set_neighdir(dir_21, n1, opposites[dir_12])

wrap(matrix, [(x, 8) for x in range(0, 4)], [(4, y) for y in range(4, 8)], 'left', 'top')
wrap(matrix, [(x, 8) for x in range(8, 12)], [(7, y) for y in range(4, 8)], 'left', 'bottom')
wrap(matrix, [(0, y) for y in range(8, 12)], [(4, y) for y in range(0, 4)], 'top', 'top')
wrap(matrix, [(11, y) for y in range(8, 12)], [(7, y) for y in range(3, -1, -1)], 'bottom', 'bottom')
wrap(matrix, [(11, y) for y in range(12, 16)], [(x, 0) for x in range(7, 3, -1)], 'bottom', 'left')
wrap(matrix, [(8, y) for y in range(12, 16)], [(x, 11) for x in range(7, 3, -1)], 'top', 'right')
wrap(matrix, [(x, 15) for x in range(8, 12)], [(x, 11) for x in range(3, -1, -1)], 'right', 'right')



trace = [[' ' for _ in range(0, M)] for _ in range(0, N)]
for x, line in enumerate(lines):
    for y, c in enumerate(line):
        trace[x][y] = c

marks = {'top': '^', 'bottom': 'v', 'left': '<', 'right': '>'}
def mark(trace, node, dir):
    print("===========================================================")
    print(node)
    print(dir)

    x, y = node.x, node.y
    trace[x][y] = marks[dir]

    print('\n'.join([''.join(l) for l in trace]))


current = start
dir = 'right'

for i in path:
    # mark(trace, current, dir)

    if i in ['L', 'R']:
        dir = dirs[i][dir]
        # mark(trace, current, dir)
    else:
        for _ in range(0, i):
            next, new_dir = current.get_neighdir(dir)
            if next.type == 'empty':
                current = next
                if new_dir:
                    dir = new_dir

            # mark(trace, current, dir)


# print("===============================")
# print("===============================")
# print("===============================")
# print('\n'.join([''.join(l) for l in trace]))


print(current)
print(dir)




