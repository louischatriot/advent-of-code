import sys
import re
import u as u
from collections import defaultdict
import math
import itertools

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
hands = []
for l in lines:
    hand, bid = l.split()
    hands.append((hand, int(bid)))

card_order = list(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']))
card_strength = { c: i for i, c in enumerate(card_order) }

def pure_hand_strength(hand):
    res = 0
    N = len(card_strength)
    for i, c in enumerate(reversed(hand)):
        res += N ** i * card_strength[c]
    return res

M = 10 ** (1 + math.ceil(math.log(pure_hand_strength('AAAAA')) / math.log(10)))  # For readability

# Higher = better
def kind(card):
    dist = defaultdict(lambda: 0)
    for c in card:
        dist[c] += 1

    if any(dist[c] == 5 for c in card_order):
        return 7 * M

    if any(dist[c] == 4 for c in card_order):
        return 6 * M

    if any(dist[c] == 3 for c in card_order) and any(dist[c] == 2 for c in card_order):
        return 5 * M

    if any(dist[c] == 3 for c in card_order):
        return 4 * M

    pairs = 0
    for c in card_order:
        if dist[c] == 2:
            pairs += 1

    if pairs == 2:
        return 3 * M

    if pairs == 1:
        return 2 * M

    return M

def strength(bucket):
    hand = bucket[0]
    return kind(hand) + pure_hand_strength(hand)

hands.sort(key=strength)

res = 0
for i, bucket in enumerate(hands):
    hand, bid = bucket
    res += (i+1) * bid

print(res)


# PART 2
new_card_order = list(reversed(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']))
new_card_strength = { c: i for i, c in enumerate(new_card_order) }

def new_pure_hand_strength(hand):
    res = 0
    N = len(new_card_strength)
    for i, c in enumerate(reversed(hand)):
        res += N ** i * new_card_strength[c]
    return res

def new_kind(card):
    if 'J' not in card:
        return kind(card)

    if card == 'JJJJJ':
        return 7 * M

    dist = defaultdict(lambda: 0)
    for c in card:
        dist[c] += 1

    non_jokers = []
    for c, v in dist.items():
        if v > 0 and c != 'J':
            non_jokers.append(c)

    # Totally too lazy to actually think about the structure of the problem vs trying every combination
    best = 0
    for s in itertools.product(non_jokers, repeat=dist['J']):
        joker_idx = 0
        new_card = ''
        for c in card:
            if c != 'J':
                new_card += c
            else:
                new_card += s[joker_idx]
                joker_idx += 1

        best = max(best, kind(new_card))

    return best

def new_strength(bucket):
    hand = bucket[0]
    return new_kind(hand) + new_pure_hand_strength(hand)

hands.sort(key=new_strength)

res = 0
for i, bucket in enumerate(hands):
    hand, bid = bucket
    res += (i+1) * bid

print(res)





