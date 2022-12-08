

"""
Should parse it cleanly but it's a pain :)
        [H]     [W] [B]
    [D] [B]     [L] [G] [N]
[P] [J] [T]     [M] [R] [D]
[V] [F] [V]     [F] [Z] [B]     [C]
[Z] [V] [S]     [G] [H] [C] [Q] [R]
[W] [W] [L] [J] [B] [V] [P] [B] [Z]
[D] [S] [M] [S] [Z] [W] [J] [T] [G]
[T] [L] [Z] [R] [C] [Q] [V] [P] [H]
 1   2   3   4   5   6   7   8   9
 """

stacks = [
    [],   # Unused stack 0
    ['T', 'D', 'W', 'Z', 'V', 'P'],
    ['L', 'S', 'W', 'V', 'F', 'J', 'D'],
    ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
    ['R', 'S', 'J'],
    ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
    ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'],
    ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
    ['P', 'T', 'B', 'Q'],
    ['H', 'G', 'Z', 'R', 'C']
]


with open("inputs/day_5.data") as file:
    lines = [line.rstrip() for line in file]


parsed = []
for line in lines:
    line = line[5:]
    if '0' <= line[1] <= '9':   # Always one or two digits
        n = int(line[0:2])
        line = line[8:]
    else:
        n = int(line[0])
        line = line[7:]

    sf = int(line[0])
    st = int(line[-1])


    for i in range(0, n):
        stacks[st].append(stacks[sf].pop())

for s in stacks:
    print(s)





