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
s = lines[0]

R = 40
for _ in range(R):
    new_s = ''
    d = s[0]
    n = 1

    for c in s[1:]:
        if c != d:
            new_s += str(n) + str(d)
            d = c
            n = 1
        else:
            n += 1

    new_s += str(n) + str(d)
    s = new_s

print(len(s))


# PART 2
# Reusing part 1 works, but is really slow. Looking into speeding it up.
# Will look into the sequence's cosmological decay (seehttps://en.wikipedia.org/wiki/Look-and-say_sequence)
# to break it into forecastable and independent pieces



