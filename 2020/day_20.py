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

# for tn, tile in tiles.items():
    # print(tn)
    # print_tile(tile)

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

tile = tiles[1171]

# print(top(tile))
# print(bottom(tile))
# print(right(tile))
# print(left(tile))
# print("==========================")

# print_tile(tile)
# print_tile(flipV(tile))
# print_tile(flipH(tile))



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

for l in matrix:
    print(l)

full_matrix = []
for l in matrix:
    fl = []

    for f in l:
        tile_n, tile_flip, tile_rotate = f
        fl.append(get_oriented_tile(tile_n, tile_flip, tile_rotate))

    full_matrix.append(fl)


for i in range(0, N):
    for j in range(0, 10):
        print('  '.join([''.join(tile[j]) for tile in full_matrix[i]]))
    print('')








sys.exit(0)

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

tile_contents = dict()
tiles = dict()
tile_number = None
h1, h2, v1, v2 = None, None, None, None
for i, l in enumerate(lines):
    if l == '':
        continue

    if l[0:4] == 'Tile':
        tile_number = int(l[5:-1])
        h1 = lines[i+1]
        h2 = lines[i+10]
        v1, v2 = '', ''
        tile_contents[tile_number] = []

        for j in range(1, 11):
            v1 += lines[i+j][0]
            v2 += lines[i+j][-1]
            tile_contents[tile_number].append(lines[i+j])

        # normal = [tile_n(h1), tile_n(v1), tile_n(h2), tile_n(v2)]
        # flipH = [tile_nr(h1), tile_n(v2), tile_nr(h2), tile_n(v1)]
        # flipV = [tile_n(h2), tile_nr(v1), tile_n(h1), tile_nr(v2)]


        normal = [tile_nr(h1), tile_n(v1), tile_n(h2), tile_nr(v2)]
        flipH = [tile_n(h1), tile_n(v2), tile_nr(h2), tile_nr(v1)]
        flipV = [tile_nr(h2), tile_nr(v1), tile_n(h1), tile_n(v2)]

        # TODO check all different?

        tiles[tile_number] = [normal, flipH, flipV]


for l in tile_contents[1951]:
    print(l)

print('')
print('')

for l in tile_contents[1951]:
    print(''.join([c for c in reversed(l)]))

print('')
print('')

for l in reversed(tile_contents[1951]):
    print(l)

print('')
print('')


print(tiles[1951])


1/0



all_links = dict()

for tn, flips in tiles.items():
    all_links[tn] = [[], [], []]

    for f, flip in enumerate(flips):
        these_links = dict()

        for tn2, flips2 in tiles.items():
            if tn2 == tn:
                continue

            tile_links = []

            for f2, flip2 in enumerate(flips2):
                if any(i == j for i in flip for j in flip2):
                    tile_links.append(f2)

            if len(tile_links) > 0:
                these_links[tn2] = tile_links

        all_links[tn][f] = these_links



# Check whatever the flip each piece is always linked to the same piece (i.e. this problem is simpler than general case)
for tn, links in all_links.items():
    if any('-'.join(map(str, sorted(list(links[0].keys())))) != '-'.join(map(str, sorted(list(l.keys())))) and idx > 0 for l in links):
        print("PROBLEM")
        1/0

res = 1
corners = []
for tn, links in all_links.items():
    if any(len(l) == 2 for l in links):
        res *= tn
        corners.append(tn)

print(res)


# PART 2
edges = []
for tn, links in all_links.items():
    if all(len(l) == 3 for l in links):
        edges.append(tn)

N = int(len(tiles) ** .5)
matrix = []
placed_tiles = set()


for _ in range(0, 3):
    line = []

    # Line beginning (top left or just left)
    if len(matrix) == 0:
        # Find top left corner
        top_left = None
        for corner in corners:
            if top_left is not None:
                break

            normal, flipH, flipV = tiles[corner]
            # Look only at normal placement for top left corner, the others are useless symetries for now

            can_be = True
            for tn, fns in all_links[corner][0].items():
                for fn in fns:
                    tile_flip = tiles[tn][fn]
                    if any(b == normal[0] or b == normal[1] for b in tile_flip):
                        can_be = False

            if can_be:
                top_left = corner

        line = [(top_left, 0, 0)]
        placed_tiles.add(top_left)

    else:
        # Find left-most of next line
        tl_tn, tl_fn, tl_r = matrix[-1][0]
        bottom_border = tiles[tl_tn][tl_fn][(2 + tl_r) % 4]

        found = False
        for tn, fns in all_links[tl_tn][tl_fn].items():
            if tn in placed_tiles:
                continue

            for fn in fns:
                tile_borders = tiles[tn][fn]
                if any(b == bottom_border for b in tile_borders):
                    if found:
                        pass
                        # print("CONFLICT", tn, fn)
                    else:
                        i = tile_borders.index(bottom_border)
                        line = [(tn,fn, i)]
                        placed_tiles.add(tn)
                        found = True

        placed_tiles.add(line[0])

    # Rest of line
    for _ in range(1, N):
        left_tn, left_fn, left_rotation = line[-1]
        left_tile_borders = tiles[left_tn][left_fn]
        right_border = left_tile_borders[(3 + left_rotation) % 4]

        links = all_links[left_tn][left_fn]

        found = False
        for tn, fns in links.items():
            if tn in placed_tiles:
                continue

            for fn in fns:
                tile_borders = tiles[tn][fn]
                if any(b == right_border for b in tile_borders):
                    if found:
                        pass
                        # print("CONFLICT", tn, fn)
                    else:


                        i = tile_borders.index(right_border)

                        print("TILE", tn, fn, i, right_border)

                        line.append((tn, fn, (i-1) % 4))
                        placed_tiles.add(tn)
                        found = True

        if not found:
            print("PROBLEM NOT FOUND AT LINE", line)

    matrix.append(line)


print(tiles[1171])


for l in matrix:
    print(l)


picture = [['XXX' for _ in range(0,N*10)] for _ in range(0,N*10)]

for I, matrix_line in enumerate(matrix):
    for J, __v in enumerate(matrix_line):
        tn, fn, rn = __v

        for i, l in enumerate(tile_contents[tn]):
            for j, c in enumerate(l):
                # Flip
                if fn == 0:
                    it, jt = i, j
                if fn == 1:
                    it, jt = i, 9 - j
                if fn == 2:
                    it, jt = 9 - i, j

                # Rotate
                if rn == 1:
                    it, jt = jt, 9 - it
                if rn == 2:
                    it, jt = 9 - it, 9 - jt
                if rn == 3:
                    it, jt = jt, it

                picture[10 * I + it][10 * J + jt] = c


for idx, l in enumerate(picture):
    if idx % 10 == 0:
        print('')
    print(''.join(l[0:10]) + '  ' + ''.join(l[10:20]) + '  ' + ''.join(l[20:30]))


