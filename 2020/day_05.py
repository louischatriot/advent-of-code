import sys
import re
import u as u

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]

# PART 1
res = -1
seats = []
for l in lines:
    r, c = u.split_at_char(l, 7)

    rn = 0
    p = 1
    for i in reversed(r):
        if i == 'B':
            rn += p
        p *= 2

    cn = 0
    p = 1
    for i in reversed(c):
        if i == 'R':
            cn += p
        p *= 2

    sid = rn * 8 + cn
    res = max(res, sid)
    seats.append(sid)

print(res)


# PART 2
seats = sorted(seats)
res = None
for i in range(0, len(seats) - 1):
    if seats[i+1] - seats[i] == 2:
        res = seats[i] + 1

print(res)


