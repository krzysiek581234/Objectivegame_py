from Animal import Animal
from OrganismType import OrganismType

class Sheep(Animal):
    def __init__(self,position,World):
        super(Sheep, self).__init__(position,World)
        self.strength = 4
        self.initiative = 4
        self.kod = "S"
        self.type = OrganismType.SHEEP
        self.color = (181, 101, 167)
    def newChild(self,position,world):
        return Sheep(position,world)