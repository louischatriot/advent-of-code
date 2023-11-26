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


# If final it's a hex, otherwise it's a raw binary from recursion
def parse_packet(hex, final=True):

    # print("NEW PARSE", hex)

    if final:
        binary = ''.join([u.hex_to_binary[c] for c in hex])
    else:
        binary = hex

    # print("NEW PARSE", binary)

    version, type_id, contents = binary[0:3], binary[3:6], binary[6:]
    version, type_id = int(version, 2), int(type_id, 2)


    # print("NEW PARSE", version, type_id, contents)

    packet = None

    if type_id == 4:  # Literal value
        # print("===== LITERAL", contents)

        res = ''

        done = False
        while not done:
            section, contents = contents[0:5], contents[5:]
            res += section[1:]

            if section[0] == '0':
                done = True

        res = int(res, 2)
        packet = [version, type_id, res]


    else:  # Operator
        length_type_id, contents = contents[0], contents[1:]

        if length_type_id == '0':

            length, contents = contents[0:15], contents[15:]
            length = int(length, 2)
            packet_contents, contents = contents[0:length], contents[length:]

            # print("===== TYPE 0 ---", length, packet_contents, contents)

            packets = []
            while len(packet_contents) > 0:
                packet, packet_contents = parse_packet(packet_contents, False)
                packets.append(packet)

        else:

            length, contents = contents[0:11], contents[11:]
            length = int(length, 2)

            # print("===== TYPE 1 ---", length, contents)

            packets = []
            while len(packets) < length:
                packet, contents = parse_packet(contents, False)
                packets.append(packet)

        packet = [version, type_id, packets]


    # print("DONE", packet)

    if final:
        return packet
    else:
        return packet, contents


def get_version_sum(packet):

    if type(packet[2]) == int:
        return packet[0]

    return packet[0] + sum([get_version_sum(p) for p in packet[2]])


def get_value(packet):
    if packet[1] == 4:
        return packet[2]

    if packet[1] == 0:
        return sum([get_value(p) for p in packet[2]])

    if packet[1] == 1:
        return math.prod([get_value(p) for p in packet[2]])

    if packet[1] == 2:
        return min([get_value(p) for p in packet[2]])

    if packet[1] == 3:
        return max([get_value(p) for p in packet[2]])

    if packet[1] == 5:
        return 1 if get_value(packet[2][0]) > get_value(packet[2][1]) else 0

    if packet[1] == 6:
        return 1 if get_value(packet[2][0]) < get_value(packet[2][1]) else 0

    if packet[1] == 7:
        return 1 if get_value(packet[2][0]) == get_value(packet[2][1]) else 0



for l in lines:
    packet = parse_packet(l)
    s = get_version_sum(packet)
    v = get_value(packet)
    print(s)
    print(v)




