with open("inputs/day_12.data") as file:
    lines = [line.rstrip() for line in file]

map = [[c for c in line] for line in lines]

N = len(map)
M = len(map[0])

start = None
end = None
for i in range(0, N):
    for j in range(0, M):
        if map[i][j] == 'S':
            start = (i, j)
            map[i][j] = 'a'

        if map[i][j] == 'E':
            end = (i, j)
            map[i][j] = 'z'


transitions = [[[] for j in range(0, M)] for i in range(0, N)]
for i in range(0, N):
    for j in range(0, M):
        possible_dests = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        possible_dests = [(ii, jj) for ii, jj in possible_dests if 0 <= ii < N and 0 <= jj < M]
        possible_dests = [(ii, jj) for ii, jj in possible_dests if ord(map[ii][jj]) <= ord(map[i][j]) + 1]
        transitions[i][j] = possible_dests


def find_shortest_path_length(start, end):
    paths = [[None for j in range(0, M)] for i in range(0, N)]
    paths[start[0]][start[1]] = [start]
    boundary = [start]

    while paths[end[0]][end[1]] is None and len(boundary) > 0:
        i0, j0 = boundary.pop(0)

        for i, j in transitions[i0][j0]:
            if paths[i][j] is None:
                paths[i][j] = paths[i0][j0] + [(i, j)]
                boundary.append((i, j))

    if paths[end[0]][end[1]] is None:
        return 999999
    else:
        return len(paths[end[0]][end[1]]) - 1

# Part 1
print(find_shortest_path_length(start, end))


# Part 2
# Brute forcing it is pretty inefficient we could do a search from the end but oh well it works for this input
starts = []
for i in range(0, N):
    for j in range(0, M):
        if map[i][j] == 'a':
            starts.append((i, j))
lengths = [find_shortest_path_length(s, end) for s in starts]
print(min(lengths))






