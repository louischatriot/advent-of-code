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
rules = dict()
messages = []
on_messages = False
for l in lines:
    if on_messages:
        messages.append(l)
    else:
        if l == '':
            on_messages = True
        else:
            t, contents = l.split(': ')
            rules[t] = contents

def create_re(rules, start):
    r = rules[start]

    if r[0] == '"':
        return r[1]

    # Ha ha so dirty but oh well
    if start == '8' and '|' in r:
        return '(' + create_re(rules, '42') + ')+'

    if start == '11' and '|' in r:
        k = create_re(rules, '42')
        t = create_re(rules, '31')
        # I know no shame - but I should look up if a regexp can ask for two patterns the same number of times
        return f"({k}{t}|{k}{k}{t}{t}|{k}{k}{k}{t}{t}{t}|{k}{k}{k}{k}{t}{t}{t}{t})"

    if '|' not in r:
        res = ''
        for t in r.split(' '):
            res += create_re(rules, t)
        return res

    if '|' in r:
        a, b = r.split(' | ')
        res = '('
        for t in a.split(' '):
            res += create_re(rules, t)
        res += '|'
        for t in b.split(' '):
            res += create_re(rules, t)
        res += ')'
        return res

regexp = '^' + create_re(rules, '0') + '$'

the_re = re.compile(regexp)

res = 0
for msg in messages:
    if the_re.match(msg):
        # print(msg)
        res += 1

print(res)


# PART 2
rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'

regexp = '^' + create_re(rules, '0') + '$'

the_re = re.compile(regexp)

res = 0
for msg in messages:
    if the_re.match(msg):
        print(msg)
        res += 1

print(res)



