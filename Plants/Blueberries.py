from Call import Call
from Event import Event
from OrganismType import OrganismType
from Plant import Plant


class Blueberries(Plant):
    def __init__(self,position,World):
        super(Blueberries, self).__init__(position,World)
        self.strength = 99
        self.kod = "B"
        self.type = OrganismType.BLUEBERRIES
        self.color = (52, 86, 139)
    def newChild(self,position,world):
        return Blueberries(position,world)
    def collision(self, attacker):
        Returnevent = Event(attacker.position,Call.kill,self.position)
        self.world.eventManager(Returnevent)
        if (attacker.strength > self.strength):

            return  Event(attacker.position, Call.poison, attacker.position);
        return None