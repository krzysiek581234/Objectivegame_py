import random

from Animal import Animal
from Call import Call
from Event import Event
from OrganismType import OrganismType

class Fox(Animal):
    def __init__(self,position,World):
        super(Fox, self).__init__(position,World)
        self.strength = 3
        self.initiative = 7
        self.kod = "F"
        self.type = OrganismType.FOX
        self.color = (221, 65, 36)
    def newChild(self,position,world):
        return Fox(position,world)

    def action(self):
        nextCods = self.randmoveCords(1)
        if nextCods == None:
            return None
        if self.world.census[self.world.world_map[nextCods.x][nextCods.y]].strength < self.strength:
            return Event(self.position, Call.move, nextCods)
        else:
            return None