class Computer:

    def parse_input(lines):
        reg = dict()
        program = None

        for line in lines:
            if line == '':
                program = True
                continue

            line = line.split()

            if program is None:
                reg[line[1][0:-1].lower()] = int(line[2])

            if program is True:
                program = list(map(int, line[1].split(',')))

        return program, reg


    def __init__(self, program, registers = None):
        self.registers = { 'a': 0, 'b': 0, 'c': 0 }
        self.program = [inst for inst in program]
        self.inst_pointer = 0

        if registers:
            for r in self.registers.keys():
                if r in registers.keys():
                    self.registers[r] = registers[r]

        self.stdout = list()


    def get_combo_value(self, operand):
        if 0 <= operand <= 3:
            return operand

        for v, reg in [(4, 'a'), (5, 'b'), (6, 'c')]:
            if operand == v:
                return self.registers[reg]

        raise ValueError("Unexpected combo operand", operand)


    def execute_instruction(self):
        opcode = self.program[self.inst_pointer]
        operand = self.program[self.inst_pointer + 1]

        if opcode == 3:  # jnz
            if self.registers['a'] == 0:
                self.inst_pointer += 2
            else:
                self.inst_pointer = operand

            return

        if opcode == 0:  # adv
            self.registers['a'] = self.registers['a'] // (2 ** self.get_combo_value(operand))

        elif opcode == 1:  # bxl
            self.registers['b'] = self.registers['b'] ^ operand

        elif opcode == 2:  # bst
            self.registers['b'] = self.get_combo_value(operand) % 8

        elif opcode == 4:  # bxc
            self.registers['b'] = self.registers['b'] ^ self.registers['c']

        elif opcode == 5:  # out
            self.stdout.append(self.get_combo_value(operand) % 8)

        elif opcode == 6:  # bdv
            self.registers['b'] = self.registers['a'] // (2 ** self.get_combo_value(operand))

        elif opcode == 7:  # cdv
            self.registers['c'] = self.registers['a'] // (2 ** self.get_combo_value(operand))
        else:
            raise ValueError("Unknown opcode", opcode)

        self.inst_pointer += 2  # Except jnz we always increment instruction pointer by 2


    def run(self):
        while self.inst_pointer < len(self.program):
            self.execute_instruction()










