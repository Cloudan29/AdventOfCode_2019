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
    score = 0
    player_move = []
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
                    if e.output == 0:
                        if (x,y) in stuff_in_game[1]:
                            stuff_in_game[1].remove((x,y))
                        if (x,y) in stuff_in_game[2]:
                            stuff_in_game[2].remove((x,y))
                        if (x,y) in stuff_in_game[3]:
                            stuff_in_game[3].remove((x,y))
                        if (x,y) in stuff_in_game[4]:
                            stuff_in_game[4].remove((x,y))

                    stuff_in_game[e.output].append((x, y))
                x = 0
                y = 0
            output_sequence = (output_sequence + 1) % 3
        except Input:
            # If you wanna see the game:
            # display_game(stuff_in_game)
            decision = 0
            if stuff_in_game[3][0][0] < stuff_in_game[4][0][0]:
                decision = 1
            elif stuff_in_game[3][0][0] > stuff_in_game[4][0][0]:
                decision = -1
            player_move.append(decision)
        except Interrupt:
            break

    return score

def display_game(stuff_in_game):
    minx, maxx, miny, maxy = 0, 0, 0, 0
    for things in stuff_in_game:
        for thing in stuff_in_game[things]:
            if thing[0] > maxx:
                maxx = thing[0]
            if thing[0] < minx:
                minx = thing[0]
            if thing[1] > maxy:
                maxy = thing[1]
            if thing[1] < miny:
                miny = thing[1]

    board = [[' ' for _ in range(maxx - minx + 1)] for _ in range(maxy - miny + 1)]
    for things in stuff_in_game:
        to_display = ''
        if things == 0:
            to_display = ' '
        elif things == 1:
            to_display = 'W'
        elif things == 2:
            to_display = 'B'
        elif things == 3:
            to_display = 'P'
        elif things == 4:
            to_display = 'O'
        for thing in stuff_in_game[things]:
            board[thing[1]-miny][thing[0]-minx] = to_display

    for row in board:
        print(''.join(row))

    
print (part1())
print (part2())