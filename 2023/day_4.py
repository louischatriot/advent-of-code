with open("inputs/day_4.data") as file:
    lines = [line.rstrip() for line in file]

def contains(s):
    l, r = s.split(',')
    l1, l2 = l.split('-')
    r1, r2 = r.split('-')
    l1, l2, r1, r2 = int(l1), int(l2), int(r1), int(r2)

    return (l1 <= r1 and l2 >= r2) or (r1 <= l1 and r2 >= l2)

def overlaps(s):
    l, r = s.split(',')
    l1, l2 = l.split('-')
    r1, r2 = r.split('-')
    l1, l2, r1, r2 = int(l1), int(l2), int(r1), int(r2)

    return (l1 <= r1 <= l2) or (l1 <= r2 <= l2) or contains(s)


# Part 1
res = 0
for line in lines:
    res += 1 if contains(line) else 0

print(res)


# Part 2
res = 0
for line in lines:
    res += 1 if overlaps(line) else 0

print(res)
