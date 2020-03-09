"""
Still haven't finished part 2 to this one
"""

class Planet:
    def __init__(self, pos):
        self.pos = pos
        self.vel = {'x': 0, 'y': 0, 'z': 0}

    def apply_gravity(self, dx, dy, dz):
        self.vel['x'] += dx
        self.vel['y'] += dy
        self.vel['z'] += dz

    def apply_velocity(self):
        self.pos['x'] += self.vel['x']
        self.pos['y'] += self.vel['y']
        self.pos['z'] += self.vel['z']

    def potential_energy(self):
        return abs(self.pos['x']) + abs(self.pos['y']) + abs(self.pos['z'])
    
    def kinetic_energy(self):
        return abs(self.vel['x']) + abs(self.vel['y']) + abs(self.vel['z'])

    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()

    def __str__(self):
        return str(self.pos['x']) + ',' + str(self.pos['y']) + ',' + str(self.pos['z'])
    
    def __repr__(self):
        return str(self)


inp = open("inputs/day12.txt")
positions = []
for line in inp:
    line = line.replace('<', '').replace('>', '')
    positions.append([int(cord[2:]) for cord in line.split(', ')])


def part1():
    planets = [Planet({'x': p[0], 'y': p[1], 'z': p[2]}) for p in positions]
    for step in range(1000):
        dx = [0,0,0,0]
        dy = [0,0,0,0]
        dz = [0,0,0,0]
        for i in range(len(planets)):
            for j in range(len(planets)):
                if j == i:
                    continue

                if planets[i].pos['x'] > planets[j].pos['x']:
                    dx[i] -= 1
                elif planets[i].pos['x'] < planets[j].pos['x']:
                    dx[i] += 1

                if planets[i].pos['y'] > planets[j].pos['y']:
                    dy[i] -= 1
                elif planets[i].pos['y'] < planets[j].pos['y']:
                    dy[i] += 1

                if planets[i].pos['z'] > planets[j].pos['z']:
                    dz[i] -= 1
                elif planets[i].pos['z'] < planets[j].pos['z']:
                    dz[i] += 1

        for i in range(len(planets)):
            planets[i].apply_gravity(dx[i], dy[i], dz[i])
            planets[i].apply_velocity()

    ans = 0
    for planet in planets:
        ans += planet.total_energy()

    return ans

def part2():
    planets = [Planet({'x': p[0], 'y': p[1], 'z': p[2]}) for p in positions]
    past_states = []
    iterations = 0
    while True:
        dx = [0,0,0,0]
        dy = [0,0,0,0]
        dz = [0,0,0,0]
        for i in range(len(planets)):
            for j in range(len(planets)):
                if j == i:
                    continue

                if planets[i].pos['x'] > planets[j].pos['x']:
                    dx[i] -= 1
                elif planets[i].pos['x'] < planets[j].pos['x']:
                    dx[i] += 1

                if planets[i].pos['y'] > planets[j].pos['y']:
                    dy[i] -= 1
                elif planets[i].pos['y'] < planets[j].pos['y']:
                    dy[i] += 1

                if planets[i].pos['z'] > planets[j].pos['z']:
                    dz[i] -= 1
                elif planets[i].pos['z'] < planets[j].pos['z']:
                    dz[i] += 1

        for i in range(len(planets)):
            planets[i].apply_gravity(dx[i], dy[i], dz[i])
            planets[i].apply_velocity()
        
        p1 = (planets[0].pos['x'], planets[0].pos['y'], planets[0].pos['z'], planets[0].vel['x'], planets[0].vel['y'], planets[0].vel['z'])
        p2 = (planets[1].pos['x'], planets[1].pos['y'], planets[1].pos['z'], planets[1].vel['x'], planets[1].vel['y'], planets[1].vel['z'])
        p3 = (planets[2].pos['x'], planets[2].pos['y'], planets[2].pos['z'], planets[2].vel['x'], planets[2].vel['y'], planets[2].vel['z'])
        p4 = (planets[3].pos['x'], planets[3].pos['y'], planets[3].pos['z'], planets[3].vel['x'], planets[3].vel['y'], planets[3].vel['z'])
        new_state = (p1, p2, p3, p4)
        if new_state in past_states:
            break
        else:
            past_states.append(new_state)
            iterations += 1

    return iterations

print (part1())
print (part2())