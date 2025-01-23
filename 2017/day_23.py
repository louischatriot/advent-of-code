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
class Duet:
    def __init__(self, program):
        self.program = [inst for inst in program]
        self.inst_pointer = 0
        self.memory = defaultdict(lambda: 0)
        self.receiver = None
        self.receive_queue = deque()
        self.snd_called = 0
        self.mul_called = 0
        self.WAITING = False

    def get_value(self, x):
        try:
            return int(x)
        except ValueError:
            return self.memory[x]

    def set_receiver(self, receiver):
        self.receiver = receiver

    def receive(self, v):
        self.receive_queue.append(v)

    def run_until_waiting(self):
        self.WAITING = False
        while True:
            if self.inst_pointer >= len(self.program):
                break

            inst = self.program[self.inst_pointer]
            inst, ops = inst[0:3], inst[4:]

            try:
                x, y = ops.split()
                xv, yv = self.get_value(x), self.get_value(y)
            except ValueError:
                x = ops
                xv = self.get_value(x)

            if inst == 'jgz':
                if xv > 0:
                    self.inst_pointer += yv
                else:
                    self.inst_pointer += 1
                continue

            if inst == 'jnz':
                if xv != 0:
                    self.inst_pointer += yv
                else:
                    self.inst_pointer += 1
                continue

            if inst == 'snd':
                self.receiver.receive(xv)
                self.snd_called += 1

            elif inst == 'set':
                self.memory[x] = yv

            elif inst == 'add':
                self.memory[x] += yv

            elif inst == 'sub':
                self.memory[x] -= yv

            elif inst == 'mul':
                self.memory[x] *= yv
                self.mul_called += 1

            elif inst == 'mod':
                self.memory[x] %= yv

            elif inst == 'rcv':
                if not self.receive_queue:
                    self.WAITING = True
                    break

                self.memory[x] = self.receive_queue.popleft()

            else:
                raise ValueError("Unknown instruction")

            self.inst_pointer += 1


duet = Duet(lines)
duet.run_until_waiting()
print(duet.mul_called)


# PART 2
# The code basically tries to divide every number between A and B, spaced by delta C, by every number
# h is increased whenever one of these divisions is integer i.e. the number has a divisor, i.e. it is not prime
primes = u.primes_until_n(1000000)
primes = { p: True for p in primes }

res = 0
A = 108400
B = 125400
D = 17

for n in range(A, B+1, D):
    if n not in primes:
        res += 1

print(res)



