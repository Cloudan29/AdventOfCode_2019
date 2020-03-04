class Output(Exception):
    def __init__(self, output):
        self.output = output

class Interrupt(Exception):
    pass

class Input(Exception):
    pass

class Machine:
    def __init__(self, code):
        # Creates an array of the code to be ran followed by a bunch of zeros as needed by the programming problems
        self.code = code + [0 for _ in range(100000)]
        # Instruction pointer and relative base are both instantiated to 0
        self.ip = 0
        self.rb = 0

    def run_machine(self, inputs):
        # Run forever (aka until something raises an exception)
        while True:
            # Grab the next instruction opcode
            opcode = self.code[self.ip] % 100
            # First look for the interrupt instruction
            if opcode == 99:
                raise Interrupt()
            
            # Set up the addressing modes for the parameters of the instruction
            address_mode1 = self.code[self.ip] // 100 % 10
            address_mode2 = self.code[self.ip] // 1000 % 10
            address_mode3 = self.code[self.ip] // 10000 % 10

            # Based on the addressing modes, figure out what the values will be
            if address_mode1 == 2:
                value1 = self.rb + self.code[self.ip+1]
            else:
                value1 = self.ip+1 if address_mode1 == 1 else self.code[self.ip+1]

            if address_mode2 == 2:
                value2 = self.rb + self.code[self.ip+2]
            else:
                value2 = self.ip+2 if address_mode2 == 1 else self.code[self.ip+2]

            if address_mode3 == 2:
                value3 = self.rb + self.code[self.ip+3]
            else:
                value3 = self.ip+3 if address_mode3 == 1 else self.code[self.ip+3]

            # Simple adder
            if opcode == 1:
                self.code[value3] = self.code[value1] + self.code[value2]
                self.ip+=4
            # Simple multiplier
            elif opcode == 2:
                self.code[value3] = self.code[value1] * self.code[value2]
                self.ip+=4
            # Input instruction, if there is no input, raise an exception. The main program should handle entering an input, and rerun the machine
            elif opcode == 3:
                if len(inputs) == 0:
                    raise Input()
                self.code[value1] = inputs.pop(0)
                self.ip+=2
            # Output instruction. Simply move the instruction pointer forward then raise an Output. The main program should handle this.
            elif opcode == 4:
                output_value = self.code[value1]
                self.ip+=2
                raise Output(output_value)
            # Jump if not zero instruction
            elif opcode == 5:
                if self.code[value1] != 0:
                    self.ip = self.code[value2]
                else:
                    self.ip+=3
            # Jump if zero instruction
            elif opcode == 6:
                if self.code[value1] == 0:
                    self.ip = self.code[value2]
                else:
                    self.ip+=3
            # Sets a flag at value3 if the first value is less than the second value
            elif opcode == 7:
                if self.code[value1] < self.code[value2]:
                    self.code[value3] = 1
                else:
                    self.code[value3] = 0
                self.ip+=4
            # Sets a flag at value3 if the first value is equal to the second value
            elif opcode == 8:
                if self.code[value1] == self.code[value2]:
                    self.code[value3] = 1
                else:
                    self.code[value3] = 0
                self.ip+=4
            # Changes the value of the relative base to be the instructions input value
            elif opcode == 9:
                self.rb += self.code[value1]
                self.ip+=2