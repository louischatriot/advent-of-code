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
N = int(lines[0])
offset = 0
res = 1

while N > 1:
    if N % 2 == 0:
        offset += 1
    else:
        offset += 1
        res += 2 ** offset

    N //= 2

print(res)


# PART 1
N = int(lines[0])
kill_pos = 1 + N // 2

first_dll = u.DoubleLinkedList(1)
prev_dll = first_dll
kill_dll = None
for i in range(2, N+1):
    dll = u.DoubleLinkedList(i)
    dll.add_after(prev_dll)
    prev_dll = dll

    if i == kill_pos:
        kill_dll = dll

first_dll.add_after(prev_dll)


current_size = N
remaining = kill_dll.next
while current_size > 4:
    if current_size % 2 == 0:
        next_kill_dll = kill_dll.next
    else:
        next_kill_dll = kill_dll.next.next

    kill_dll.remove()
    remaining = kill_dll.next
    kill_dll = next_kill_dll

    current_size -= 1


print(remaining.prev.value)


