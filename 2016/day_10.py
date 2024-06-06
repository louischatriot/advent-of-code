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
outputs = defaultdict(lambda: [])
bots = defaultdict(lambda: [])
rules = dict()
queue = []

def add_to_bot(bots, queue, bot, v):
    bots[bot].append(v)
    if len(bots[bot]) == 2:
        queue.append(bot)

for line in lines:
    if line[0:5] == 'value':
        v, bot = line[6:].split(' goes to bot ')
        v, bot = int(v), int(bot)
        add_to_bot(bots, queue, bot, v)

    else:
        bot, s = line[4:].split(' gives low to ')
        bot = int(bot)
        low, high = s.split(' and high to ')
        lt, lb = low.split()
        lb = int(lb)
        ht, hb = high.split()
        hb = int(hb)
        rules[bot] = ((lt, lb), (ht, hb))

while len(queue) > 0:
    bot = queue.pop(0)

    if len(bots[bot]) != 2:
        raise ValueError

    v, V = min(bots[bot]), max(bots[bot])
    low, high = rules[bot]

    if v == 17 and V == 61:
        print("THE RIGHT BOT IS", bot)

    if low[0] == 'bot':
        add_to_bot(bots, queue, low[1], v)
    else:
        outputs[low[1]].append(v)

    if high[0] == 'bot':
        add_to_bot(bots, queue, high[1], V)
    else:
        outputs[high[1]].append(V)


# PART 2
res = outputs[0][0] * outputs[1][0] * outputs[2][0]
print(res)





