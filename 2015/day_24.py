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


print(weights, per_bag)


mem = [[None for _ in range(len(weights))] for _ in range(per_bag+1)]

def is_possible(weights, mem, S, w):
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
    res = is_possible(weights, mem, S, w-1)

    if S - weights[w] >= 0:
        res = is_possible(weights, mem, S - weights[w], w-1) or res

    mem[S][w] = res
    return res


res = is_possible(weights, mem, per_bag, len(weights)-1)
print(res)

for l in mem:
    print(['TRUE' if c else '----' for c in l])


def all_possibilities(weights, mem, S, w):
    todo = [(set(), S, w)]
    done = []

    while len(todo) > 0:
        base, S, w = todo.pop(0)

        if S == 0:
            print(base)
            done.append(base)
            continue

        if w == 0:
            if weights[0] == S:
                print(base)
                done.append(base.union({S}))
            continue

        if mem[S][w-1] is True:
            todo.append((base, S, w-1))

        new_S = S - weights[w]
        if new_S >= 0 and mem[new_S][w-1] is True:
            todo.append((base.union({weights[w]}), new_S, w-1))

    return done


res = all_possibilities(weights, mem, per_bag, len(weights)-1)

print(len(res))


"""
res = is_possible(weights, mem, per_bag, 3)
print(res)

for l in mem:
    print(['TRUE' if c else '----' for c in l])
"""




sys.exit(0)


possibilities = [[None for _ in range(len(weights))] for _ in range(per_bag+1)]

possibilities[weights[0]][0] = True

for weight_max in range(len(weights)-1):
    for S in range(1, per_bag+1):
        if possibilities[S][weight_max]:
            possibilities[S][weight_max + 1] = True

            new_S = S + weights[weight_max + 1] 
            if new_S <= per_bag:
                possibilities[new_S][weight_max + 1] = True

print(possibilities[per_bag][-1])


for l in possibilities:
    print(['TRUE' if c else '----' for c in l])











