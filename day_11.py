with open("inputs/day_11_example.data") as file:
    lines = [line.rstrip() for line in file]


# Example
wd = 1
bigm = 23 * 19 * 13 * 17
monkeys = [
    [79, 98],
    [54, 65, 75, 74],
    [79, 60, 97],
    [74]
]

tests = [
    lambda w: ((w * 19) // wd, 2 if ((w * 19) // wd) % 23 == 0 else 3),
    lambda w: ((w +  6) // wd, 2 if ((w +  6) // wd) % 19 == 0 else 0),
    lambda w: ((w *  w) // wd, 1 if ((w *  w) // wd) % 13 == 0 else 3),
    lambda w: ((w +  3) // wd, 0 if ((w +  3) // wd) % 17 == 0 else 1)
]


# Could have written a parser :)
wd = 1
bigm = 11 * 2 * 5 * 17 * 19 * 7 * 3 * 13
monkeys = [
    [92, 73, 86, 83, 65, 51, 55, 93],
    [99, 67, 62, 61, 59, 98],
    [81, 89, 56, 61, 99],
    [97, 74, 68],
    [78, 73],
    [50],
    [95, 88, 53, 75],
    [50, 77, 98, 85, 94, 56, 89]
]

tests = [
    lambda w: ((w * 5) // wd, 3 if ((w * 5) // wd) % 11 == 0 else 4),
    lambda w: ((w * w) // wd, 6 if ((w * w) // wd) % 2 == 0 else 7),
    lambda w: ((w * 7) // wd, 1 if ((w * 7) // wd) % 5 == 0 else 5),
    lambda w: ((w + 1) // wd, 2 if ((w + 1) // wd) % 17 == 0 else 5),
    lambda w: ((w + 3) // wd, 2 if ((w + 3) // wd) % 19 == 0 else 3),
    lambda w: ((w + 5) // wd, 1 if ((w + 5) // wd) % 7 == 0 else 6),
    lambda w: ((w + 8) // wd, 0 if ((w + 8) // wd) % 3 == 0 else 7),
    lambda w: ((w + 2) // wd, 4 if ((w + 2) // wd) % 13 == 0 else 0)
]


# Part 1 (and 2 actually)

inspections = [0 for _ in range(0, len(monkeys))]
N = 10000

for _ in range(0, N):
    for i, m in enumerate(monkeys):
        for _ in range(0, len(m)):
            inspections[i] += 1
            w = m.pop(0)
            w, t = tests[i](w)
            monkeys[t].append(w % bigm)





print("====================================")
print(inspections)
print(sorted(inspections))
s = sorted(inspections)
print(s[-1] * s[-2])
print("====================================")
print(monkeys)





