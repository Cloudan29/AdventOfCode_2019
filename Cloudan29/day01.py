inp = open("Cloudan29/inputs/day01.txt")
modules_mass = [int(m) for m in inp.read().split("\n")]

def part1():
    ans = 0
    for mass in modules_mass:
        ans += int(mass / 3) - 2
    
    return ans


def part2():
    ans = 0
    for mass in modules_mass:
        fuel = int(mass / 3) - 2
        ans += fuel
        while fuel > 0:
            fuel = int(fuel / 3) - 2
            if fuel > 0:
                ans += fuel

    return ans

print (part1())
print (part2())