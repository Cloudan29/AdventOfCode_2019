from intcode import *
inp = [int(ins) for ins in open("inputs/day09.txt").read().split(",")]

def part1():
    machine = Machine([j for j in inp])
    while True:
        try:
            machine.run_machine([1])
        except Output as e:
            print (e.output)
        except Interrupt:
            break

def part2():
    machine = Machine([j for j in inp])
    while True:
        try:
            machine.run_machine([2])
        except Output as e:
            print (e.output)
        except Interrupt:
            break

part1()
part2()