inp = open("inputs/day04.txt")
low, high = [int(num) for num in inp.read().split("-")]

def part1():
    ans = 0
    for i in range(low, high):
        password = [int(j) for j in str(i)]
        if password != sorted(password):
            continue

        for digit in password:
            if password.count(digit) >= 2:
                ans += 1
                break

    return ans

def part2():
    ans = 0
    for i in range(low, high):
        password = [int(j) for j in str(i)]
        if password != sorted(password):
            continue

        for digit in password:
            if password.count(digit) == 2:
                ans += 1
                break

    return ans

print (part1())
print (part2())