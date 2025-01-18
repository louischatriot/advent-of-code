import sys
import re
import u as u
from collections import defaultdict, deque
import math
import itertools
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
score = 0
current_score = 0
i = 0
data = lines[0]
garbages = 0

while i < len(data):
    c = data[i]

    if c == '!':
        i += 2
        continue

    # Go right to the end of garbage
    if c == '<':
        i += 1

        while True:
            c = data[i]

            if c == '!':
                i += 2
                continue

            if c == '>':
                i += 1
                break

            garbages += 1
            i += 1

        continue

    if c == '{':
        current_score += 1

    elif c == '}':
        score += current_score
        current_score -= 1

    else:
        if c != ',':
            raise ValueError("Should be a comma")

    i += 1



print(score)
print(garbages)









