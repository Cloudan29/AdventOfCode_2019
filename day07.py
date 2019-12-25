import itertools
from intcode import Machine, Output, Interrupt

inp = [int(ins) for ins in open("inputs/day07.txt").read().split(",")]

def part1():
    permutations = list(itertools.permutations(range(5)))
    output_signals = []
    for permutation in permutations:
        next_signal = 0
        for phase in permutation:
            while True:
                try:
                    machine = Machine([j for j in inp])
                    machine.run_machine([phase, next_signal])
                except Output as e:
                    next_signal = e.output
                    break
            
        output_signals.append(next_signal)

    return max(output_signals)

def part2():
    permutations = list(itertools.permutations(range(5,10)))
    output_signals = []
    for permutation in permutations:
        machines = [Machine([j for j in inp]) for _ in range(5)]
        next_signal = 0
        i = 0
        phase_flag = False
        while True:
            try:
                if not phase_flag:
                    machines[i].run_machine([permutation[i],next_signal])
                else:
                    machines[i].run_machine([next_signal])
            except Output as e:
                next_signal = e.output
            except Interrupt:
                break

            i = (i + 1) % 5
            if i == 0:
                phase_flag = True

        output_signals.append(next_signal)

    return max(output_signals)

print (part1())
print (part2())