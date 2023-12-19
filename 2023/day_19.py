import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import numpy as np

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
workflows = defaultdict(lambda: list())
parts = list()
do_parts = False

for l in lines:
    if l == '':
        do_parts = True
        continue

    if not do_parts:
        name, contents = l.split('{')
        contents = contents[0:-1].split(',')

        for content in contents[0:-1]:
            condition, dest = content.split(':')
            op = '<' if '<' in condition else '>'
            dim, v = condition.split(op)
            workflows[name].append((dim, op, int(v), dest))

        workflows[name].append(contents[-1])

    else:
        part = l[1:-1].split(',')
        __part = {p.split('=')[0]: int(p.split('=')[1]) for p in part}
        parts.append(__part)

def compare(a, op, b):
    if op == '<':
        return a < b

    elif op == '>':
        return a > b

    else:
        raise ValueError("Unexpected operator")

def follow(workflows, part):
    start = 'in'
    end_accepted = 'A'
    end_refused = 'R'

    current = start
    while True:
        workflow = workflows[current]

        for rule in workflow:
            if type(rule) == str:
                current = rule
                break

            else:
                dim, op, val, dest = rule
                if compare(part[dim], op, val):
                    current = dest
                    break


        if current in [end_accepted, end_refused]:
            break

    return current == end_accepted

res = 0
for part in parts:
    if follow(workflows, part):
        res += sum(v for _, v in part.items())

print(res)


# PART 2
def split(bucket, dim, op, val):
    l, h = bucket[dim]

    if (op == '<' and l >= val) or (op == '>' and h <= val):
        return None, bucket

    if (op == '<' and h < val) or (op == '>' and l >= val):
        return bucket, None

    yes = {k: v for k, v in bucket.items()}
    no = {k: v for k, v in bucket.items()}

    if op == '<':
        yes[dim] = (l, val-1)
        no[dim] = (val, h)
    else:
        yes[dim] = (val+1, h)
        no[dim] = (l, val)

    return yes, no



def follows(workflows, bucket, _from):
    if _from == 'A':
        return [bucket]
    elif _from == 'R':
        return []

    buckets = []
    no = bucket

    for dim, op, val, dest in workflows[_from][0:-1]:
        yes, no = split(no, dim, op, val)

        if yes is not None:
            for b in follows(workflows, yes, dest):
                buckets.append(b)

        if no is None:
            break

    if no is not None:
        end_rule = workflows[_from][-1]
        for b in follows(workflows, no, end_rule):
            buckets.append(b)

    return buckets


bucket = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
buckets = follows(workflows, bucket, 'in')

res = 0
for bucket in buckets:
    res += (bucket['x'][1] - bucket['x'][0] + 1) * (bucket['m'][1] - bucket['m'][0] + 1) * (bucket['a'][1] - bucket['a'][0] + 1) * (bucket['s'][1] - bucket['s'][0] + 1)

print(res)


