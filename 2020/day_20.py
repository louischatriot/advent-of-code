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


# PART 1 & 2
def print_tile(tile):
    for l in tile:
        print(''.join(l))
    print('')

tiles = dict()

for i, l in enumerate(lines):
    if l == '':
        continue

    if l[0:4] == 'Tile':
        tile_number = int(l[5:-1])
        tiles[tile_number] = []

        for j in range(1, 11):
            tiles[tile_number].append(lines[i+j])

N = int(len(tiles) ** .5)

def flipV(tile):
    res = []
    for l in reversed(tile):
        res.append(l)
    return res

def flipH(tile):
    res = []
    for l in tile:
        res.append([c for c in reversed(l)])
    return res

def noflip(tile):
    return tile

def rotate(tile):
    res = [['X' for _ in range(0, len(tile[0]))] for _ in range(0, len(tile))]

    for i, l in enumerate(tile):
        for j, c in enumerate(l):
            res[len(tile) - 1 - j][i] = c

    return res

def left(tile):
    res = ''
    for i, l in enumerate(tile):
        res += l[0]
    return res

def right(tile):
    res = ''
    for i, l in enumerate(tile):
        res += l[-1]
    return res

def top(tile):
    return ''.join(tile[0])

def bottom(tile):
    return ''.join(tile[-1])

borders = [top, left, bottom, right]
flips = [noflip, flipV, flipH]


done_tiles = set()

# Find top left
for tn, tile in tiles.items():
    open_borders = 0

    for border_fn in [top, left]:  # If I luck out some time has no top and left border as it stands otherwise I search again after flipping and rotating
        border = border_fn(tile)
        found_border = False

        for tn2, tile2 in tiles.items():
            if tn2 == tn:
                continue

            if ( any(border == border_fn2(tile2) for border_fn2 in borders) or
                 any(border == border_fn2(flipV(tile2)) for border_fn2 in borders) or
                 any(border == border_fn2(flipH(tile2)) for border_fn2 in borders)
            ):
                found_border = True
                break

        if found_border:
            open_borders += 1

    if open_borders == 0:
        top_left = tn
        break

# Utility functions
def get_oriented_tile(tile_n, tile_flip, tile_rotate):
    tile0_n, tile0_flip, tile0_rotate = line[-1]

    tile = tiles[tile_n]
    tile = tile_flip(tile)
    for _ in range(0, tile_rotate):
        tile = rotate(tile)

    return tile

def find_tile(tile0, border0, border):
    tile0_border = border0(tile0)

    found = None
    for tn, tile in tiles.items():
        if tn == tile0_n or tn in done_tiles:
            continue

        for flip in flips:
            the_tile = flip(tile)

            for r in range(0, 4):
                if not found:
                    if border(the_tile) == tile0_border:
                        found = (tn, flip, r)
                    else:
                        the_tile = rotate(the_tile)

    if not found:
        print("PROBLEM")
    else:
        return found


matrix = []

# Top line
line = [(top_left, noflip, 0)]
done_tiles.add(top_left)

for _ in range(1, N):
    tile0_n, tile0_flip, tile0_rotate = line[-1]
    tile0 = get_oriented_tile(tile0_n, tile0_flip, tile0_rotate)

    found = find_tile(tile0, right, left)
    line.append(found)

matrix.append(line)


# Other lines
for _ in range(1, N):
    tile0_n, tile0_flip, tile0_rotate = matrix[-1][0]
    tile0 = get_oriented_tile(tile0_n, tile0_flip, tile0_rotate)
    found = find_tile(tile0, bottom, top)

    line = [found]
    for _ in range(1, N):
        tile0_n, tile0_flip, tile0_rotate = line[-1]
        tile0 = get_oriented_tile(tile0_n, tile0_flip, tile0_rotate)

        found = find_tile(tile0, right, left)
        line.append(found)

    matrix.append(line)


# PART 1 ANSWER
res = matrix[0][0][0] * matrix[-1][0][0] * matrix[0][-1][0] * matrix[-1][-1][0]
print(res)


full_matrix = []
for l in matrix:
    fl = []

    for f in l:
        tile_n, tile_flip, tile_rotate = f
        fl.append(get_oriented_tile(tile_n, tile_flip, tile_rotate))

    full_matrix.append(fl)

# Let's look at the full tile matrix!
for i in range(0, N):
    for j in range(0, 10):
        print('  '.join([''.join(tile[j]) for tile in full_matrix[i]]))
    print('')

picture = []
for l in full_matrix:
    for i in range(1, 9):
        pic_line = []

        for tile in l:
            pic_line += tile[i][1:9]

        picture.append(pic_line)

print("========================================")
for l in picture:
    print(l)


pattern = []
pattern.append("                  # ")
pattern.append("#    ##    ##    ###")
pattern.append(" #  #  #  #  #  #   ")


for flip in flips:
    the_pic = flip(picture)

    for _ in range(0, 4):
        one_found = False


        for i0 in range(0, len(the_pic) - len(pattern)):
            for j0 in range(0, len(the_pic[0]) - len(pattern[0])):

                found = True

                for i in range(0, len(pattern)):
                    for j in range(0, len(pattern[0])):
                        if pattern[i][j] == '#' and the_pic[i0 + i][j0 + j] != '#':
                            found = False

                if found:
                    one_found = True
                    for i in range(0, len(pattern)):
                        for j in range(0, len(pattern[0])):
                            if pattern[i][j] == '#':
                                the_pic[i0 + i][j0 + j] = 'O'


        if one_found:
            print("========================================")
            for l in the_pic:
                print(l)

            res = 0
            for l in the_pic:
                for c in l:
                    if c == '#':
                        res += 1
            print("========================================")
            print(res)

        the_pic = rotate(the_pic)





