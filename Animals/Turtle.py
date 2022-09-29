import random

from Animal import Animal
from Call import Call
from Event import Event
from OrganismType import OrganismType

class Turtle(Animal):
    def __init__(self,position,World):
        super(Turtle, self).__init__(position,World)
        self.strength = 4
        self.initiative = 4
        self.kod = "T"
        self.type = OrganismType.TURTLE
        self.color = (149, 82, 81)
    def newChild(self,position,world):
        return Turtle(position,world)
    def action(self):
        if random.randrange(4) == 0:
            nextCods = self.randmoveCords(1)
            if nextCods == None:
                return None
            return Event(self.position,Call.move,nextCods)
        return None
    def collision(self, attacker):
        if(self.type == attacker.type):
            return self.newAnimal()
        else:
            if attacker.strength < 5:
                print("Turtle defended himself")
                return None
            else:
                return Event(attacker.position,Call.kill, self.position)