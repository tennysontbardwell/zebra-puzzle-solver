class House:
    def __init__(self, nat, color, cigar, bev, animal):
        self.nat = nat
        self.color = color
        self.cigar = cigar
        self.bev = bev
        self.animal = animal
        self.all = [nat, color, cigar, bev, animal]


def checkSame(s1, s2, houses):
    for house in houses:
        i = 0
        for thing in house.all:
            if s1 == thing:
                i += 1
        if i == 2:
            return True
    return False

def nextTo(s1, s2, houses, dif):
    """1 means s1 is right of s2, -1 means s1 is left of s2"""
    loc1 = -1
    loc2 = -1
    for i, h in enumerate(houses):
        for thing in h.all:
            if thing == s1:
                loc1 = i
            if thing == s2:
                loc2 = i
    return loc1 - loc2 == dif



NATS = ['brit', 'dane', 'german', 'swede', 'norwegian']
COLORS = ['blue', 'yellow', 'green', 'red', 'white']
CIGARS = ['dunhill', 'blue master', 'pall mall', 'prince', 'blends']
BEVS = ['root beer', 'milk', 'water', 'coffee', 'tea']
ANIMALS = ['fish', 'dog', 'bird', 'cat', 'horse']

def checkSetup(houses):
    if not houses[2].bev == BEVS[1]:
        return False
    if not checkSame(NATS[0], COLORS[3], houses):
        return False
    if not checkSame(NATS[3], ANIMALS[1], houses):
        return False
    if not checkSame(NATS[1], BEVS[4], houses):
        return False
    if not nextTo(COLORS[2], COLORS[4], houses, -1):
        return False
    if not checkSame(COLORS[2], BEVS[3], houses):
        return False
    if not checkSame(ANIMALS[2], CIGARS[2], houses):
        return False
    if not checkSame(COLORS[1], CIGARS[0], houses):
        return False
    if not houses[0].nat == NATS[4]:
        return False
    if not (nextTo(CIGARS[4] == ANIMALS[3], houses, 1) or 
            nextTo(CIGARS[4] == ANIMALS[3], houses, -1)):
        return False
    if not (nextTo(CIGARS[0] == ANIMALS[4], houses, 1) or 
            nextTo(CIGARS[0] == ANIMALS[4], houses, -1)):
        return False
    if not checkSame(CIGARS[1], BEVS[0], houses):
        return False
    if not checkSame(NATS[2], CIGARS[3], houses):
        return False
    if not (nextTo(NATS[4] == COLORS[0], houses, 1) or 
            nextTo(NATS[4] == COLORS[0], houses, -1)):
        return False
    if not (nextTo(CIGARS[4] == BEVS[2], houses, 1) or 
            nextTo(CIGARS[4] == BEVS[2], houses, -1)):
        return False
    return True


def allPerm(things):
    if len(things) is 2:
        return [ [ things[0], things[1] ], [things[1], things[0] ] ]
    else:
        toReturn = []
        for index, item in enumerate(things):
            new = list(things)
            del new[index]
            temp = allPerm(new)
            toReturn += [list(item)+x for x in temp]
        return toReturn


def main():
    natOrder = allPerm(NATS)
    colorOrder = allPerm(COLORS)
    cigarOrder = allPerm(CIGARS)
    bevOrder = allPerm(BEVS)
    animalOrder = allPerm(ANIMALS)
    for nOi, nO in enumerate(natOrder):
        for coOi, coO in enumerate(colorOrder):
            for ciOi, ciO in enumerate(cigarOrder):
                for bOi, bO in enumerate(bevOrder):
                    for aOi, aO in enumerate(animalOrder):
                        houses = []
                        for i in range(4):
                            h = House(nO[i], coO[i], ciO[i], bO[i], aO[i])
                            houses.append(h)
                        if checkSetup(houses):
                            print('found it')
                            return True
                        else:
                            print("Completed %d %d %d %d %d" % 
                                (nOi, coOi, ciOi, bOi, aOi))

if __name__ == "__main__":
    main()