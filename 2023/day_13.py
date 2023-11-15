import ast
import functools

with open("inputs/day_13.data") as file:
    lines = [line.rstrip() for line in file]


left = []
right = []
l = True

for line in lines:
    if line != '':
        if l:
            left.append(line)
        else:
            right.append(line)

        l = not l

left = [ast.literal_eval(l) for l in left]
right = [ast.literal_eval(r) for r in right]
N = len(left)



def compare(l, r):
    if len(l) == 0 and len(r) > 0:
        return 1

    if len(l) > 0 and len(r) == 0:
        return -1

    if len(l) == 0 and len(r) == 0:
        return 0

    fl, fr = l[0], r[0]
    tail_l, tail_r = l[1:], r[1:]

    if type(fl) == int and type(fr) == int:
        if fl < fr:
            return 1
        elif fl > fr:
            return -1
        else:
            return compare(tail_l, tail_r)

    if type(fl) == int:
        fl = [fl]

    if type(fr) == int:
        fr = [fr]

    c = compare(fl, fr)
    if c == 1:
        return 1
    elif c == -1:
        return -1
    else:
        return compare(tail_l, tail_r)


# Part 1
res = 0
for i in range(0, N):
    if compare(left[i], right[i]) == 1:
        res += i+1

print(res)


# Part 2

with open("inputs/day_13.data") as file:
    lines = [line.rstrip() for line in file]

signals = [ast.literal_eval(line) for line in lines if line != '']

signals.append([[2]])
signals.append([[6]])

signals.sort(key=functools.cmp_to_key(compare))
signals = [str(s) for s in reversed(signals)]

res = (signals.index('[[2]]') + 1) * (signals.index('[[6]]') + 1)
print(res)



