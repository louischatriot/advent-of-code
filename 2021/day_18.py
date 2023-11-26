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


import json

# PART 1
def check_and_explode(n):
    s = []
    to_explode_idx = None
    end_of_to_explode_idx = None
    last_left_idx = None
    first_right_idx = None

    for idx, c in enumerate(n):
        if '0' <= c <= '9':
            if to_explode_idx is None:
                last_left_idx = idx
            else:
                if first_right_idx is None and end_of_to_explode_idx is not None:
                    first_right_idx = idx

        elif c == ']':
            s.pop()

            if len(s) == 4 and to_explode_idx is not None and end_of_to_explode_idx is None:
                end_of_to_explode_idx = idx

        elif c == '[':
            s.append(True)

            if len(s) == 5 and to_explode_idx is None:
                to_explode_idx = idx

    if to_explode_idx is None:
        return n

    left, right = n[to_explode_idx+1:end_of_to_explode_idx].split(',')
    left, right = int(left), int(right)

    if first_right_idx is not None:
        end_idx = first_right_idx
        while '0' <= n[end_idx] <= '9':
            end_idx += 1

        right = str(int(n[first_right_idx:end_idx]) + right)
        n = n[0:first_right_idx] + right + n[end_idx:]

    if to_explode_idx is not None:
        n = n[0:to_explode_idx] + '0' + n[end_of_to_explode_idx+1:]

    if last_left_idx is not None:
        beg_idx = last_left_idx
        while '0' <= n[beg_idx] <= '9':
            beg_idx -= 1

        left = str(int(n[beg_idx+1:last_left_idx+1]) + left)
        n = n[0:beg_idx+1] + left + n[last_left_idx+1:]

    return n


def check_and_split(n):
    big_idx = None
    end_idx = None

    for idx, c in enumerate(n):
        if '0' <= c <= '9':

            if big_idx is not None:
                if end_idx is None:  # ASSUMING WE NEVER GET NUMBERS LARGER THAN 100
                    end_idx = idx
            else:
                big_idx = idx

        else:
            if end_idx is None:
                big_idx = None

    if big_idx is None:
        return n

    num = int(n[big_idx:end_idx+1])
    n = n[0:big_idx] + '[' + str(num // 2) + ',' + str(num - num // 2) + ']' + n[end_idx+1:]

    return n


def make_valid(n):
    new_n = None
    while new_n is None:
        new_n = check_and_explode(n)
        if n != new_n:
            n = new_n
            new_n = None
            continue

        new_n = check_and_split(n)
        if n != new_n:
            n = new_n
            new_n = None
            continue

    return n


def add(n1, n2):
    n = '[' + n1 + ',' + n2 + ']'
    n = make_valid(n)
    return n


def magnitude(n):
    if type(n) == str:
        n = json.loads(n)

    if type(n) == int:
        return n

    return 3 * magnitude(n[0]) + 2 * magnitude(n[1])


n = lines[0]
for l in lines[1:]:
    n = add(n, l)

m = magnitude(n)
print(m)


# PART 2
res = -1
for n in lines:
    for m in lines:
        if n != m:
            res = max(res, magnitude(add(n, m)))

print(res)
