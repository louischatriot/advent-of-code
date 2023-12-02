import sys
import re
import u as u
from collections import defaultdict
import math
import itertools

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
rotations = []
matrices = []
for a in range(0, 3):
    for b in range(0, 3):
        if b == a:
            continue

        for c in range(0, 3):
            if c == a or c == b:
                continue

            for sa in [-1, 1]:
                for sb in [-1, 1]:
                    for sc in [-1, 1]:
                        m = [[0, 0, 0] for _ in range(0, 3)]

                        m[0][a] = sa
                        m[1][b] = sb
                        m[2][c] = sc

                        det = m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[2][0] * m[1][2]) + m[0][2] * (m[1][0] * m[2][1] - m[2][0] * m[1][1])
                        if det == 1:
                            matrices.append(m)

print("Generated rotation matrices:", len(matrices))

def rotate(m, p):
    va, vb, vc = p
    return tuple(m[i][0] * va + m[i][1] * vb + m[i][2] * vc for i in range(0, 3))


scanners = []
current_scanner = []
for l in lines[1:]:
    if l == '':
        continue
    elif l[0:3] == '---':
        scanners.append(current_scanner)
        current_scanner = []
    else:
        current_scanner.append(tuple(map(int, l.split(','))))

scanners.append(current_scanner)
print("Parsed scanners:", len(scanners))


def signature(points):
    ref = points[0]
    l = [str(p[0] - ref[0]) + ',' + str(p[1] - ref[1]) + ',' + str(p[2] - ref[2]) for p in points]
    l.sort()
    return ';;'.join(l)


def d(p1, p2):
    va, vb, vc = p1
    wa, wb, wc = p2
    return (va - wa) ** 2 + (vb - wb) ** 2 + (vc - wc) ** 2

def eql(p1, p2):
    va, vb, vc = p1
    wa, wb, wc = p2
    return (va == wa) and (vb == wb) and (vc == wc)

def minus(p1, p2):
    va, vb, vc = p1
    wa, wb, wc = p2
    return ((va - wa), (vb - wb), (vc - wc))


def scanner_pair(scanner1, scanner2):
    dist0 = []
    for p1, p2 in itertools.combinations(scanner1, 2):
        if p1 != p2:
            dist0.append((d(p1, p2), p1, p2))

    dist0.sort()

    dist1 = []
    for p1, p2 in itertools.combinations(scanner2, 2):
        if p1 != p2:
            dist1.append((d(p1, p2), p1, p2))

    dist1.sort()

    matches = []
    i, j = 0, 0
    while i < len(dist0) and j < len(dist1):
        if dist0[i][0] == dist1[j][0]:
            matches.append((dist0[i][0], dist0[i][1:], dist1[j][1:]))
            i += 1
            j += 1

        elif dist0[i][0] < dist1[j][0]:
            i += 1

        else:
            j += 1

    # 66 means 12 points
    rotation, delta = None, None
    if len(matches) >= 66:
        # First pair with unique distance
        for i in range(0, len(matches)-1):
            if matches[i+1][0] > matches[i][0]:
                break

        p1a, p1b = matches[i][1]
        p2a, p2b = matches[i][2]

        for m in matrices:
            q2a = rotate(m, p2a)
            q2b = rotate(m, p2b)

            if eql(minus(p1a, p1b), minus(q2a, q2b)) or eql(minus(p1a, p1b), minus(q2b, q2a)):
                if rotation is None:
                    rotation = m

                    if eql(minus(p1a, q2a), minus(p1b, q2b)):
                        delta = minus(p1a, q2a)
                    else:
                        delta = minus(p1a, q2b)

                else:
                    raise ValueError("Found two possible rotations")

    # Maybe check that the found rotation works for all points, but trusting input quality here :)

    return rotation, delta


nodes = set()
edges = defaultdict(lambda: dict())


for i, s in enumerate(scanners):
    nodes.add(i)

    for j, t in enumerate(scanners):
        if s == t:
            continue

        rot, delta = scanner_pair(s, t)

        if rot == None:
            continue

        edges[i][j] = (rot, delta)


start_node = 0
paths = { start_node: [] }
nodes_to_do = { start_node }

while len(nodes_to_do) > 0:
    node = nodes_to_do.pop()
    base_path = paths[node]

    for next_node, edge in edges[node].items():

        if next_node not in paths:
            paths[next_node] = base_path + [edge]
            nodes_to_do.add(next_node)



for k, v in paths.items():
    print(k, v)





