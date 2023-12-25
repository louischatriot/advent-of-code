import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import numpy as np
import random

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]




# Shamelessly taken from https://stackoverflow.com/questions/15993447/python-data-structure-for-efficient-add-remove-and-random-choice
class ListDict(object):
    def __init__(self):
        self.item_to_position = {}
        self.items = []

    def __contains__(self, item):
        return item in self.item_to_position

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return "LISTDICT => " + ', '.join(map(str, self.items))

    def add_item(self, item):
        if item in self.item_to_position:
            return
        self.items.append(item)
        self.item_to_position[item] = len(self.items)-1

    def remove_item(self, item):
        position = self.item_to_position.pop(item)
        last_item = self.items.pop()
        if position != len(self.items):
            self.items[position] = last_item
            self.item_to_position[last_item] = position

    def choose_random_item(self):
        return random.choice(self.items)






# PART 1
def parse_input():
    nodes = set()
    edges = ListDict()

    for l in lines:
        a, bs = l.split(': ')
        nodes.add(a)

        for b in bs.split(' '):
            nodes.add(b)
            edges.add_item((a, b))

    return (nodes, edges)


def find_one_cut():
    nodes, edges = parse_input()

    while len(nodes) > 2:
        a, b = edges.choose_random_item()
        new_node = f"{a}+{b}"

        nodes.remove(a)
        nodes.remove(b)
        nodes.add(new_node)

        # TODO: should find a more efficient data structure here (but well this works not too bad already)
        to_remove = list()
        to_add = list()
        for edge in edges:
            if a in edge and b in edge:
                to_remove.append(edge)

            elif a in edge or b in edge:
                to_remove.append(edge)
                edge_as_list = list(edge)
                to_add.append(edge_as_list[1] if edge_as_list[0] in [a, b] else edge_as_list[0])

        for edge in to_remove:
            edges.remove_item(edge)

        for vertice in to_add:
            edges.add_item((vertice, new_node))


    comp1, comp2 = nodes
    comp1, comp2 = set(comp1.split('+')), set(comp2.split('+'))

    nodes, edges = parse_input()

    cutting_edges = 0
    for a, b in edges:
        if (a in comp1 and b in comp2) or (a in comp2 and b in comp1):
            cutting_edges += 1

    # Keep searching at random until you find the three-cut
    if cutting_edges == 3:
        return len(comp1) * len(comp2)
    else:
        return find_one_cut()


res = find_one_cut()
print(res)



