import datetime
inp = open("inputs/day10.txt").read().split('\n')
w = len(inp[0])
h = len(inp)
asteroids = []
for j in range(len(inp)):
    for i in range(len(inp[j])):
        if inp[j][i] == '#':
            asteroids.append((i,j))

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def determinant(a, b):
    return a[0] * b[1] - b[0] * a[1]

def diff_directions(a, b):
    if a[0] == b[0]:
        return ((a[1] > 0 and b[1] < 0) or (a[1] < 0 and b[1] > 0))
    return ((a[0] > 0 and b[0] < 0) or (a[0] < 0 and b[0] > 0))

def part1():
    asteroid_scans = {}
    for asteroid in asteroids:
        scanned_asteroids = []
        remaining_asteroids = [a for a in asteroids]
        remaining_asteroids.remove(asteroid)
        while len(remaining_asteroids) > 0:
            closest_asteroid = (400,400)
            for ka in remaining_asteroids:
                if dist(asteroid, ka) < dist(asteroid, closest_asteroid):
                    closest_asteroid = ka

            scanned_asteroids.append(closest_asteroid)
            remaining_asteroids.remove(closest_asteroid)
            i = 0
            while i < len(remaining_asteroids):
                ca_vector = (closest_asteroid[0]-asteroid[0],closest_asteroid[1]-asteroid[1])
                ra_vector = (remaining_asteroids[i][0]-asteroid[0],remaining_asteroids[i][1]-asteroid[1])
                if determinant(ca_vector, ra_vector) == 0 and not diff_directions(ca_vector, ra_vector):
                    remaining_asteroids.pop(i)
                else:
                    i+=1

        asteroid_scans[asteroid] = len(scanned_asteroids)

    ans = (0,0)
    largest_scanned = 0
    for scan in asteroid_scans:
        if asteroid_scans[scan] > largest_scanned:
            ans = scan
            largest_scanned = asteroid_scans[scan]

    return (ans, asteroid_scans[ans])

print (part1())