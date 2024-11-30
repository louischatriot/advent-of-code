registers = ['a', 'b', 'c', 'd']

class Assembunny:
    def __init__(self, program):
        self.program = [l for l in program]
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

            # print(self.inst_pointer, self.program, self.memory)

            if inst == 'inc':
                self.memory[operands] += 1
                self.inst_pointer += 1

            elif inst == 'dec':
                self.memory[operands] -= 1
                self.inst_pointer += 1

            elif inst == 'cpy':
                x, y = operands.split()

                if y in registers:  # Can be made illegal by tgl, in that case skip
                    self.memory[y] = self.get_value(x)

                self.inst_pointer += 1

            elif inst == 'jnz':
                x, y = operands.split()
                y = self.get_value(y)
                if self.get_value(x) != 0:
                    self.inst_pointer += y
                else:
                    self.inst_pointer += 1

            elif inst == 'tgl':
                x = operands
                offset = self.get_value(x)

                if self.inst_pointer + offset < len(self.program):
                    taddress = self.inst_pointer + offset
                    tinst = self.program[taddress]
                    tinst, toperands = tinst[0:3], tinst[4:]

                    if tinst == 'inc':
                        self.program[taddress] = f"dec {toperands}"
                    elif tinst in ['dec', 'tgl']:
                        self.program[taddress] = f"inc {toperands}"
                    elif tinst == 'jnz':
                        self.program[taddress] = f"cpy {toperands}"
                    elif tinst == 'cpy':
                        self.program[taddress] = f"jnz {toperands}"
                    else:
                        raise ValueError("Unexpected instruction, can't toggle")

                self.inst_pointer += 1




            else:
                raise ValueError("Unknown instruction")






