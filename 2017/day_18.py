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
# Inefficient implementation but less error prone
# class Duet:
    # def __init__(self, program):
        # self.program = [inst for inst in program]
        # self.inst_pointer = 0
        # self.memory = defaultdict(lambda: 0)
        # self.played_sounds = list()
        # self.recovered_frequencies = list()

    # def get_value(self, x):
        # try:
            # return int(x)
        # except ValueError:
            # return self.memory[x]

    # def run(self):
        # while True:
            # inst = self.program[self.inst_pointer]
            # inst, ops = inst[0:3], inst[4:]

            # try:
                # x, y = ops.split()
                # xv, yv = self.get_value(x), self.get_value(y)
            # except ValueError:
                # x = ops
                # xv = self.get_value(x)

            # if inst == 'jgz':
                # if xv > 0:
                    # self.inst_pointer += yv
                # else:
                    # self.inst_pointer += 1
                # continue

            # if inst == 'snd':
                # self.played_sounds.append(xv)

            # elif inst == 'set':
                # self.memory[x] = yv

            # elif inst == 'add':
                # self.memory[x] += yv

            # elif inst == 'mul':
                # self.memory[x] *= yv

            # elif inst == 'mod':
                # self.memory[x] %= yv

            # elif inst == 'rcv':
                # self.recovered_frequencies.append(self.played_sounds[-1])
                # print(self.played_sounds[-1])
                # break

            # else:
                # raise ValueError("Unknown instruction")

            # self.inst_pointer += 1


# duet = Duet(lines)
# duet.run()


# PART 2
class Duet:
    def __init__(self, program):
        self.program = [inst for inst in program]
        self.inst_pointer = 0
        self.memory = defaultdict(lambda: 0)
        self.receiver = None
        self.receive_queue = deque()
        self.snd_called = 0
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

            if inst == 'snd':
                self.receiver.receive(xv)
                self.snd_called += 1

            elif inst == 'set':
                self.memory[x] = yv

            elif inst == 'add':
                self.memory[x] += yv

            elif inst == 'mul':
                self.memory[x] *= yv

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


d0, d1 = Duet(lines), Duet(lines)
d0.memory['p'] = 0
d1.memory['p'] = 1
d0.set_receiver(d1)
d1.set_receiver(d0)

while not d0.WAITING or d0.receive_queue or not d1.WAITING or d1.receive_queue:
    d0.run_until_waiting()
    d1.run_until_waiting()


print(d1.snd_called)














