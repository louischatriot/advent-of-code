registers = ['a', 'b', 'c', 'd']

class Assembunny:
    def __init__(self, program, out = None, post_loop_func = None):
        self.program = [l for l in program]
        self.memory = { reg: 0 for reg in registers }
        self.out = out
        self.inst_pointer = 0
        self.post_loop_func = post_loop_func  # A function to run after each loop
        self.executed_instructions = 0

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

            elif inst == 'out':
                v = self.memory[operands]
                if self.out is None:
                    print(v)
                else:
                    self.out.append(v)
                    if len(self.out) >= 15:
                        break
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

            elif inst == 'fun':  # To speed up day 23 part 2
                a, b, c, d = self.memory['a'], self.memory['b'], self.memory['c'], self.memory['d']
                self.memory['a'] = a * b
                self.memory['b'] = b - 1
                self.memory['c'] = 2 * (b - 1)
                self.memory['d'] = 0

                self.inst_pointer += 1


            else:
                raise ValueError("Unknown instruction")

            self.executed_instructions += 1

            if self.post_loop_func:
                self.post_loop_func(self)






