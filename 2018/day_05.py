import sys
import re
import u as u
from collections import defaultdict
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
data = [c for c in lines[0]]

# Much faster than deleting the first pattern we see then restarting from scratch
def collapse(data):
    redo = True
    while redo:
        redo = False
        __todo = list()

        for i, p in enumerate(u.pairwise(data)):
            a, b = p
            if abs(ord(a) - ord(b)) == 32:
                __todo.append(i)
                redo = True

        if redo:
            # Avoid deleting patterns such as cCc where only cC or Cc should be deleted
            todo = [__todo[0]]
            for i, j in u.pairwise(__todo):
                if j > i + 1:
                    todo.append(j)

            new_data = data[0:todo[0]]
            for i, j in u.pairwise(todo):
                new_data += data[i+2:j]
            new_data += data[todo[-1]+2:]

            data = new_data

    return data


res = len(collapse(data))
print(res)


# PART 2
m = res
for r in range(ord('A'), ord('A') + 26):
    rdata = [c for c in data if c not in [chr(r), chr(r+32)]]
    res = len(collapse(rdata))
    m = min(m, res)

print(m)







