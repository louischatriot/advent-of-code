from time import time

with open("inputs/day_22_example.data") as file:
    lines = [line.rstrip() for line in file]


class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbours = dict()

    def __str__(self):
        return f"<{self.type}> {self.x},{self.y}"

    def set_type(self, t):
        self.type = t

    def set_neighbour(self, direction, neighbour):
        self.neighbours[direction] = neighbour

    def get_neighbour(self, direction):
        return self.neighbours[direction]



path = None
start = None
matrix = []
max_y = -1

for x, l in enumerate(lines):
    if l == '':
        continue

    if l[0] not in [' ', '.', '#']:
        path = l
        continue

    line_start = None
    line_nodes = []

    full_line_nodes = []

    for y, c in enumerate(l):
        full_line_nodes.append(None)
        max_y = max(max_y, y)

        if c == ' ':
            continue

        if line_start is None:
            line_start = y + 1

        # Leave an empty line at the top of the input file :)
        n = Node(x, y+1)
        n.set_type('wall' if c == '#' else 'empty')
        line_nodes.append(n)
        full_line_nodes[-1] = n

    # Linking the line
    for i in range(0, len(line_nodes)):
        n1 = line_nodes[i-1]
        n2 = line_nodes[i]
        n1.set_neighbour('right', n2)
        n2.set_neighbour('left', n1)

    matrix.append(full_line_nodes)


for y in range(0, max_y+1):
    xs, xe = None, None

    for x in range(0, len(matrix)):
        elt = None if len(matrix[x]) <= y else matrix[x][y]

        if elt is not None:
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




# n = matrix[6][2]
# print(n)
# n = n.get_neighbour('bottom')
# print(n)

# n = n.get_neighbour('bottom')
# print(n)

# n = n.get_neighbour('bottom')
# print(n)

# n = n.get_neighbour('right')
# n = n.get_neighbour('right')
# n = n.get_neighbour('right')
# n = n.get_neighbour('right')
# n = n.get_neighbour('right')
# n = n.get_neighbour('right')
# print(n)

# n = n.get_neighbour('top')
# print(n)

# n = n.get_neighbour('top')
# n = n.get_neighbour('top')
# print(n)

# n = n.get_neighbour('top')
# n = n.get_neighbour('top')
# print(n)

# n = n.get_neighbour('top')
# print(n)

# n = n.get_neighbour('left')
# print(n)

# n = n.get_neighbour('bottom')
# print(n)






