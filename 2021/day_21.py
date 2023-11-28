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


# PART 1
# Zero-base positions
pos1 = int(lines[0][28:]) - 1
pos2 = int(lines[1][28:]) - 1

# Zero-base the die as well
die_next = 1 - 1
rolls = 0

score1, score2 = 0, 0

while score1 < 1000 and score2 < 1000:
    d = 0
    for _ in range(0, 3):
        d += die_next + 1
        die_next = (die_next + 1) % 100
        rolls += 1

    pos1 = (pos1 + d) % 10
    score1 += pos1 + 1

    if score1 >= 1000:
        break

    d = 0
    for _ in range(0, 3):
        d += die_next + 1
        die_next = (die_next + 1) % 100
        rolls += 1

    pos2 = (pos2 + d) % 10
    score2 += pos2 + 1

if score1 >= 1000:
    print(rolls * score2)
else:
    print(rolls * score1)


# PART 2
# Everything zero-baseed as well
pos1 = int(lines[0][28:]) - 1
pos2 = int(lines[1][28:]) - 1
MAX_SCORE = 21

dice = [i+j+k for i in range(1, 4) for j in range(1, 4) for k in range(1,4)]
dice_freq = defaultdict(lambda: 0)
for d in dice:
    dice_freq[d] += 1

mem = dict()
def key(pos1, pos2, score1, score2, next_player):
    return f"{pos1}-{pos2}-{score1}-{score2}-P{next_player}"


def wins(pos1, pos2, score1, score2, next_player):
    if score1 >= MAX_SCORE:
        return (1, 0)

    if score2 >= MAX_SCORE:
        return (0, 1)

    _key = key(pos1, pos2, score1, score2, next_player)
    if _key in mem:
        return mem[_key]

    wins1, wins2 = 0, 0
    for d, freq in dice_freq.items():
        if next_player == 1:
            new_pos1 = (pos1 + d) % 10
            w1, w2 = wins(new_pos1, pos2, score1 + new_pos1 + 1, score2, 2)
        else:
            new_pos2 = (pos2 + d) % 10
            w1, w2 = wins(pos1, new_pos2, score1, score2 + new_pos2 + 1, 1)

        wins1, wins2 = wins1 + freq * w1, wins2 + freq * w2

    mem[_key] = (wins1, wins2)
    return (wins1, wins2)


wins1, wins2 = wins(pos1, pos2, 0, 0, 1)
print(wins1, wins2)



