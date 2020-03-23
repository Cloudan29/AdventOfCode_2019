class Chemical:
    def __init__(self, name, reacts=[], per_reacts=0):
        self.name = name
        self.reacts = []
        self.per_reacts = 0
        self.need = 0

        self.set_reacts(reacts)
        self.set_per_reacts(per_reacts)

    def set_reacts(self, reacts):
        for react in reacts:
            self.reacts.append((react[0], react[1]))

    def set_per_reacts(self, per_reacts):
        self.per_reacts = per_reacts

    def calc_need(self, amount):
        if self.name == 'ORE':
            return []

        self.need += amount

        factor = 1
        while factor * self.per_reacts < amount:
            factor += 1

        nexts = []
        for react in self.reacts:
            nexts.append((react[0] * factor, react[1]))

        return nexts

    def __repr__(self):
        thing = []
        for react in self.reacts:
            thing.append((react[0], react[1].name))
        return str(self.per_reacts) + " " + self.name + " " + str(thing)


def chem_exists(name):
    for chem in chemicals:
        if name == chem.name:
            return True
    
    return False


inp = open("inputs/day14.txt")
chemicals = []

for line in inp:
    reactants, product = line.split(" => ")
    reacts = []

    product = product.rstrip()
    product = product.split(" ")
    product = (int(product[0]), product[1])

    reactants = reactants.split(", ")

    for reactant in reactants:
        reactant = reactant.split(" ")
        reactant = (int(reactant[0]), reactant[1])

        if not chem_exists(reactant[1]):
            new_chem = Chemical(reactant[1])
            chemicals.append(new_chem)
            reacts.append((int(reactant[0]), new_chem))
        else:
            for chemical in chemicals:
                if chemical.name == reactant[1]:
                    reacts.append((int(reactant[0]), chemical))
                    break

    if chem_exists(product[1]):
        for chemical in chemicals:
            if chemical.name == product[1]:
                chemical.set_per_reacts(product[0])
                chemical.set_reacts(reacts)
                break
    else:
        chemicals.append(Chemical(product[1], reacts, product[0]))


def part1():
    queue = []
    ans = 0

    for chemical in chemicals:
        if chemical.name == 'FUEL':
            queue.append((1, chemical))
    
    while len(queue) > 0:
        next_chem = queue.pop(0)
        nexts = next_chem[1].calc_need(next_chem[0])

        for n in nexts:
            queue.append((n[0], n[1]))

    for chemical in chemicals:
        for react in chemical.reacts:
            if 'ORE' == react[1].name:
                factor = 1
                while factor * chemical.per_reacts < chemical.need:
                    factor += 1

                ans += react[0] * factor

    return ans

def part2():
    pass


print(part1())
print(part2())
