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
res = 0
word = 'XMAS'
N, M = len(lines), len(lines[0])

# Horizontal
for line in lines:
    rev = ''.join([c for c in reversed(line)])
    res += line.count(word)
    res += rev.count(word)

# Vertical
for c in range(M):
    col = ''.join([lines[i][c] for i in range(N)])
    rev = ''.join([c for c in reversed(col)])
    res += col.count(word)
    res += rev.count(word)

# Diagonals
for d in u.diagonals(lines):
    diag = ''.join(d)
    rev = ''.join([c for c in reversed(diag)])
    res += diag.count(word)
    res += rev.count(word)

print(res)


# PART 2
res = 0
for i, j in itertools.product(range(1, N-1), range(1, M-1)):
    if lines[i][j] != 'A':
        continue

    # Boy isn't that clean
    if lines[i-1][j-1] == 'M' and lines [i+1][j-1] == 'M' and lines[i-1][j+1] == 'S' and lines[i+1][j+1] == 'S':
        res += 1
    elif lines[i-1][j-1] == 'S' and lines [i+1][j-1] == 'M' and lines[i-1][j+1] == 'S' and lines[i+1][j+1] == 'M':
        res += 1
    elif lines[i-1][j-1] == 'S' and lines [i+1][j-1] == 'S' and lines[i-1][j+1] == 'M' and lines[i+1][j+1] == 'M':
        res += 1
    elif lines[i-1][j-1] == 'M' and lines [i+1][j-1] == 'S' and lines[i-1][j+1] == 'M' and lines[i+1][j+1] == 'S':
        res += 1

print(res)



















