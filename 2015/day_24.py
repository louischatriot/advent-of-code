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
weights = list(int(l) for l in lines)

total = sum(weights)
per_bag = total // 3

""" Way too slow!
def all_subsets(weights, S):
    res = []

    if S == 0:
        return [set()]

    if len(weights) == 1:
        if weights[0] == S:
            return [{S}]
        else:
            return []

    if sum(weights) < S:
        return []

    for weight in weights:
        if weight > S:
            continue

        for subset in all_subsets([w for w in weights if w != weight], S - weight):
            res.append(subset.union({weight}))

    return res
"""

def is_possible_internal(weights, mem, S, w):
    if mem[S][w] is not None:
        return mem[S][w]

    if S == 0:
        mem[S][w] = True
        return True

    if w == 0:
        res = True if weights[0] == S else False
        mem[S][w] = res
        return res

    # To avoid lazy evaluation
    res = is_possible_internal(weights, mem, S, w-1)

    if S - weights[w] >= 0:
        res = is_possible_internal(weights, mem, S - weights[w], w-1) or res

    mem[S][w] = res
    return res


def is_possible(weights, S):
    mem = [[None for _ in range(len(weights))] for _ in range(S+1)]
    res = is_possible_internal(weights, mem, S, len(weights)-1)
    return res


def all_possibilities(weights, S, MAX_L=None):
    if MAX_L is None:
        MAX_L = len(weights)

    # Populate graph
    mem = [[None for _ in range(len(weights))] for _ in range(S+1)]
    is_possible_internal(weights, mem, per_bag, len(weights)-1)

    todo = [(set(), S, len(weights)-1)]
    done = []

    while len(todo) > 0:
        base, S, w = todo.pop(0)

        if S == 0:
            done.append(base)
            continue

        if w == 0:
            if weights[0] == S:
                done.append(base.union({S}))
            continue

        if len(base) >= MAX_L:
            continue

        if mem[S][w-1] is True:
            todo.append((base, S, w-1))

        new_S = S - weights[w]
        if new_S >= 0 and mem[new_S][w-1] is True:
            todo.append((base.union({weights[w]}), new_S, w-1))

    return done


weights_set = set(weights)

min_qe = 99999999999

for pos in all_possibilities(weights, per_bag, 6):
    new_weights = list(weights_set.difference(pos))
    if not is_possible(new_weights, per_bag):
        continue

    min_qe = min(min_qe, math.prod(pos))


print(min_qe)




