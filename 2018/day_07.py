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
dependencies = defaultdict(lambda: set())
todo = set()
for line in lines:
    b, e = line[5], line[36]
    todo.add(b)
    todo.add(e)
    dependencies[e].add(b)


order = list()

while todo:
    doable = list()

    for step in todo:
        if len(dependencies[step]) == 0:
            doable.append(step)

    step = min(doable)
    order.append(step)

    for a in dependencies:
        if step in dependencies[a]:
            dependencies[a].remove(step)

    todo.remove(step)


res = ''.join(order)
print(res)


# PART 2
dependencies = defaultdict(lambda: set())
todo = set()
for line in lines:
    b, e = line[5], line[36]
    todo.add(b)
    todo.add(e)
    dependencies[e].add(b)


DELAY = 0 if is_example else 60
NWORKERS = 2 if is_example else 5

# So actually we were not supposed to find the optimal, just follow the alphabetical rule ...
# def dfs(done, doing1, doing2, rem1, rem2):
    # if len(todo) == len(done):
        # return 0

    # if rem2 < rem1:
        # return dfs(done, doing2, doing1, rem2, rem1)

    # # Here rem1 <= rem2

    # if rem1 > 0:
        # __done = { s for s in done }
        # __done.add(doing1)

        # if rem2 == rem1:
            # __done.add(doing2)
            # doing2 = None

        # return rem1 + dfs(__done, None, doing2, 0, rem2 - rem1)

    # # Here rem1 is 0 and rem2 is >= 0 ; even if both are 0 we can attribute a task to w1 only and still be optimal

    # # done = { 'C', 'A', 'F', 'D', 'B' }

    # doable = list()
    # for step in todo:
        # if step in done:
            # continue

        # if step == doing2:
            # continue

        # if len(dependencies[step].difference(done)) == 0:
            # doable.append(step)

    # if len(doable) == 0:  # Need to wait for worker 2
        # __done = { s for s in done }
        # __done.add(doing2)

        # return rem2 + dfs(__done, None, None, 0, 0)

    # else:
        # best = float("inf")

        # for step in doable:
            # candidate = dfs(done, step, doing2, ord(step) - ord('A') + 1 + DELAY, rem2)
            # best = min(best, candidate)

        # return best


# res = dfs(set(), None, None, 0, 0)
# print(res)


done = set()
workers = list()
res = 0
while len(done) < len(todo):
    doable = list()
    for step in todo:
        if step in done:
            continue

        if any(step == s for _, s in workers):
            continue

        if len(dependencies[step].difference(done)) == 0:
            doable.append(step)

    if len(doable) > 0 and len(workers) <= NWORKERS:
        for step, _ in zip(sorted(doable), range(NWORKERS - len(workers))):
            workers.append((ord(step) - ord('A') + 1 + DELAY, step))

    # Now all workers that can work are busy

    workers = sorted(workers)
    to_finish, workers = workers[0], workers[1:]
    t, step = to_finish
    res += t
    done.add(step)
    workers = [(_t - t, _step) for _t, _step in workers]




print(res)



