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
from assembunny import Assembunny

computer = Assembunny(lines)
computer.run()
print(computer.get_value('a'))


# PART 2
computer = Assembunny(lines)
computer.set_value('c', 1)
computer.run()
print(computer.get_value('a'))




