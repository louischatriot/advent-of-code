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
def tile_n(t):
    res = 0
    for i, e in enumerate(t):
        if e == '#':
            res += 2**i
    return res

def tile_nr(t):
    res = 0
    for i, e in enumerate(reversed(t)):
        if e == '#':
            res += 2**i
    return res

tiles = dict()
tile_number = None
h1, h2, v1, v2 = None, None, None, None
for i, l in enumerate(lines):
    if l == '':
        pass
        continue

    if l[0:4] == 'Tile':
        tile_number = int(l[5:-1])
        h1 = lines[i+1]
        h2 = lines[i+10]
        v1, v2 = '', ''
        for j in range(1, 11):
            v1 += lines[i+j][0]
            v2 += lines[i+j][-1]

        normal = [tile_n(h1), tile_n(v1), tile_n(h2), tile_n(v2)]
        flipH = [tile_nr(h1), tile_n(v2), tile_nr(h2), tile_n(v1)]
        flipV = [tile_n(h2), tile_nr(v1), tile_n(h1), tile_nr(v2)]

        # TODO check all different

        tiles[tile_number] = []
        for o in [normal, flipH, flipV]:
            for i in range(0, 4):
                tiles[tile_number].append(o[i:]+o[0:i])


for tile, orientation in tiles.items():
    pass






