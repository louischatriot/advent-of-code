from time import time

with open("inputs/day_21.data") as file:
    lines = [line.rstrip() for line in file]

monkeys = dict()

for line in lines:
    name, res = line.split(': ')

    try:
        res = int(res)
        monkeys[name] = res
    except:
        for operation in ['+', '-', '*', '/']:
            if operation in res:
                op1, op2 = res.split(' ' + operation + ' ')
                monkeys[name] = [operation, op1, op2]



def evaluate(monkeys, node):
    if type(monkeys[node]) is int:
        return monkeys[node]

    operation, op1, op2 = monkeys[node]

    if operation == '+':
        return evaluate(monkeys, op1) + evaluate(monkeys, op2)

    if operation == '-':
        return evaluate(monkeys, op1) - evaluate(monkeys, op2)

    if operation == '*':
        return evaluate(monkeys, op1) * evaluate(monkeys, op2)

    if operation == '/':
        return evaluate(monkeys, op1) / evaluate(monkeys, op2)


# Part 1
res = evaluate(monkeys, 'root')
print("PART 1:", int(res))


# Part 2
_, res1, res2 = monkeys['root']

# Boundaries for dichotomy found empirically
# Good thing the function is monotonous and the target does not move oO
low = 1999000000000
high = 3999000000000

monkeys['humn'] = low
monkeys['humn'] = high

target = evaluate(monkeys, res2)

while True:
    test = (low + high) // 2
    monkeys['humn'] = test

    res = evaluate(monkeys, res1) - target

    if res == 0:
        print("PART 2:", test)
        break

    if res > 0:
        low = test
    else:
        high = test



