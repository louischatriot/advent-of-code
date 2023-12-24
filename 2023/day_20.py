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
# Wow that's actually a knitting job
class FlipFlop:
    def __init__(self, name, destinations, pulse_tracker, pulses_to_send):
        self.state = "off"
        self.name = name
        self.sources = []
        self.destinations = destinations
        self.pulse_tracker = pulse_tracker
        self.pulses_to_send = pulses_to_send
        self.reset_received()

    def reset_received(self):
        self.received = {0: 0, 1: 0}

    def add_source(self, source):
        self.sources.append(source)

    def receive_signal(self, signal, source):
        if signal == 0:
            if self.state == "on":
                self.send_signal(0)
                self.state = "off"

            else:
                self.send_signal(1)
                self.state = "on"

    def send_signal(self, signal):
        for d in self.destinations:
            self.pulse_tracker[signal] += 1
            self.received[signal] += 1
            self.pulses_to_send.append((d, signal, self.name))


class Conjunction:
    def __init__(self, name, destinations, pulse_tracker, pulses_to_send):
        self.name = name
        self.sources = []
        self.destinations = destinations
        self.pulse_tracker = pulse_tracker
        self.pulses_to_send = pulses_to_send
        self.reset_received()
        self.to_log = ''

    def reset_received(self):
        self.received = {0: 0, 1: 0}

    def add_source(self, source):
        self.sources.append(source)
        self.state = { s: 0 for s in self.sources }

    def receive_signal(self, signal, source):
        self.state[source] = signal
        if all(v == 1 for k, v in self.state.items()):
            self.send_signal(0)
        else:
            self.send_signal(1)

    def send_signal(self, signal):
        for d in self.destinations:
            if self.name in ['dl', 'vd', 'ns', 'bh']:
                if signal == 1:
                    print("BOOM <<<", self.name, self.to_log)

            self.received[signal] += 1
            self.pulse_tracker[signal] += 1
            self.pulses_to_send.append((d, signal, self.name))


class Broadcaster:
    def __init__(self, destinations, pulse_tracker, pulses_to_send):
        self.name = '<broadcaster>'
        self.destinations = destinations
        self.pulse_tracker = pulse_tracker
        self.pulses_to_send = pulses_to_send

    def receive_signal(self, signal, source):
        self.send_signal(signal)

    def send_signal(self, signal):
        for d in self.destinations:
            # print("Sending", signal, "from", self.name, "to", d)
            self.pulse_tracker[signal] += 1
            self.pulses_to_send.append((d, signal, self.name))


class NoOp:
    def __init__(self, name):
        self.name = name
        self.destinations = []
        self.reset_received()

    def add_source(self, source):
        pass

    def reset_received(self):
        self.received = {0: 0, 1: 0}

    def receive_signal(self, signal, source):
        self.received[signal] += 1
        # print("Received", signal)


modules = dict()
pulse_tracker = { 0: 0, 1: 0 }
pulses_to_send = list()

def reset_modules(modules, pulse_tracker):
    keys_to_delete = [k for k in modules]
    for k in keys_to_delete:
        del modules[k]

    pulse_tracker[0] = 0
    pulse_tracker[1] = 0

    for l in lines:
        name, destinations = l.split(' -> ')
        destinations = destinations.split(', ')
        if name != 'broadcaster':
            kind, name = name[0], name[1:]
        else:
            kind, name = '<broadcaster>', '<broadcaster>'

        if kind == '<broadcaster>':
            module = Broadcaster(destinations, pulse_tracker, pulses_to_send)

        elif kind == '%':
            module = FlipFlop(name, destinations, pulse_tracker, pulses_to_send)

        elif kind == '&':
            module = Conjunction(name, destinations, pulse_tracker, pulses_to_send)

        else:
            raise ValueError("Unexpected kind")

        modules[name] = module

    # Adding noops
    noops = []
    for name, module in modules.items():
        for dest_name in module.destinations:
            if dest_name not in modules:
                noops.append(dest_name)

    for dest_name in noops:
        dest = NoOp(dest_name)
        modules[dest_name] = dest

    # Adding sources
    for name, module in modules.items():
        for dest_name in module.destinations:
            modules[dest_name].add_source(name)


def press_button(pulse_tracker, pulses_to_send):
    pulse_tracker[0] += 1
    pulses_to_send.append(('<broadcaster>', 0, '<button>'))

    while len(pulses_to_send) > 0:
        pulse = pulses_to_send.pop(0)
        dest_name, signal, source_name = pulse
        modules[dest_name].receive_signal(signal, source_name)

reset_modules(modules, pulse_tracker)

vd = modules['vd']
ns = modules['ns']
bh = modules['bh']
dl = modules['dl']

R = 1000  # Set to 4000 to detect the first cycle of each 4 last inputs for part 2
for r in range(1, R):
    vd.to_log = r
    ns.to_log = r
    bh.to_log = r
    dl.to_log = r

    press_button(pulse_tracker, pulses_to_send)

res = pulse_tracker[0] * pulse_tracker[1]
print(res)


# PART 2
"""
By setting R to 4000 above we detect the 4 cycle lengths for the signals of the 4 inputs going into
rx through zh. lcm of those gives the result.
Note that this is a lucky case where (i) these cycles all start at 0 (otherwise it's a bit more of
a pain to calculate cf buses day 13 2020, and more importantly (ii) whenever one of these outputs
a 1 they don't output anything else during that button press otherwise that makes true cycle length
more combinatorial
"""
a = 3767
b = 3881
c = 3761
d = 3779

k = u.lcm(a, b)
k = u.lcm(k, c)
k = u.lcm(k, d)

print(k)

