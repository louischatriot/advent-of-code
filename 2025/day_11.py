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
nodes = set()
edges = defaultdict(lambda: list())

for line in lines:
    origin, dests = line.split(': ')
    dests = dests.split(' ')

    nodes.add(origin)
    for dest in dests:
        nodes.add(dest)
        edges[origin].append(dest)

# Pure recursive search, no memoization, no loop detection
def count_paths_to(final_dest, edges, current):
    if current == final_dest:
        return 1

    if len(edges[current]) == 0:
        return 0

    return sum(count_paths_to(final_dest, edges, dest) for dest in edges[current])

res = count_paths_to('out', edges, 'you')
print(res)


# PART 2
# Too long to list the paths
# def list_all_paths_to(final_dest, edges, current):
    # if current == final_dest:
        # yield [current]

    # if len(edges[current]) == 0:
        # return

    # for dest in edges[current]:
        # for path in list_all_paths_to(final_dest, edges, dest):
            # yield [current] + path

# res = 0
# for path in list_all_paths_to('out', edges, 'svr'):
    # if 'fft' in path and 'dac' in path:
        # res += 1

# print(res)

mem = dict()
def count_good_paths_to(final_dest, current, okfft, okdac):
    key = f"{current}---{okfft}---{okdac}"
    if key in mem:
        return mem[key]

    if current == final_dest:
        if okfft and okdac:
            return 1
        else:
            return 0

    if len(edges[current]) == 0:
        return 0

    res = 0
    for dest in edges[current]:
        if current == 'fft':
            okfft = True

        if current == 'dac':
            okdac = True

        res += count_good_paths_to(final_dest, dest, okfft, okdac)

    mem[key] = res
    return res

res = count_good_paths_to('out', 'svr', False, False)
print(res)





