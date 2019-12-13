from intcode import *
inp = [int(ins) for ins in open("inputs/day13.txt").read().split(",")]

def part1():
    machine = Machine([j for j in inp])
    start_game_state = {0: [], 1: [], 2: [], 3: [], 4: []}
    # empty, wall, block, horizontal paddle, ball
    output_sequence = 0
    x = 0
    y = 0

    while True:
        try:
            machine.run_machine([])
        except Output as e:
            if output_sequence == 0:
                x = e.output
            elif output_sequence == 1:
                y = e.output
            else:
                start_game_state[e.output].append((x, y))
                x = 0
                y = 0
            output_sequence = (output_sequence + 1) % 3
        except Interrupt:
            break
    
    return len(start_game_state[2])

def part2():
    machine = Machine([j for j in inp])
    stuff_in_game = {0: [], 1: [], 2: [], 3: [], 4: []}
    machine.code[0] = 2
    output_sequence = 0
    player_move = []
    score = 0
    x = 0
    y = 0

    while True:
        try:
            machine.run_machine(player_move)
        except Output as e:
            if output_sequence == 0:
                x = e.output
            elif output_sequence == 1:
                y = e.output
            else:
                if x == -1 and y == 0:
                    score = e.output
                else:
                    stuff_in_game[e.output].append((x, y))
                x = 0
                y = 0
            output_sequence = (output_sequence + 1) % 3
        except Input:
            decision = 0
            if stuff_in_game[3][0][0] < stuff_in_game[4][0][0]:
                decision = 1
            elif stuff_in_game[3][0][0] > stuff_in_game[4][0][0]:
                decision = -1
            player_move.append(decision)
        except Interrupt:
            break

    return score
  
print (part1())
print (part2())