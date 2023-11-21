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
p1_parsed, p2_parsed = [], []
dop2 = False
for l in lines:
    if dop2 and l[0] != 'P':  # Aw yeah
        p2_parsed.append(int(l))
    else:
        if l == '':
            dop2 = True
        elif l[0] != 'P':
            p1_parsed.append(int(l))

# Last card at the beginning
p1 = [c for c in reversed(p1_parsed)]
p2 = [c for c in reversed(p2_parsed)]

while len(p1) > 0 and len(p2) > 0:
    card1, deck1 = p1[-1], [c for c in p1[0:-1]]
    card2, deck2 = p2[-1], [c for c in p2[0:-1]]

    if card1 > card2:
        p1, p2 = [card2, card1] + deck1, deck2
    else:
        p1, p2 = deck1, [card1, card2] + deck2

p = p1 if len(p2) == 0 else p2
res = sum([(idx + 1) * c for idx, c in enumerate(p)])
print(res)


# PART 2
def play(p1, p2):
    seen = set()

    while len(p1) > 0 and len(p2) > 0:
        key = ('-'.join(map(str, p1)), '-'.join(map(str, p2)))
        if key in seen:
            return p1, []
        else:
            seen.add(key)

        card1, deck1 = p1[0], [c for c in p1[1:]]
        card2, deck2 = p2[0], [c for c in p2[1:]]

        if card1 <= len(deck1) and card2 <= len(deck2):
            # Recurse
            recdeck1 = deck1[0:card1]
            recdeck2 = deck2[0:card2]

            res1, res2 = play(recdeck1, recdeck2)
            if len(res1) > 0:
                p1 = deck1 + [card1, card2]
                p2 = deck2
            else:
                p1 = deck1
                p2 = deck2 + [card2, card1]

        else:
            # Normal Combat
            if card1 > card2:
                p1, p2 = deck1 + [card1, card2], deck2
            else:
                p1, p2 = deck1, deck2 + [card2, card1]

    return p1, p2

# Last card at the end, easier in fact oO
p1 = [c for c in p1_parsed]
p2 = [c for c in p2_parsed]

p1, p2 = play(p1, p2)

p = p1 if len(p2) == 0 else p2
res = sum([(len(p) - idx) * c for idx, c in enumerate(p)])
print(res)



