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
if not is_example:
    computer.memory['a'] = 7

computer.run()
print(computer.get_value('a'))


# PART 2
faster_program = [line for line in lines]
faster_program = faster_program[0:2] + ['fun'] + faster_program[16:]
faster_program[4] = 'cpy -3 c'

computer = Assembunny(faster_program)
if not is_example:
    computer.memory['a'] = 12

computer.run()
print(computer.memory)



