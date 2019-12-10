from intcode import *
inp = open("inputs/day05.txt").read().split(",")

def part1():
    machine = Machine([int(instr) for instr in inp])
    interrupt = False
    while not interrupt:
        try:
            machine.run_machine([1])
        except Output as e:
            print (e.output)
        except Interrupt:
            interrupt = True

def part2():
    machine = Machine([int(instr) for instr in inp])
    interrupt = False
    while not interrupt:
        try:
            machine.run_machine([5])
        except Output as e:
            print (e.output)
        except Interrupt:
            interrupt = True

part1()
part2()