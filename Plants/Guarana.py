from Call import Call
from Event import Event
from OrganismType import OrganismType
from Plant import Plant


class Guarana(Plant):
    def __init__(self,position,World):
        super(Guarana, self).__init__(position,World)
        self.strength = 0
        self.kod = "+"
        self.type = OrganismType.GUARANA
        self.color =(247, 202, 201)
    def newChild(self,position,world):
        return Guarana(position,world)
    def collision(self, attacker):
        attacker.addStrength(3)
        return Event(attacker.position,Call.kill, self.position)