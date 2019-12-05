inp = open("inputs/day02.txt")
arr = inp.read().split(",")

def part1(noun, verb):
    codes = [int(a) for a in arr]
    codes[1] = noun
    codes[2] = verb

    for i in range(0,len(codes),4):
        opcode = codes[i]
        oper1 = codes[i+1]
        oper2 = codes[i+2]
        oper3 = codes[i+3]
        if opcode == 99:
            break
        elif opcode == 1:
            codes[oper3] = codes[oper1] + codes[oper2]
        elif opcode == 2:
            codes[oper3] = codes[oper1] * codes[oper2]
        
    return codes[0]

def part2(target):
    for noun in range(100):
        for verb in range(100):
            if part1(noun, verb) == target:
                return 100 * noun + verb
        
    return -1

print (part1(12, 2))
print (part2(19690720))