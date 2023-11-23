import sys
import re
import u as u
from collections import defaultdict
import math

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1 & 2
called = list(map(int, lines[0].split(',')))

board = []
boards = []
for l in lines[2:]:
    if l == '':
        boards.append(board)
        board = []
    else:
        board.append(list(map(int, l.split())))

if len(board) > 0:
    boards.append(board)

results = []
for _ in range(0, len(boards)):
    res = [[0 for c in l] for l in boards[0]]
    results.append(res)

N = len(boards[0])  # Square boards

done_boards = set()

for c in called:
    for idx, board in enumerate(boards):
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == c:
                    results[idx][i][j] = 1

                    if sum(results[idx][i]) == N or sum([results[idx][ii][j] for ii in range(0, N)]) == N:
                        if len(done_boards) == 0:  # PART 1
                            res = 0
                            for ii in range(0, N):
                                for jj in range(0, N):
                                    if results[idx][ii][jj] == 0:
                                        res += boards[idx][ii][jj]

                            print(res * c)

                        if len(done_boards) == len(boards)-1 and idx not in done_boards:  # PART 2 - last to win
                            res = 0
                            for ii in range(0, N):
                                for jj in range(0, N):
                                    if results[idx][ii][jj] == 0:
                                        res += boards[idx][ii][jj]

                            print(res * c)

                        done_boards.add(idx)






