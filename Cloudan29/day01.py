def part1():
    ans = 0
    with open("Cloudan29/inputs/day01.txt") as inp:
        for line in inp:
            ans += int(int (line) / 3) - 2
    
    return ans


def part2():
    ans = 0
    with open("Cloudan29/inputs/day01.txt") as inp:
        for line in inp:
            fuel = int(int(line) / 3) - 2
            ans += fuel
            while fuel > 0:
                fuel = int(fuel / 3) - 2
                if fuel > 0:
                    ans += fuel

    return ans

#print (part1())
print (part2())