from intcode import Machine, Interrupt
inp = [int(ins) for ins in open("inputs/day02.txt").read().split(",")]

def part1(noun, verb):
    machine = Machine([j for j in inp])
    machine.code[1] = noun
    machine.code[2] = verb
    try:
        machine.run_machine([])
    except Interrupt:
        pass
        
    return machine.code[0]

def part2(target):
    for noun in range(100):
        for verb in range(100):
            if part1(noun, verb) == target:
                return 100 * noun + verb
        
    return -1

print (part1(12, 2))
print (part2(19690720))