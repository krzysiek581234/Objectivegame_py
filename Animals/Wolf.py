from Animal import Animal
from OrganismType import OrganismType

class Wolf(Animal):
    def __init__(self,position,World):
        super(Wolf, self).__init__(position,World)
        self.strength = 9
        self.initiative = 5
        self.kod = "W"
        self.type = OrganismType.WOLF
        self.color = (146, 168, 209)
    def newChild(self,position,world):
        return Wolf(position,world)