def get_priority(i):
    if 'a' <= i <= 'z':
        p = ord(i) + 1 - ord('a')
    else:
        p = ord(i) + 27 - ord('A')

    return p



with open("inputs/day_3.data") as file:
    lines = [line.rstrip() for line in file]

# Part 1
res = 0
for line in lines:
    l = line[0:len(line)//2]
    r = line[len(line)//2:]
    i = (set(l).intersection(set(r))).pop()
    res += get_priority(i)

print(res)


# Part 2
res = 0
for i in range(0, len(lines), 3):
    i = (set(lines[i]).intersection(set(lines[i+1])).intersection(set(lines[i+2]))).pop()
    res += get_priority(i)

print(res)
