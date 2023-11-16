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
program = []
for _l in lines:
    l = _l.split(' ')
    program.append((l[0], int(l[1])))


def run(program, change):
    visited = set()
    pointer = 0
    acc = 0
    while True:
        if pointer in visited:
            return acc, True

        if pointer == len(program):
            return acc, False

        inst, val = program[pointer]
        visited.add(pointer)

        if change == pointer:
            if inst == 'nop':
                inst = 'jmp'
            elif inst == 'jmp':
                inst = 'nop'

        if inst == 'nop':
            pointer += 1
            pass
        elif inst == 'acc':
            acc += val
            pointer += 1
        elif inst == 'jmp':
            pointer += val

acc, error = run(program, None)
print(acc)


# PART 2
for c in range(0, len(program)):
    acc, error = run(program, c)
    if not error:
        print(acc)




