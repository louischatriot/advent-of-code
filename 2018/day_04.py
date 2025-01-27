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
sleep_totals = defaultdict(lambda: 0)
by_minute = defaultdict(lambda: defaultdict(lambda: 0))

current_guard = None
current_sleep_start = None
for line in sorted(lines):
    timestamp, msg = line.split('] ')
    timestamp = timestamp[1:]

    if msg[0:5] == 'Guard':
        current_guard = int(msg.split(' ')[1][1:])
        continue

    if msg[0:5] == 'falls':
        current_sleep_start = int(timestamp[-2:])
        continue

    if msg[0:5] == 'wakes':
        wake_up = int(timestamp[-2:])
        sleep_totals[current_guard] += wake_up - current_sleep_start
        for m in range(current_sleep_start, wake_up):
            by_minute[current_guard][m] += 1
        continue

M = max(sleep_totals.values())
for g, v in sleep_totals.items():
    if v == M:
        guard = g
        break


M = max(by_minute[guard].values())
for m, v in by_minute[guard].items():
    if v == M:
        minute = m
        break

print(minute * guard)


# PART 2
M = 0
for guard in sleep_totals:
    for m, v in by_minute[guard].items():
        M = max(M, v)

for guard in sleep_totals:
    for m, v in by_minute[guard].items():
        if v == M:
            print(guard * m)
            break





