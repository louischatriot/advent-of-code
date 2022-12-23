from time import time

with open("inputs/day_23.data") as file:
    lines = [line.rstrip() for line in file]

elves = []
for x, l in enumerate(lines):
    for y, c in enumerate(l):
        if c == '#':
            elves.append(['N', x, y])


# xmin, xmax, ymin, ymax
def get_box(elves):
    xs = [x for _, x, _ in elves]
    ys = [y for _, _, y in elves]
    return min(xs), max(xs), min(ys), max(ys)

def print_elves(elves):
    xmin, xmax, ymin, ymax = get_box(elves)
    grid = [['.' for _ in range(ymin, ymax+1)] for _ in range(xmin, xmax+1)]

    for n, e in enumerate(elves):
        dir, x, y = e
        # grid[x-xmin][y-ymin] = dir   # Read more carefully!
        grid[x-xmin][y-ymin] = chr(97 + n)

    print('\n'.join([' '.join([c for c in l]) for l in grid]))
    print("==========================================")
    print("==========================================")


dirs = ['N', 'S', 'W', 'E']
moves = {
    'N': {'test': [(-1, -1), (-1, 0), (-1, 1)], 'dir': (-1, 0)},
    'S': {'test': [(1, -1), (1, 0), (1, 1)], 'dir': (1, 0)},
    'W': {'test': [(-1, -1), (0, -1), (1, -1)], 'dir': (0, -1)},
    'E': {'test': [(-1, 1), (0, 1), (1, 1)], 'dir': (0, 1)}
}

adjacents = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]



# Part 1 and 2
dir0_main = 'N'

for r in range(0, 10000):
    positions = set((x, y) for _, x, y in elves)
    proposals = {}

    for n, e in enumerate(elves):
        proposal = None
        dir0, x0, y0 = e

        # No proposal if the elf has no neighbours
        if all([(x0 + dx, y0 + dy) not in positions for dx, dy in adjacents]):
            continue

        dir0 = dir0_main   # Overriding because I did not read the text correctly oO - I thought every elf would remember their last direction
        d0 = dirs.index(dir0)

        for d in range(0, len(dirs)):
            dir_test = dirs[(d0 + d) % len(dirs)]

            if all((x0 + x, y0 + y) not in positions for x, y in moves[dir_test]['test']):
                proposal = (x0 + moves[dir_test]['dir'][0], y0 + moves[dir_test]['dir'][1], e, dir_test)
                break

        if proposal:
            x, y, e, d = proposal
            if (x, y) not in proposals:
                proposals[(x, y)] = []
            proposals[(x, y)].append((e, d))

    for p, es in proposals.items():
        if len(es) == 1:
            x, y = p
            e, d = es[0]
            e[0] = d
            e[1] = x
            e[2] = y

    # Comment this out and run the right number of rounds for part 1
    if len(proposals) == 0:
        print(r+1)
        1/0

    dir0_main = dirs[(dirs.index(dir0_main) + 1) % len(dirs)]

xmin, xmax, ymin, ymax = get_box(elves)
res = (xmax - xmin + 1) * (ymax - ymin + 1) - len(elves)
print(res)







