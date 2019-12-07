import itertools
inp = open("inputs/day07.txt")
inp = [int(ins) for ins in inp.read().split(",")]

def part1():
    permutations = list(itertools.permutations(range(5)))
    output_signals = []
    for permutation in permutations:
        input_signals = [0]
        for phase in permutation:
            input_signals.append(run_machine(phase, input_signals[-1], [j for j in inp], False, 0)[0])

        output_signals.append(input_signals[-1])

    return max(output_signals)

def part2():
    permutations = list(itertools.permutations(range(5,10)))
    output_signals = []
    for permutation in permutations:
        machine_states = [[j for j in inp] for _ in range(5)]
        machine_starts = [0 for _ in range(5)]
        input_signals = [0]
        i = 0
        phase_flag = False
        while True:
            result = run_machine(permutation[i], input_signals[-1], machine_states[i], phase_flag, machine_starts[i])
            machine_starts[i] = result[2]
            input_signals.append(result[0])
            i = (i + 1) % 5
            if i == 0:
                phase_flag = True
            if result[1]:
                break

        output_signals.append(input_signals[-2])

    return max(output_signals)

def run_machine(phase_setting, input_signal, instruction_set, phase_flag, pointer_start):
    output_signal = 0
    j = 0 if not phase_flag else 1
    i = pointer_start
    while True:
        instruction = instruction_set[i]
        if instruction == 99:
            break
        parse_instruction = [int(str(instruction)[j]) for j in range(len(str(instruction))-1, -1, -1)]
        opcode = parse_instruction[0]
        address_modes = []
        for j in parse_instruction[2:]:
            address_modes.append(j)
        while len(address_modes) < 3:
            address_modes.append(0)

        value1 = i+1 if address_modes[0] == 1 else instruction_set[i+1]
        value2 = 0
        value3 = 0
        if opcode != 4:
            value2 = i+2 if address_modes[1] == 1 else instruction_set[i+2]
            value3 = i+3 if address_modes[2] == 1 else instruction_set[i+3]

        if opcode == 1:
            instruction_set[value3] = instruction_set[value1] + instruction_set[value2]
            i+=4
        elif opcode == 2:
            instruction_set[value3] = instruction_set[value1] * instruction_set[value2]
            i+=4
        elif opcode == 3:
            if j == 0:
                instruction_set[value1] = phase_setting
                j += 1
            elif j == 1:
                instruction_set[value1] = input_signal
            i+=2
        elif opcode == 4:
            output_signal = instruction_set[value1]
            i+=2
            return (output_signal, False, i)
        elif opcode == 5:
            if instruction_set[value1] != 0:
                i = instruction_set[value2]
            else:
                i+=3
        elif opcode == 6:
            if instruction_set[value1] == 0:
                i = instruction_set[value2]
            else:
                i+=3
        elif opcode == 7:
            if instruction_set[value1] < instruction_set[value2]:
                instruction_set[value3] = 1
            else:
                instruction_set[value3] = 0
            i+=4
        elif opcode == 8:
            if instruction_set[value1] == instruction_set[value2]:
                instruction_set[value3] = 1
            else:
                instruction_set[value3] = 0
            i+=4

    return (output_signal, True, i)


print (part1())
print (part2())