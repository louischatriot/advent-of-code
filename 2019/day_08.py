import sys
import re
import u as u
# from collections import defaultdict, Counter
import collections
import math
import itertools

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
M = 25
N = 6
layer_length = M * N
image = lines[0]

best = layer_length + 1
res = None
for layer_n in range(len(image) // layer_length):
    layer = image[layer_length * layer_n: layer_length * (layer_n + 1)]
    count = collections.Counter(layer)
    if count['0'] < best:
        res = count['1'] * count['2']
        best = count['0']

print(res)


# PART 2
message = [[' ' for _ in range(M)] for _ in range(N)]

for i in range(0, N):
    for j in range(0, M):
        for layer_n in range(len(image) // layer_length):
            if message[i][j] != ' ':
                break

            p = layer_n * layer_length + M * i + j
            if image[p] == '0':
                message[i][j] = 'X'
                break
            elif image[p] == '1':
                message[i][j] = '.'
                break

for l in message:
    print(' '.join(l))


