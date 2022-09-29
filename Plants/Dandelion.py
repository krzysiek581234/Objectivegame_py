import random

from Call import Call
from Event import Event
from OrganismType import OrganismType
from Plant import Plant


class Dandelion(Plant):
    def __init__(self,position,World):
        super(Dandelion, self).__init__(position,World)
        self.strength = 0
        self.kod = "D"
        self.type = OrganismType.DANDELION
        self.seeds = 3
        self.color = (107, 91, 149)
    def newChild(self,position,world):
        return Dandelion(position,world)
    def action(self):
        for x in range(self.seeds):
            if random.randrange(100) < 50:
                while True:
                    childCords = self.randmoveCords(1)
                    if childCords == None:
                        return None
                    else:
                        if self.world.ispositionfree(childCords):
                            return Event(self.position, Call.create, childCords)
        return None