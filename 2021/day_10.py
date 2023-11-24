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
matches = dict()
matches['('] = ')'
matches['['] = ']'
matches['{'] = '}'
matches['<'] = '>'

points = dict()
points[')'] = 3
points[']'] = 57
points['}'] = 1197
points['>'] = 25137

res = 0
good = []
for l in lines:
    s = []
    ok = True
    for c in l:
        if c in ['(', '[', '{', '<']:
            s.append(c)
        else:
            o = s.pop()
            if c != matches[o]:
                res += points[c]
                ok = False
                break
    if ok:
        good.append(l)

print(res)


# PART 2
points = dict()
points[')'] = 1
points[']'] = 2
points['}'] = 3
points['>'] = 4

scores = []
for l in good:
    s = []
    for c in l:
        if c in ['(', '[', '{', '<']:
            s.append(c)
        else:
            o = s.pop()

    missing = ''
    while len(s) > 0:
        missing += matches[s.pop()]

    score = 0
    for c in missing:
        score = 5 * score + points[c]

    scores.append(score)

scores = sorted(scores)
print(scores[len(scores) // 2])




