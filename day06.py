inp = open("inputs/day06.txt")

class Planet():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    def total_orbits(self):
        if self.parent == None:
            return 0
        
        return 1 + self.parent.total_orbits()
        
    def __str__(self):
        return self.name

    def __repr__(self):
        children = [child.name for child in self.children]
        return str(children) + "->" + self.name + "->" + str(self.parent)
    
planets = []
for line in inp:
    body_name, planet_name = line.rstrip().split(")")
    satelite = None
    body = None
    for p in planets:
        if planet_name == p.name:
            satelite = p
        if body_name == p.name:
            body = p

    if satelite != None and body != None:
        satelite.parent = body
        body.children.append(satelite)
    elif satelite != None and body == None:
        body = Planet(body_name, None)
        body.children.append(satelite)
        satelite.parent = body
        planets.append(body)
    elif satelite == None and body != None:
        satelite = Planet(planet_name, body)
        body.children.append(satelite)
        planets.append(satelite)
    elif satelite == None and body == None:
        body = Planet(body_name, None)
        satelite = Planet(planet_name, body)
        body.children.append(satelite)
        planets.append(body)
        planets.append(satelite)

def part1():
    ans = 0
    for planet_name in planets:
        ans += planet_name.total_orbits()

    return ans

def part2():
    you = None
    for p in planets:
        if p.name == "YOU":
            you = p

    ans = 0
    searched = [you]
    queue = [you]
    path = []
    while len(queue) > 0:
        item = queue[-1]
        if item == None:
            queue.pop()
            continue

        while len(path) != 0:
            if item not in path[-1].children and item != path[-1].parent:
                path.pop()
            else:
                break

        if len(item.children) != 0:
            path.append(item)

        names = [c.name for c in item.children]
        if "SAN" in names:
            break

        queue.pop()

        if item.parent not in searched:
            queue.append(item.parent)
            searched.append(item.parent)
        
        for child in item.children:
            if child not in searched:
                queue.append(child)
                searched.append(child)

    return len(path) - 1

print (part1())
print (part2())