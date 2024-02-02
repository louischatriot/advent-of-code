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


# PART 2
matrix = [[c for c in l] for l in lines]
I, J = len(matrix), len(matrix[0])
PART_TWO = True

if PART_TWO:
    matrix[0][0] = '#'
    matrix[0][-1] = '#'
    matrix[-1][0] = '#'
    matrix[-1][-1] = '#'

R = 100
for _ in range(R):
    new_matrix = [['.' for _ in range(J)] for _ in range(I)]

    for i, j in itertools.product(range(I), range(J)):
        on_neighbours = sum(1 if c == '#' else 0 for _, _, c in u.neighbours_not_center_iterator(matrix, i, j))
        if matrix[i][j] == '#' and on_neighbours in [2, 3]:
            new_matrix[i][j] = '#'
        if matrix[i][j] == '.' and on_neighbours == 3:
            new_matrix[i][j] = '#'

    matrix = new_matrix

    if PART_TWO:
        matrix[0][0] = '#'
        matrix[0][-1] = '#'
        matrix[-1][0] = '#'
        matrix[-1][-1] = '#'

res = sum(1 if matrix[i][j] == '#' else 0 for i, j in itertools.product(range(I), range(J)))
print(res)




