import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import numpy as np

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
class FlipFlop:
    def __init__(self, name, pulse_tracker, modules, input, output, pulses_to_send):
        self.state = "off"
        self.pulse_tracker = pulse_tracker
        self.input = input
        self.output = output
        self.modules = modules
        self.name = name
        self.pulses_to_send = pulses_to_send

    def receive_signal(self, signal, _from):
        if signal == 0:
            if self.state == "on":
                self.send_signal(0)
                self.state = "off"

            else:
                self.send_signal(1)
                self.state = "on"

    def send_signal(self, signal):
        self.pulse_tracker[signal] += 1
        self.pulses_to_send.append((self.output, signal, self.name))


class Conjunction:
    def __init__(self, name, pulse_tracker, modules, inputs, output, pulses_to_send):
        self.state = { c: 0 for c in inputs }
        self.pulse_tracker = pulse_tracker
        self.inputs = inputs
        self.output = output
        self.modules = modules
        self.name = name
        self.pulses_to_send = pulses_to_send

    def receive_signal(self, signal, _from):
        self.state[_from] = signal
        if all(v == 1 for k, v in self.state.items()):
            self.send_signal(0)
        else:
            self.send_signal(1)

    def send_signal(self, signal):
        self.pulse_tracker[signal] += 1
        self.pulses_to_send.append((self.output, signal, self.name))





