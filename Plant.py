import random

from Organism import *
from Call import *
from Event import Event

class Plant(Organism):
    def __init__(self,position,World):
        super().__init__(position,World)
        self.strength =0
        self.initiative =0
        self.chanceofspreding = 20

    def action(self):
        if random.randrange(100) < self.chanceofspreding:
            while True:
                childCords = self.randmoveCords(1)
                if childCords == None:
                    return None
                else:
                    if self.world.ispositionfree(childCords):
                        return Event(self.position, Call.create, childCords)
        return None

    def randmoveCords(self,rangee):
        nextCords = Coordinates(self.position.x, self.position.y)
        do = True
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (self.world.checkcords(self.position.x +x,self.position.y+ y)):
                    do = False
        if do:
            return None
        notexit = True
        while notexit:
            randx = random.randrange(-rangee,rangee+1)
            randy = random.randrange(-rangee,rangee+1)
            nextCords.x = self.position.x + randx
            nextCords.y = self.position.y + randy
            if self.world.checkcords(nextCords.x, nextCords.y):
                break
        return nextCords

    def collision(self, attacker):
        return Event(attacker.position,Call.kill, self.position)

    def newChild(self,position,World):
        pass
    def getkod(self):
        return self.kod