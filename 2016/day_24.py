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
    lines = [line.rstrip() for line in file]


# PART 1
if is_example:
    for l in lines:
        print(l)

g = u.Graph()
g.create_from_matrix(lines)
g.print()
res, _ = g.get_shortest_path_covering_all_nodes('0')
print(res)


# PART 2
g = u.Graph()
g.create_from_matrix(lines, full=True)
g.print()
res = g.tsp('0', True)
print(res)



