import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import collections
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
locks, keys = list(), list()
HEIGHT = None

matrix = list()
for line in lines:
    if line == '':
        if all(c == '#' for c in matrix[0]):
            heights = [[matrix[i][j] for i in range(len(matrix))].index('.') - 1 for j in range(len(matrix[0]))]
            locks.append(heights)
        else:
            heights = [len(matrix) - [matrix[i][j] for i in range(len(matrix))].index('#') - 1 for j in range(len(matrix[0]))]
            keys.append(heights)

        if HEIGHT is None:
            HEIGHT = len(matrix)

        matrix = list()

    else:
        matrix.append(line)


res = 0
for lock, key in itertools.product(locks, keys):
    if all(a + b < HEIGHT-1 for a, b in zip(lock, key)):
        res += 1

print(res)


