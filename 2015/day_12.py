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
numbers = re.compile('[^"\'][-0-9]+')  # Hu hu hu
doc = lines[0]

res = 0
for m in numbers.finditer(doc):
    res += int(m.group()[1:])

print(res)


# PART 2
import json
doc = json.loads(lines[0])

def value_of(doc):
    if type(doc) == int:
        return doc

    if type(doc) == str:
        return 0

    res = 0

    if type(doc) == list:
        for v in doc:
            res += value_of(v)

    elif type(doc) == dict:
        if all(v != 'red' for k, v in doc.items()):
            for k, v in doc.items():
                res += value_of(v)

    else:
        raise ValueError("Unexpected type")

    return res


res = value_of(doc)
print(res)


