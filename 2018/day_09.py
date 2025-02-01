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


# PART 1 & 2
data = lines[0].split()
players = int(data[0])
marbles = int(data[-2])

scores = defaultdict(lambda: 0)
zero = u.DoubleLinkedList(0)
current = zero

# Uncomment for part 2
# marbles *= 100

for m in range(1, marbles+1):
    if m % 23 == 0:
        player = ((m - 1) % players) + 1
        scores[player] += m

        for _ in range(6):
            current = current.prev

        scores[player] += current.prev.value
        current.prev.remove()

    else:
        current = current.next
        current.insert_value_after(m)
        current = current.next


res = 0
for k, v in scores.items():
    res = max(res, v)

print(res)




