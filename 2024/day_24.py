import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import collections
import os

is_example = (len(sys.argv) > 1)
fn = os.getcwd() + '/inputs/' + os.path.basename(__file__).replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
PART_1 = False
WORD_SIZE = 45 if not is_example else 5


def get_initial_state():
    wires = dict()
    gates = None
    gates_by_in = defaultdict(lambda: list())

    for line in lines:
        if line == '':
            gates = list()
            continue

        if gates is None:
            wire, signal = line.split(': ')
            wires[wire] = int(signal)
        else:
            inp, out = line.split(' -> ')
            a, op, b = inp.split(' ')
            gate = [a, b, op, out]
            gates.append(gate)
            gates_by_in[a].append(gate)
            gates_by_in[b].append(gate)


    return wires, gates, gates_by_in


def simulate(wires, gates_by_in):
    to_explore = collections.deque()
    for wire in wires:
        for gate in gates_by_in[wire]:
            to_explore.append(gate)

    while to_explore:
        gate = to_explore.popleft()
        a, b, op, out = gate

        if a in wires and b in wires:
            av, bv = wires[a], wires[b]
            wires[out] = av & bv if op == 'AND' else (av ^ bv if op == 'XOR' else av | bv)
            for g in gates_by_in[out]:
                to_explore.append(g)


def get_value(wires, signal):
    bound = WORD_SIZE + 1 if signal == 'z' else WORD_SIZE
    bound = 100 if PART_1 else bound
    s = ''
    for n in range(bound):
        z = f"{signal}{n:02}"
        if z not in wires:
            if PART_1:
                break
            else:
                raise ValueError(f"Wire {z} not set")
        s = str(wires[z]) + s

    res = int(s, 2)
    return res


def set_value(wires, signal, value):
    bound = WORD_SIZE + 1 if signal == 'z' else WORD_SIZE
    bound = 100 if PART_1 else bound
    s = bin(value)[2:]
    s = '0' * (bound - len(s)) + s

    for n, c in enumerate(reversed(s)):
        z = f"{signal}{n:02}"
        if z not in wires:
            if PART_1:
                wires[z] = 0
                continue
            else:
                raise ValueError("Wire not part of initial state")
        wires[z] = int(c)


wires, gates, gates_by_in = get_initial_state()
simulate(wires, gates_by_in)
res = get_value(wires, 'z')
print(res)


# PART 2

for n in range(45):
    the_wire = f"x{n:02}"

    wires, gates, gates_by_in = get_initial_state()

    set_value(wires, 'x', 0)
    set_value(wires, 'y', 0)
    wires[the_wire] = 1

    simulate(wires, gates_by_in)

    x = get_value(wires, 'x')
    y = get_value(wires, 'y')
    z = get_value(wires, 'z')

    if x+y != z:
        print(the_wire)


def get_bad_gate_pairs_from(the_wire):
    wires, gates, gates_by_in = get_initial_state()

    # Get all gates where a swap could have occured
    to_explore = collections.deque()
    for gate in gates_by_in[the_wire]:
        to_explore.append(gate)

    swappable = list()

    while to_explore:
        gate = to_explore.popleft()
        a, b, op, out = gate
        swappable.append(gate)

        for gate in gates_by_in[out]:
            to_explore.append(gate)

    res = set()

    # Test all possibilities
    for g1, g2 in itertools.combinations(swappable, 2):
        g1out, g2out = g1[3], g2[3]
        g1[3] = g2out
        g2[3] = g1out

        set_value(wires, 'x', 0)
        set_value(wires, 'y', 0)
        wires[the_wire] = 1

        simulate(wires, gates_by_in)

        x = get_value(wires, 'x')
        y = get_value(wires, 'y')
        z = get_value(wires, 'z')

        if x+y == z:
            res.add(tuple(sorted([g1out, g2out])))

        # Clean up gates outs and wires state
        wires = { k: v for k,v in __wires.items() }
        g1[3] = g1out
        g2[3] = g2out

    return res


# Cached from calling the above function on all n where addition doesn't work
pairs = dict()

pairs['x12'] = {('nqs', 'z13'), ('fgc', 'fsf'), ('z12', 'z13'), ('fgc', 'z12'), ('nqs', 'qts'), ('fsf', 'z13'), ('fgc', 'nqs')}
pairs['x29'] = {('gdv', 'z29'), ('z29', 'z30'), ('mtj', 'z29')}
pairs['x33'] = {('dgr', 'vvm'), ('vvm', 'z33'), ('z33', 'z34'), ('wrd', 'z33')}
pairs['x37'] = {('bkj', 'z37'), ('dtv', 'z37'), ('z37', 'z38'), ('jkb', 'z37')}


# Need to find more tests cases to narrow it down do one candidate
res = list()
testsx = [12, 29, 33, 37, 1235575543, 213124578, 2**44-1, 2**30+33333, 111111111, 2**44]
testsy = [29, 33, 37, 1235575543, 213124578, 12, 2**12+5, 2**44-123, 222222222, 2**44]

for p1 in pairs['x12']:
    for p2 in pairs['x29']:
        for p3 in pairs['x33']:
            for p4 in pairs['x37']:
                candidate = [p1, p2, p3, p4]

                ok = True
                for tx, ty in zip(testsx, testsy):
                    # Create fresh copy
                    wires, gates, gates_by_in = get_initial_state()
                    gates_by_out = { gate[3]: gate for gate in gates }

                    # Swap
                    for g1out, g2out in candidate:
                        g1, g2 = gates_by_out[g1out], gates_by_out[g2out]
                        g1[3] = g2out
                        g2[3] = g1out

                    set_value(wires, 'x', tx)
                    set_value(wires, 'y', ty)

                    simulate(wires, gates_by_in)

                    x = get_value(wires, 'x')
                    y = get_value(wires, 'y')
                    z = get_value(wires, 'z')

                    if x+y != z:
                        ok = False


                if ok:
                    res.append(candidate)



print(len(res))



for candidate in res:
    s = list()
    for c1, c2 in candidate:
        s.append(c1)
        s.append(c2)

    s = ','.join(sorted(s))

    print(s)

