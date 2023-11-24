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
inputs, outputs = [], []
for l in lines:
    _in, _out = l.split(' | ')
    inputs.append(_in.split(' '))
    outputs.append(_out.split(' '))

res = 0
for _out in outputs:
    for s in _out:
        if len(s) in [2, 3, 4, 7]:
            res += 1

print(res)


# PART 2
true_numbers = dict()
true_numbers['abcefg'] = '0'
true_numbers['cf'] = '1'
true_numbers['acdeg'] = '2'
true_numbers['acdfg'] = '3'
true_numbers['bcdf'] = '4'
true_numbers['abdfg'] = '5'
true_numbers['abdefg'] = '6'
true_numbers['acf'] = '7'
true_numbers['abcdefg'] = '8'
true_numbers['abcdfg'] = '9'

res = 0

for input, output in zip(inputs, outputs):
    mapping = dict()

    one = next(filter(lambda x: len(x) == 2, input))
    four = next(filter(lambda x: len(x) == 4, input))
    seven = next(filter(lambda x: len(x) == 3, input))
    eight = next(filter(lambda x: len(x) == 7, input))
    mapping['a'] = next(c for c in seven if c not in one)
    three = next(filter(lambda x: len(x) == 5 and all(c in x for c in seven), input))
    mapping['b'] = next(c for c in four if c not in three)
    mapping['d'] = next(c for c in four if c in three and c not in one)
    five = next(filter(lambda x: len(x) == 5 and mapping['b'] in x, input))
    mapping['c'] = next(c for c in three if c not in five)
    mapping['f'] = next(c for c in one if c != mapping['c'])
    two = next(filter(lambda x: len(x) == 5 and x != three and x != five, input))
    mapping['e'] = next(c for c in two if c not in three)
    mapping['g'] = next(c for c in 'abcdefg' if c not in list(mapping.values()))

    _mapping = dict()  # Fuck me
    for k, v in mapping.items():
        _mapping[v] = k

    mapping = _mapping

    n = ''
    for out in output:
        n += true_numbers[''.join(sorted([mapping[c] for c in out]))]
    n = int(n)
    res += n

print(res)




