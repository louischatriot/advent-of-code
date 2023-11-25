with open("inputs/day_6.data") as file:
    lines = [line.rstrip() for line in file]

signal = lines[0]

# Not optimal but small input so we don't care
def first_marker(signal, size = 4):
    for i in range(0, len(signal) + 1 - size):
        if len(signal[i:i+size]) == len(set(signal[i:i+size])):
            return i + size

    return -1


# Part 1
print(first_marker(signal, 4))

# Part 2
print(first_marker(signal, 14))





