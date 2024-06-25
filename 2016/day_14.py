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
salt = lines[0]
print(salt)

# CLEAN :)
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
three = re.compile('(' + '|'.join([d * 3 for d in digits])  + ')')
fives = { d: re.compile(d * 5) for d in digits }

# ALLEÏ BOURRIN
SCAN = 50000
inwhat = 1000
hashes = list()
for i in range(SCAN+inwhat+1):
    t = u.generate_md5(salt + str(i))
    hashes.append(t)

keys = list()
for i in range(SCAN):
    m = three.search(hashes[i])
    if m:
        d = m.group(1)[0]
        for j in range(1, inwhat+1):
            if fives[d].search(hashes[i+j]):
                keys.append(i)
                break
    if len(keys) >= 64:
        break

print(keys[63])


# PART 2
HASHHASH = 2017

hashes = list()
for i in range(SCAN+inwhat+1):
    t = salt + str(i)
    for _ in range(HASHHASH):
        t = u.generate_md5(t)

    hashes.append(t)

keys = list()
for i in range(SCAN):
    m = three.search(hashes[i])
    if m:
        d = m.group(1)[0]
        for j in range(1, inwhat+1):
            if fives[d].search(hashes[i+j]):
                keys.append(i)
                break

    if len(keys) >= 64:
        break

print(keys[63])




# for d in digits:
    # last_five = SCAN + inwhat + 1

    # for i in reversed(range(SCAN)):
        # if fives[d].search(hashes[i]):
            # last_five = i

        # if last_five - i <= inwhat:
            # okay[d][i] = True

# keys = []

# for i in range(SCAN):
    # m = three.search(hashes[i])
    # if m:
        # d = m.group(1)[0]
        # if okay[d][i]:
            # keys.append(i)

# print(keys[63])

# print(keys)





