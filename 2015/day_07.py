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
number_regex = re.compile('[0-9]+')

def get_val(expr, mem):
    if number_regex.search(expr):
        return int(expr)
    else:
        return mem[expr]

# OK, so the correct approach here would be a topological sort of instructions to avoid variable not found
# This has the same effect while being much less efficient (O(n2))
mem = dict()
done = set()
while len(done) < len(lines):
    for l in lines:
        if l in done:
            continue

        try:
            expr, dest = l.split(' -> ')

            if 'AND' in expr:
                a, b = expr.split(' AND ')
                mem[dest] = get_val(a, mem) & get_val(b, mem)

            elif 'OR' in expr:
                a, b = expr.split(' OR ')
                mem[dest] = get_val(a, mem) | get_val(b, mem)

            elif 'LSHIFT' in expr:
                a, b = expr.split(' LSHIFT ')
                mem[dest] = get_val(a, mem) << get_val(b, mem)

            elif 'RSHIFT' in expr:
                a, b = expr.split(' RSHIFT ')
                mem[dest] = get_val(a, mem) >> get_val(b, mem)

            elif 'NOT' in expr:
                a = expr[4:]
                mem[dest] = ~get_val(a, mem) % 65536

            else:
                mem[dest] = get_val(expr, mem)

            done.add(l)

        except Exception as e:
            continue  # Required variable not in memory

res_part1 = mem['a']
print(res_part1)


# PART 2
mem = dict()
done = set()
while len(done) < len(lines):
    for l in lines:
        if l in done:
            continue

        mem['b'] = res_part1

        try:
            expr, dest = l.split(' -> ')

            if 'AND' in expr:
                a, b = expr.split(' AND ')
                mem[dest] = get_val(a, mem) & get_val(b, mem)

            elif 'OR' in expr:
                a, b = expr.split(' OR ')
                mem[dest] = get_val(a, mem) | get_val(b, mem)

            elif 'LSHIFT' in expr:
                a, b = expr.split(' LSHIFT ')
                mem[dest] = get_val(a, mem) << get_val(b, mem)

            elif 'RSHIFT' in expr:
                a, b = expr.split(' RSHIFT ')
                mem[dest] = get_val(a, mem) >> get_val(b, mem)

            elif 'NOT' in expr:
                a = expr[4:]
                mem[dest] = ~get_val(a, mem) % 65536

            else:
                mem[dest] = get_val(expr, mem)

            done.add(l)

        except Exception as e:
            continue  # Required variable not in memory

print(mem['a'])

