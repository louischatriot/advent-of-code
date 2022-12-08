with open("inputs/day_8.data") as file:
    lines = [line.rstrip() for line in file]

forest = [[int(t) for t in line] for line in lines]

N = len(forest)
M = len(forest[0])

left = [[-1 for j in range(0, M)] for i in range(0, N)]
right = [[-1 for j in range(0, M)] for i in range(0, N)]
top = [[-1 for j in range(0, M)] for i in range(0, N)]
bottom = [[-1 for j in range(0, M)] for i in range(0, N)]


# Could be more compact but less legible
for i in range(0, N):
    for j in range(1, M):
        left[i][j] = max(left[i][j-1], forest[i][j-1])

    for j in range(M-2, -1, -1):
        right[i][j] = max(right[i][j+1], forest[i][j+1])

for j in range(0, M):
    for i in range(1, N):
        top[i][j] = max(top[i-1][j], forest[i-1][j])

    for i in range(N-2, -1, -1):
        bottom[i][j] = max(bottom[i+1][j], forest[i+1][j])


# Part 1
res = 0
for i in range(0, N):
    for j in range(0, M):
        if forest[i][j] > min(left[i][j], right[i][j], top[i][j], bottom[i][j]):
            res += 1

print(res)


# Part 2

max_score = 0
for i in range(0, N):
    for j in range(0, M):
        score = 1

        # Right
        c = 0
        for jj in range(j+1, M):
            c += 1
            if forest[i][jj] >= forest[i][j]:
                break
        score *= c

        # Left
        c = 0
        for jj in range(j-1, -1, -1):
            c += 1
            if forest[i][jj] >= forest[i][j]:
                break
        score *= c

        # Bottom
        c = 0
        for ii in range(i+1, N):
            c += 1
            if forest[ii][j] >= forest[i][j]:
                break
        score *= c

        # Top
        c = 0
        for ii in range(i-1, -1, -1):
            c += 1
            if forest[ii][j] >= forest[i][j]:
                break
        score *= c

        max_score = max(max_score, score)

print(max_score)

