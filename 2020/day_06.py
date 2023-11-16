import sys
import re
import u as u

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]

lines.append('')

# PART 1
qs = dict()
res = 0
for l in lines:
    if l == '':
        res += len(qs)
        qs = dict()
        continue

    for c in l:
        qs[c] = True

print(res)


# PART 2
qs = dict()
lc = 0
res = 0
for l in lines:
    if l == '':
        res += sum([1 if qs[c] == lc else 0 for c in qs])
        qs = dict()
        lc = 0
        continue

    for c in l:
        if c not in qs:
            qs[c] = 0
        qs[c] += 1
    lc += 1

print(res)


