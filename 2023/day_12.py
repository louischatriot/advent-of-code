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
# Brute forcing the shit out of it instead of going smart with leftmost and rightmost (and knowing I will regret it for part 2)
# cf this more efficient algorithm https://github.com/louischatriot/small-katas/blob/main/nonograms.py
# Memoization brings only a minor speed up, removed it
mem = dict()

def get_possibilities(clue, L):
    CL = len(clue) - 1 + sum(clue)

    if L == CL:
        return ['.'.join('#' * c for c in clue)]

    key = '-'.join(map(str, clue)) + '--' + str(L)
    if key in mem:
        return mem[key]

    res = []
    fc, clues = clue[0], clue[1:]
    for offset in range(0, L - CL + 1):
        base = '.' * offset + '#' * fc

        if len(clues) == 0:
            base += '.' * (L - len(base))
            res.append(base)
        else:
            base += '.'
            pos = get_possibilities(clues, L - len(base))
            res += [base + p for p in pos]

    mem[key] = res
    return res


res = 0
for l in lines:
    state, clue = l.split(' ')
    clue = list(map(int, clue.split(',')))

    matches = 0
    for pos in get_possibilities(clue, len(state)):
        if all(s == p or s == '?' for p, s in zip(pos, state)):
            matches += 1

    res += matches

print(res)


# PART 2
mem = dict()

# Clue lookup can be optimized in both the recursion and the terminal case (and in could be memoized for the terminal case)
# But fast enough as of now
def n_matches(clues, state, depth=0):
    S = len(state)

    if len(clues) == 1:
        clue = clues[0]
        res = 0
        for i in range(0, S - clue + 1):
            if all(elt != '#' for elt in state[0:i]) and all(elt != '.' for elt in state[i:i+clue]) and all(elt != '#' for elt in state[i+clue:]):
                res += 1
        return res

    mem_key = '-'.join(map(str, clues)) + '--' + state
    if mem_key in mem:
        return mem[mem_key]

    res = 0
    max_i = S - (sum(clues) + len(clues) - 1)
    clue, clues = clues[0], clues[1:]

    for i in range(0, max_i + 1):
        if all(elt != '.' for elt in state[i:i+clue]) and all(elt != '#' for elt in state[0:i]) and state[i+clue] != '#':
            res += n_matches(clues, state[i+clue+1:], depth+1)

    mem[mem_key] = res
    return res


res = 0
for l in lines:
    state, clues = l.split(' ')
    clues = list(map(int, clues.split(',')))

    state = '?'.join([state for _ in range(0,5)])
    clues = [c for c in clues] + [c for c in clues] + [c for c in clues] + [c for c in clues] + [c for c in clues]

    matches = n_matches(clues, state)
    res += matches

print(res)





