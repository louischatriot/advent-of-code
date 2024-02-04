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
PWD_LENGTH = 8
former_password = lines[0]

# Assumes we always stay at 8 characters
def increment(word, pos = None):
    if pos is None:
        pos = len(word) - 1

    letter = word[pos]

    if letter != 'z':
        return word[0:pos] + chr(ord(letter) + 1) + word[pos+1:]
    else:
        return increment(word[0:pos] + 'a' + word[pos+1:], pos-1)

def find_next(pwd):
    while True:
        pwd = increment(pwd)

        if not any(c in pwd for c in ['i', 'o', 'l']):
            if any(ord(pwd[i]) == ord(pwd[i+1]) - 1 and ord(pwd[i+1]) == ord(pwd[i+2]) - 1 for i in range(len(pwd)-2)):
                if any(pwd[i] == pwd[i+1] and pwd[j] == pwd[j+1] and pwd[i] != pwd[j] for i, j in itertools.product(range(len(pwd)-1), range(len(pwd)-1))):
                    break

    return pwd

pwd = find_next(former_password)
print(pwd)


# PART 2
pwd = find_next(pwd)
print(pwd)



