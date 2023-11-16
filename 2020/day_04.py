import sys
import re

fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if len(sys.argv) > 1 else '') + '.data'
with open(fn) as file:
    lines = [line.rstrip() for line in file]

# PART 1
passports = []
current_passport = dict()

for l in lines:
    if l == '':
        passports.append(current_passport)
        current_passport = dict()
        continue

    data = l.split(' ')
    for d in data:
        k, v = d.split(':')
        current_passport[k] = v

if current_passport is not None:
    passports.append(current_passport)

needed_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
res = 0
for p in passports:
    if all(k in p.keys() for k in needed_keys):
        res += 1

print(res)


# PART 2
rhcl = re.compile('^#[0-9a-f]{6}$')
ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
rpid = re.compile('^[0-9]{9}$')
res = 0
for p in passports:
    if all(k in p.keys() for k in needed_keys):
        if not (1920 <= int(p['byr']) <= 2002):
            continue

        if not (2010 <= int(p['iyr']) <= 2020):
            continue

        if not (2020 <= int(p['eyr']) <= 2030):
            continue

        u = p['hgt'][-2:]
        h = int(p['hgt'][0:len(p['hgt'])-2])
        if u == 'cm' and not (150 <= h <= 193):
            continue

        if u == 'in' and not (59 <= h <= 76):
            continue

        if not rhcl.match(p['hcl']):
            continue

        if p['ecl'] not in ecl:
            continue

        if not rpid.match(p['pid']):
            continue

        res += 1

print(res)




