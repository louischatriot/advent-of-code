import sys
import re
import u as u
from collections import defaultdict, deque
import math
import itertools
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line[0:-1] for line in file]


# PART 1
map = [[c for c in line] for line in lines]
N, M = len(map), len(map[0])

goblins = list()
elves = list()

ELF_DMG = 3   # PART 1
ELF_DMG = 15  # PART 2

for y, x in itertools.product(range(N), range(M)):
    if map[y][x] == 'G':
        goblins.append([y, x, 200, 3, "goblin"])
    elif map[y][x] == 'E':
        elves.append([y, x, 200, ELF_DMG, "elf"])

beginning_elves = len(elves)


# Ortho neighbours in reading order
ortho = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def dist(u1, u2):
    y1, x1, hp1, dmg1, t1 = u1
    y2, x2, hp2, dmg2, t2 = u2
    return abs(y1-y2) + abs(x1-x2)


def attack(elves, goblins, unit):
    possible_targets = goblins if unit[4] == 'elf' else elves
    possible_targets = [u for u in possible_targets if u[2] > 0]
    in_range = [u for u in possible_targets if dist(u, unit) == 1]

    if len(in_range) == 0:
        return elves, goblins

    fewest_hp = min(u[2] for u in in_range)
    weakest = [u for u in in_range if u[2] == fewest_hp]
    target = sorted(weakest)[0]
    target[2] = max(0, target[2] - unit[3])

    for u in itertools.chain(elves, goblins):
        if u[2] == 0:
            map[u[0]][u[1]] = '.'

    elves = [u for u in elves if u[2] > 0]
    goblins = [u for u in goblins if u[2] > 0]

    return elves, goblins


full_turns = 0
finished = False

while True:
    attack_order = sorted(elves + goblins)
    for unit in attack_order:
        # Dead units can't do anything
        if unit[2] == 0:
            continue

        possible_targets = goblins if unit[4] == 'elf' else elves
        possible_targets = [u for u in possible_targets if u[2] > 0]

        # No one left to attack
        if len(possible_targets) == 0:
            finished = True
            break

        # Are there units already in range? If yes attack right away
        in_range = [u for u in possible_targets if dist(u, unit) == 1]
        if len(in_range) >= 1:
            elves, goblins = attack(elves, goblins, unit)
            continue

        # Move - find open squares first
        open_squares = set((y+dy, x+dx) for y, x, _, _, _ in possible_targets for dy, dx in ortho if map[y+dy][x+dx] == '.')

        # No open square in range of targets
        if len(open_squares) == 0:
            continue

        # Get shortest paths to all reachable open squares
        y, x, _, _, _ = unit
        to_explore = deque()
        to_explore.append((y, x, 0, None, None))
        visited = set()
        ends = list()
        while to_explore:
            y, x, d, fdy, fdx = to_explore.popleft()

            if (y, x) in visited:
                continue
            else:
                visited.add((y, x))

            if (y, x) in open_squares:
                ends.append((y, x, d, fdy, fdx))
                if len(ends) == len(open_squares):
                    break

            for dy, dx in ortho:
                ny, nx = y+dy, x+dx
                if map[ny][nx] == '.' or (ny, nx) in open_squares:
                    nfdy = fdy if fdy is not None else dy
                    nfdx = fdx if fdx is not None else dx

                    to_explore.append((ny, nx, d+1, nfdy, nfdx))

        # None of the open squares are reachable
        if len(ends) == 0:
            continue

        best_distance = min(v[2] for v in ends)
        ends = [v for v in ends if v[2] == best_distance]
        target = sorted(ends)[0]

        # Now we have the target, first in reading order in those reachable in the fewest steps, and its first step is also first in reading order
        y, x, _, _, _ = unit
        _, _, _, dy, dx = target
        ny, nx = y+dy, x+dx

        # Update unit and map
        unit[0] = ny
        unit[1] = nx
        map[y][x] = '.'
        map[ny][nx] = unit[4][0].upper()

        # Try to attack
        elves, goblins = attack(elves, goblins, unit)

    if finished:
        break

    full_turns += 1


score_elves = sum(u[2] for u in elves)
score_goblins = sum(u[2] for u in goblins)

print("FULL TURNS", full_turns)
print("ELVES", score_elves, '---', len(elves), 'out of', beginning_elves)
print("GOBLINS", score_goblins)


# PART 2
# Did the dichotomy by hand, lazy to code it
# Smallest elf attack is 15, to win with not even one loss



