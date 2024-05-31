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
import hashlib

res = 1
password = ''

while True:
    h = hashlib.new('md5')
    contents = lines[0] + str(res)
    contents = bytes(contents, 'ascii')
    h.update(bytes(lines[0] + str(res), 'ascii'))
    t = h.hexdigest()

    if t[0:5] == '00000':
        password += t[5]
        print(password)   # Keeping this it's fun to see it "crack"
        if len(password) == 8:
            break

    res += 1

print("PASSWORD FOUND", password)


# PART 2
res = 1
password = ['-', '-', '-', '-', '-', '-', '-', '-']
found = 0

while True:
    h = hashlib.new('md5')
    contents = lines[0] + str(res)
    contents = bytes(contents, 'ascii')
    h.update(bytes(lines[0] + str(res), 'ascii'))
    t = h.hexdigest()

    if t[0:5] == '00000':
        if ord('0') <= ord(t[5]) <= ord('7'):
            if password[int(t[5])] == '-':
                password[int(t[5])] = t[6]
                found += 1
                print(password)   # Keeping this it's fun to see it "crack"

                if found == 8:
                    break

    res += 1

print("PASSWORD FOUND", ''.join(password))





