import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
patterns = list()

i = 1
while True:
    if len(lines[i].split(': ')) == 2:
        break

    pattern = [[c for c in line] for line in lines[i:i+3]]
    patterns.append(pattern)
    i += 5

i -= 1
goals = list()
for line in lines[i:]:
    size, pats = line.split(': ')
    size = size.split('x')
    size = list(map(int, size))
    pats = pats.split(' ')
    pats = list(map(int, pats))

    goals.append((size, pats))


pat_size = [sum(sum(1 if c == '#' else 0 for c in line) for line in pattern) for pattern in patterns]

def rot(pattern):
    res = [[None for _ in range(3)] for _ in range(3)]

    for i,j in itertools.product(range(3), repeat=2):
        res[j][2-i] = pattern[i][j]

    return res


p = patterns[0]

for l in p:
    print(l)

for _ in range(5):
    print("=============================")
    print("=============================")
    p = rot(p)
    for l in p:
        print(l)

print(f"Initially: {len(goals)}")

# Not enough cells, no way that can fit
new_goals = list()
for size, pats in goals:
    s = u.sumproduct(pats, pat_size)
    if s > size[0] * size[1]:
        continue
    else:
        new_goals.append((size, pats))

goals = new_goals
print(f"After trivial too small: {len(goals)}")

# No need to play Tetris
new_goals = list()
for size, pats in goals:
    if size[0] * size[1] >= 9 * sum(pats):
        new_goals.append((size, pats))

goals = new_goals
print(f"After trivial big enough: {len(goals)}")

# LOLWUT actually I did not need to do what I'm doing below WAAAAT

# Apply 3+0+2 pattern
new_goals = list()
for size, pats in goals:
    n = min(pats[3], pats[0], pats[2])
    X, Y = size

    # Maxed out lines
    pat_per_full_line = Y // 6
    full_lines = n // pat_per_full_line
    rem_squares = ((Y - 6 * pat_per_full_line) // 3) * full_lines
    X -= 3 * (full_lines)

    # Last line
    rem_pats = n - full_lines * pat_per_full_line
    if rem_pats > 0:
        rem_squares += (Y - 6 * rem_pats) // 3
        X -= 3

    rem_squares += (X // 3) * (Y // 3)
    to_place = sum(pats) - 3 * n

    if rem_squares >= to_place:
        new_goals.append(goals)

goals = new_goals
print(f"After some Tetris: {len(goals)}")





"""
0:
.##
##.
#..

1:
.##
##.
###

2:
#..
##.
###

3:
##.
##.
###

4:
#.#
###
#.#

5:
###
..#
###
"""

"""
3 + 0 + 2:         3x6
###  .##  ..#    | ######
##.  ##.  .##    | ######
##.  #..  ###    | ######

5 + 5:        4x4
     ###    | .###
###  ..#    | ####
#..  ###    | ####
###         | ###.



  #.#
  ###
  .##

###..###
########
########
.######.



"""










