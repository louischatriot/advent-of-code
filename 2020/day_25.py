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
card_public = int(lines[0])
door_public = int(lines[1])

sn = 7
m = 20201227

def find_loop(pk, sn, m):
    v = 1
    l = 0
    while True:
        l += 1
        v = (v * sn) % m
        if v == pk:
            return l

def calc_sk(sn, m, l):
    res = 1
    for _ in range(0, l):
        res = (res * sn) % m
    return res

cl = find_loop(card_public, sn, m)
print(cl)

dl = find_loop(door_public, sn, m)
print(dl)

sk = calc_sk(card_public, m, dl)
print(sk)




