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
data = [int(l) for l in lines]
res = 0
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        res += 1
print(res)


# PART 2
measurements = []
for i in range(0, len(data) - 2):
    measurements.append(data[i] + data[i+1] + data[i+2])

res = 0
for i in range(1, len(measurements)):
    if measurements[i] > measurements[i-1]:
        res += 1
print(res)



