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
actions = []
for l in lines:
    if l == 'deal into new stack':
        actions.append(('new stack', None))

    elif l[0:19] == 'deal with increment':
        _, n = l.split('deal with increment ')
        n = int(n)
        actions.append(('increment', n))

    elif l[0:3] == 'cut':
        _, n = l.split('cut ')
        n = int(n)
        actions.append(('cut', n))


def new_pos(pos, S, __type, n):
    if __type == 'increment':
        return (n * pos) % S

    elif __type == 'new stack':
        return - pos - 1 % S

    elif __type == 'cut':
        return (pos - n) % S

    else:
        raise ValueError('Unknown type')


def get_coeffs(actions, S):
    a, b = None, None

    for __type, n in actions:
        if __type == 'increment':
            c, d = n, 0

        elif __type == 'new stack':
            c, d = -1, -1

        elif __type == 'cut':
            c, d = 1, -n

        else:
            raise ValueError('Unknown type')

        if a is None:
            a, b = c, d
        else:
            a, b = (a * c) % S, (b * c + d) % S

    return (a, b)


def pos_after_shuffle(pos, S):
    for __type, n in actions:
        pos = new_pos(pos, S, __type, n)

    return pos


pos = 2019
S = 10007
print(pos_after_shuffle(pos, S))

# Better way to exponentiate for part 2
a, b = get_coeffs(actions, S)
res = (a * pos + b) % S
print(res)


# PART 2
S = 119315717514047
shuffles = 101741582076661

# One shuffle
a, b = get_coeffs(actions, S)

# All shuffles
A = u.fast_modular_exp(a, shuffles, S)
B = (u.fast_modular_exp(a, shuffles, S) - 1) % S
B *= u.fast_modular_exp(a-1, S-2, S)
B = (b * B) % S

pos = u.fast_modular_exp(A, S-2, S) * (2020 - B)
pos = pos % S

print('RESULT', pos)

res = (A * pos + B) % S
print('CHECK', res)



