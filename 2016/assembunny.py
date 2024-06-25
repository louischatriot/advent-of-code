registers = ['a', 'b', 'c', 'd']

class Assembunny:
    def __init__(self, program):
        self.program = program
        self.memory = { reg: 0 for reg in registers }
        self.inst_pointer = 0

    def get_value(self, x):
        return self.memory[x] if x in registers else int(x)

    def set_value(self, x, v):
        self.memory[x] = v

    def run(self):
        while True:
            if self.inst_pointer >= len(self.program):
                break

            inst = self.program[self.inst_pointer]
            inst, operands = inst[0:3], inst[4:]

            if inst == 'inc':
                self.memory[operands] += 1
                self.inst_pointer += 1

            elif inst == 'dec':
                self.memory[operands] -= 1
                self.inst_pointer += 1

            elif inst == 'cpy':
                x, y = operands.split()
                self.memory[y] = self.get_value(x)
                self.inst_pointer += 1

            elif inst == 'jnz':
                x, y = operands.split()
                y = int(y)
                if self.get_value(x) != 0:
                    self.inst_pointer += y
                else:
                    self.inst_pointer += 1

            else:
                raise ValueError("Unknown instruction")






