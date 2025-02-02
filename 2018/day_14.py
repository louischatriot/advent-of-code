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
    lines = [line[0:-1] for line in file]


# PART 1
target = int(lines[0])

start = u.DoubleLinkedList(3)
start.insert_value_after(7)
end = start.next
e1 = start
e2 = end
length = 2

while length < target + 10:
    v = e1.value + e2.value
    if v < 10:
        end.insert_value_after(v)
        end = end.next
        length += 1
    else:
        a, b = v // 10, v % 10
        end.insert_value_after(a)
        end = end.next
        end.insert_value_after(b)
        end = end.next
        length += 2

    for _ in range(1 + e1.value):
        e1 = e1.next

    for _ in range(1 + e2.value):
        e2 = e2.next

current = start
for _ in range(target):
    current = current.next

res = ''
for _ in range(10):
    res += str(current.value)
    current = current.next

print(res)


# PART 2
# Actually using a string is much faster than a double linked list ...
s = '37'
e1 = 0
e2 = 1
target = '589167' if is_example else '825401'

while True:
    v = int(s[e1]) + int(s[e2])
    to_insert = [v] if v < 10 else [v // 10, v % 10]
    for v in to_insert:
        s += str(v)

        if s[-len(target):] == target:
            print(len(s) - len(target))
            sys.exit(0)

    e1 = (e1 + 1 + int(s[e1])) % len(s)
    e2 = (e2 + 1 + int(s[e2])) % len(s)





