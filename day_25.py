from time import time

with open("inputs/day_25.data") as file:
    lines = [line.rstrip() for line in file]

snalphabet = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
reversed_snalphabet = {v: k for k, v in snalphabet.items()}


snafus = [line for line in lines]   # Because I love it

def snafu_to_int(s):
    res = 0
    for p, c in enumerate(reversed(s)):
        res += snalphabet[c] * 5 ** p
    return res

def int_to_snafu(i):
    P = 0
    while abs(i) > 2 * 5 ** P + (5 ** P - 1) // 2:
        P += 1

    i += (5 ** (P+1) - 1) // 2
    l = []
    while i > 0:
        r = i % 5
        l.insert(0, r)
        i = (i - r) // 5

    return ''.join([reversed_snalphabet[d - 2] for d in l])




# Part 1

ints = [snafu_to_int(s) for s in snafus]
s = sum(ints)
res = int_to_snafu(s)
print(res)








