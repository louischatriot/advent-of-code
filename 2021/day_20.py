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
algo = lines[0]

pixels = set()
for i, l in enumerate(lines[2:]):
    for j, c in enumerate(l):
        if c == '#':
            pixels.add((i, j))


def print_pixels(pixels):
    im, iM, jm, jM = 999999999, -999999999, 9999999999, -999999999
    for i, j in pixels:
        im, iM, jm, jM = min(im, i), max(iM, i), min(jm, j), max(jM, j)

    for i in range(im, iM+1):
        l = ''
        for j in range(jm, jM+1):
            if (i, j) in pixels:
                l += '#'
            else:
                l += '.'

        print(l)


R = 50

im, iM, jm, jM = 999999999, -999999999, 9999999999, -999999999
for i, j in pixels:
    im, iM, jm, jM = min(im, i), max(iM, i), min(jm, j), max(jM, j)

im -= 2 * R
iM += 2 * R + 1
jm -= 2 * R
jM += 2 * R + 1

for r in range(0, R // 2):
    new_pixels = set()
    for i in range(im+r, iM-r):
        for j in range(jm+r, jM-r):
            b = ''
            for di, dj in u.all_neighbours_and_center:
                b += ('1' if (i+di, j+dj) in pixels else '0')

            b = int(b, 2)
            if algo[b] == '#':
                new_pixels.add((i, j))

    pixels = new_pixels

    new_pixels = set()
    for i in range(im+r+1, iM-r-1):
        for j in range(jm+r+1, jM-r-1):
            b = ''
            for di, dj in u.all_neighbours_and_center:
                b += ('1' if (i+di, j+dj) in pixels else '0')

            b = int(b, 2)
            if algo[b] == '#':
                new_pixels.add((i, j))

    pixels = new_pixels


print(len(pixels))




