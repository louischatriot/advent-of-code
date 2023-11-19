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
idx = 0
rules = {}

while idx < len(lines):
    l = lines[idx]
    if l == '':
        break

    t, r = l.split(': ')
    rl, rr = r.split(' or ')
    rlb, rlu = rl.split('-')
    rrb, rru = rr.split('-')
    rlb, rlu, rrb, rru = int(rlb), int(rlu), int(rrb), int(rru)
    rules[t] = [[rlb, rlu], [rrb, rru]]

    idx += 1

idx += 2
your_ticket = [int(n) for n in lines[idx].split(',')]

idx += 3
tickets = []
while idx < len(lines):
    tickets.append([int(n) for n in lines[idx].split(',')])
    idx += 1

res = 0
valid_tickets = []
for t in tickets:
    valid = True
    for v in t:
        # Exactly one or per rule
        if not any(rule[0][0] <= v <= rule[0][1] or rule[1][0] <= v <= rule[1][1] for _, rule in rules.items()):
            res += v
            valid = False

    if valid:
        valid_tickets.append(t)

print(res)


# PART 2
rules_order = {t: [n for n in range(0, len(rules))] for t, r in rules.items()}

for t, r in rules.items():
    for ticket in valid_tickets:
        ok = []
        for i, v in enumerate(ticket):
            if r[0][0] <= v <= r[0][1] or r[1][0] <= v <= r[1][1]:
                ok.append(i)

        rules_order[t] = [n for n in rules_order[t] if n in ok]


to_prune = [o[0] for t, o in rules_order.items() if len(o) == 1]
while len(to_prune) > 0:
    tp = to_prune[0]
    to_prune = to_prune[1:]

    for t, o in rules_order.items():
        if len(o) > 1:
            rules_order[t] = [n for n in o if n != tp]
            if len(rules_order[t]) == 1:
                to_prune.append(rules_order[t][0])

res = 1
for t, _o in rules_order.items():
    o = _o[0]
    if t[0:9] == 'departure':
        res *= your_ticket[o]

print(res)

