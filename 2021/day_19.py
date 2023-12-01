import sys
import re
import u as u
from collections import defaultdict
import math

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

def rotate(m, va, vb, vc):
    return tuple(m[i][0] * va + m[i][1] * vb + m[i][2] * vc for i in range(0, 3))

# for m in matrices:
    # print(rotate(m, 8, 0, 7))











