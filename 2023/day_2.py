with open("inputs/day_2.data") as file:
    lines = [line.rstrip() for line in file]

# A bit ugly to do like this but oh well
you_select = {'X': 1, 'Y': 2, 'Z': 3}
scores = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3,
}

for k in scores:
    scores[k] += you_select[k[-1]]

res = 0
for l in lines:
    res += scores[l]

# Part 1
print(res)


to_lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
to_win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
to_draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}


res = 0
for l in lines:
    if l[-1] == 'X':
        l = f"{l[0]} {to_lose[l[0]]}"
    elif l[-1] == 'Y':
        l = f"{l[0]} {to_draw[l[0]]}"
    else:
        l = f"{l[0]} {to_win[l[0]]}"

    res += scores[l]

# Part 2
print(res)


