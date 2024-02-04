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


# PART 1 & 2 (modify one line)
import hashlib

res = 1
while True:
    h = hashlib.new('md5')
    contents = lines[0] + str(res)
    contents = bytes(contents, 'ascii')
    h.update(bytes(lines[0] + str(res), 'ascii'))
    t = h.hexdigest()

    if h.hexdigest()[0:6] == '000000':
        break

    res += 1

print(res)


