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
dirs = { 'W': (0, -1), 'E': (0, 1), 'N': (-1, 0), 'S': (1, 0) }

# Not very efficient, the same part of the regex get parsed over and over
# Fast enough for this but a better approach would be to compile first then use
def walk(edges, starting_pos, regex):
    # Terminal case, no recursion
    if '(' not in regex:
        next_starting_pos = set()

        for pos in starting_pos:
            for part in regex.split('|'):
                current = pos

                for c in part:
                    dx, dy = dirs[c]
                    next_current = (current[0] + dx, current[1] + dy)
                    edges[current].add(next_current)
                    edges[next_current].add(current)
                    current = next_current

                next_starting_pos.add(current)

        return next_starting_pos

    # Break in top level OR (separated by |)
    # If multiple parts separated by OR, treat each separately and recusively
    parts = list()
    part = ''
    idx = 0
    depth = 0
    while idx < len(regex):
        c = regex[idx]

        if c == '(':
            depth += 1
            part += c

        elif c == ')':
            depth -= 1
            part += c

        elif c == '|' and depth == 0:
            if len(part) > 0:
                parts.append(part)
                part = ''

        else:
            part += c

        idx += 1

    if len(part) > 0:
        parts.append(part)

    if len(parts) > 1:
        res = set()
        for part in parts:
            next_starting_pos = walk(edges, starting_pos, part)
            res = res.union(next_starting_pos)

        return res

    # Break in top level AND parts from parentheses
    parts = list()
    part = ''
    idx = 0
    while idx < len(regex):
        c = regex[idx]

        if c == '(':
            if len(part) > 0:
                parts.append(part)
                part = ''

            depth = 1
            while True:
                idx += 1
                c = regex[idx]
                if c == '(':
                    depth += 1
                elif c == ')':
                    depth -= 1
                    if depth == 0:
                        break
                part += c

            if len(part) > 0:
                parts.append(part)
                part = ''

        else:
            part += c

        idx += 1

    if len(part) > 0:
        parts.append(part)

    # Follow the parts, updating the set of starting positions
    for part in parts:
        starting_pos = walk(edges, starting_pos, part)

    return starting_pos


# Build graph
edges = defaultdict(lambda: set())
walk(edges, { (0, 0) }, lines[0][1:-1])



# Explore it
to_explore = deque()
to_explore.append((0, (0, 0)))
visited = set()
far_rooms = set()
res = 0

while to_explore:
    d, node = to_explore.popleft()
    if node in visited:
        continue
    else:
        visited.add(node)

    res = d
    if d >= 1000:
        far_rooms.add(node)

    for n in edges[node]:
        if n not in visited:
            to_explore.append((d+1, n))


print(res)


# PART 2
print(len(far_rooms))





