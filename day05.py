inp = open("inputs/day05.txt")
inp = [int(ins) for ins in inp.read().split(",")]

def run_machine(value):
    instructions = [j for j in inp]
    i = 0
    while True:
        instruction = instructions[i]
        if instruction == 99:
            break
        parse_instruction = [int(str(instruction)[j]) for j in range(len(str(instruction))-1, -1, -1)]
        opcode = parse_instruction[0]
        address_modes = []
        for j in parse_instruction[2:]:
            address_modes.append(j)
        while len(address_modes) < 3:
            address_modes.append(0)

        value1 = i+1 if address_modes[0] == 1 else instructions[i+1]
        value2 = i+2 if address_modes[1] == 1 else instructions[i+2]
        value3 = i+3 if address_modes[2] == 1 else instructions[i+3]

        if opcode == 1:
            instructions[value3] = instructions[value1] + instructions[value2]
            i+=4
        elif opcode == 2:
            instructions[value3] = instructions[value1] * instructions[value2]
            i+=4
        elif opcode == 3:
            instructions[value1] = value
            i+=2
        elif opcode == 4:
            print (instructions[value1])
            i+=2
        elif opcode == 5:
            if instructions[value1] != 0:
                i = instructions[value2]
            else:
                i+=3
        elif opcode == 6:
            if instructions[value1] == 0:
                i = instructions[value2]
            else:
                i+=3
        elif opcode == 7:
            if instructions[value1] < instructions[value2]:
                instructions[value3] = 1
            else:
                instructions[value3] = 0
            i+=4
        elif opcode == 8:
            if instructions[value1] == instructions[value2]:
                instructions[value3] = 1
            else:
                instructions[value3] = 0
            i+=4

run_machine(1)
run_machine(5)