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
    lines = [line.rstrip() for line in file]


# PART 1
password = 'abcdefgh'
if is_example:
    password = 'abcde'

def scramble(password):
    for line in lines:
        if line.startswith('swap position'):
            a, b = line[14:].split(' with position ')
            a, b = int(a), int(b)
            m, M = min(a, b), max(a, b)
            password = password[0:m] + password[M] + password[m+1:M] + password[m] + password[M+1:]

        elif line.startswith('swap letter'):
            a, b = line[12:].split(' with letter ')
            a, b = password.index(a), password.index(b)
            m, M = min(a, b), max(a, b)
            password = password[0:m] + password[M] + password[m+1:M] + password[m] + password[M+1:]

        elif line.startswith('reverse positions'):
            a, b = line[18:].split(' through ')
            a, b = int(a), int(b)
            m, M = min(a, b), max(a, b)
            password = password[0:m] + ''.join([c for c in reversed(password[m:M+1])]) + password[M+1:]

        elif line.startswith('rotate based on position of letter '):
            l = line[-1]
            s = password.index(l)
            if s >= 4:
                s += 1
            s += 1
            password = ''.join([password[(i - s) % len(password)] for i in range(len(password))])

        elif line.startswith('rotate'):
            if line[7] == 'l':
                dir = -1
                line = line[12:]
            else:
                dir = 1
                line = line[13:]

            s = int(line.split()[0]) * dir
            password = ''.join([password[(i - s) % len(password)] for i in range(len(password))])

        elif line.startswith('move position'):
            l, t = line[14:].split(' to position ')
            l, t = int(l), int(t)

            if l < t:
                password = password[0:l] + password[l+1:t+1] + password[l] + password[t+1:]

            elif l > t:
                password = password[0:t] + password[l] + password[t:l] + password[l+1:]

        else:
            raise ValueError("Unexpected instruction")

    return password


print(scramble(password))


# PART 2
target = 'fbgdceah'
l = u.letters[0:8]

# WOW, should use itertools.permutations
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        for g in l:
                            for h in l:
                                t = [a, b, c, d, e, f, g, h]
                                if len(t) == len(set(t)):
                                    t = ''.join(t)
                                    if scramble(t) == target:
                                        print(t)
                                        sys.exit(0)







