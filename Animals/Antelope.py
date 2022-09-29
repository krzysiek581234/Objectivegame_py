import random
from Animal import Animal
from Call import Call
from Event import Event
from OrganismType import OrganismType


class Antelope(Animal):
    def __init__(self,position,World):
        super(Antelope, self).__init__(position,World)
        self.strength = 4
        self.initiative = 4
        self.kod = "A"
        self.type = OrganismType.ANTELOPE
        self.color = (68, 184, 172)
    def newChild(self,position,World):
        return Antelope(position,World)

    def action(self):
        nextCods = self.randmoveCords(2)
        if nextCods == None:
            return None
        return Event(self.position,Call.move,nextCods)
    def collision(self, attacker):
        if(self.type == attacker.type):
            return self.newAnimal()
        else:
            if random.randrange(2) == 1:
                #ucieka
                while(True):
                    nextCods = self.randmoveCords(2)
                    if nextCods == None:
                        return Event(attacker.position, Call.kill, self.position)
                    if self.world.ispositionfree(nextCods):
                        break
                print("Atylepe run out")
                return Event(self.position, Call.move, nextCods)
            return Event(attacker.position,Call.kill, self.position)
