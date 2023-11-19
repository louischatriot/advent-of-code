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
def solve_simple(e):
    l = []
    n = ''
    for c in e:
        if c in ['+', '*']:
            l.append(int(n))
            l.append(c)
            n = ''
        else:
            n = n + c

    l.append(int(n))

    while len(l) > 1:
        a, op, b, l = l[0], l[1], l[2], l[3:]
        l = [a+b if op == '+' else a*b] + l

    return l[0]


def solve(exp):
    s = []
    for c in exp:
        if c == '(':
            s.append(c)
            s.append('')
        elif c == ')':
            e = s.pop()
            e = str(solve_simple(e))

            s.pop()

            if len(s) == 0:
                s = [e]
            else:
                s[-1] += e
        else:
            if len(s) == 0:
                s = ['']
            s[-1] += c

    return solve_simple(s[0])


res = 0
for l in lines:
    l = l.replace(' ', '')
    res += solve(l)

print(res)


# PART 2
def solve_simple_2(e):
    l = []
    n = ''
    for c in e:
        if c in ['+', '*']:
            l.append(int(n))
            l.append(c)
            n = ''
        else:
            n = n + c

    l.append(int(n))

    todo = True
    while todo:
        todo = False
        for idx, op in enumerate(l):
            if op == '+':
                l = l[0:idx-1] + [l[idx-1] + l[idx+1]] + l[idx+2:]
                todo = True
                break

    while len(l) > 1:
        a, op, b, l = l[0], l[1], l[2], l[3:]
        l = [a+b if op == '+' else a*b] + l

    return l[0]


def solve(exp):
    s = []
    for c in exp:
        if c == '(':
            s.append(c)
            s.append('')
        elif c == ')':
            e = s.pop()
            e = str(solve_simple_2(e))

            s.pop()

            if len(s) == 0:
                s = [e]
            else:
                s[-1] += e
        else:
            if len(s) == 0:
                s = ['']
            s[-1] += c

    return solve_simple_2(s[0])


res = 0
for l in lines:
    l = l.replace(' ', '')
    s = solve(l)
    res += s

print(res)




