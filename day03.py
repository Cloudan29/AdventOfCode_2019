A,B = open("inputs/day03.txt").read().split("\n")
A,B = [instructions.split(",") for instructions in [A,B]]
dirs = {"R": (1,0), "L": (-1,0), "U": (0,1), "D": (0,-1)}

def points(arr):
    x = y = 0
    ans = {}
    length = 0
    for ins in arr:
        dir, amnt = ins[0], int(ins[1:])
        for _ in range(amnt):
            length += 1
            x += dirs[dir][0]
            y += dirs[dir][1]
            if (x,y) not in ans:
                ans[(x,y)] = length

    return ans

PA = points(A)
PB = points(B)
crosses = PA.keys()&PB.keys()

def part1():
    return min([abs(x) + abs(y) for (x,y) in crosses])

def part2():
    return min([PA[cross] + PB[cross] for cross in crosses])

print (part1())
print (part2())