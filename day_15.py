with open("inputs/day_15.data") as file:
    lines = [line.rstrip() for line in file]

data = []

for l in lines:
    l = l.split(': ')

    a = l[0][10:]
    a = a.split(', ')
    a = [int(p[2:]) for p in a]

    b = l[1][21:]
    b = b.split(', ')
    b = [int(p[2:]) for p in b]

    data.append([a, b])

def d(s, b):
    return abs(s[0] - b[0]) + abs(s[1] - b[1])


# Part 1

covered = []
line_n = 2000000

for s, b in data:
    delta = d(s, b) - abs(s[1] - line_n)

    if delta < 0:
        continue

    cl = s[0] - delta
    ch = s[0] + delta

    if len(covered) == 0:
        covered.append([cl, ch])
        continue

    il = None
    for i in range(0, len(covered)):
        sl = covered[i][0]
        sh = covered[i][1]

        if il is None and sl <= ch and sh >= cl:
            il = i
            break

    ih = None
    for i in range(len(covered) - 1, -1, -1):
        sl = covered[i][0]
        sh = covered[i][1]

        if ih is None and sl <= ch and sh >= cl:
            ih = i
            break

    if il is None:
        # No overlap, add to covered list
        i0 = None
        for i in range(0, len(covered)):
            if covered[i][0] > cl:
                i0 = i
                break

        if i0 is None:
            covered += [[cl, ch]]
        else:
            covered = covered[0:i] + [[cl, ch]] + covered[i:]

    else:
        cl = min(cl, covered[il][0])
        ch = max(ch, covered[ih][1])

        covered = ([] if il == 0 else covered[0:il-1]) + [[cl, ch]] + covered[ih+1:]



res = sum([sh - sl for sl, sh in covered])

print(res)






