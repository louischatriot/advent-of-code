import sys
import re
import u as u
from collections import defaultdict

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
depart = int(lines[0])
buses = [int(b) for b in filter(lambda b: b!= 'x', lines[1].split(','))]

print(depart)
print(buses)



