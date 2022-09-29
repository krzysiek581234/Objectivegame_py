import random

from Call import Call
from Event import Event
from OrganismType import OrganismType
from Plant import Plant


class Borsch(Plant):
    def __init__(self,position,World):
        super(Borsch, self).__init__(position,World)
        self.strength = 10
        self.kod = "X"
        self.type = OrganismType.BORSCH
        self.color = (255, 111, 97)
    def newChild(self,position,world):
        return Borsch(position,world)
    def action(self):
        self.world.eventManager(Event(self.position, Call.killAllAnimals, self.position))
        if random.randrange(100) < 10:
            while True:
                childCords = self.randmoveCords(1)
                if childCords == None:
                    return None
                else:
                    if self.world.ispositionfree(childCords):
                        return Event(self.position, Call.create, childCords)
        return None
    def collision(self, attacker):
        Returnevent = Event(attacker.position,Call.kill,self.position)
        self.world.eventManager(Returnevent)
        if (attacker.strength > self.strength and attacker.type != OrganismType.CYBER_SHEEP):
            return  Event(attacker.position, Call.poison, attacker.position);
        return None