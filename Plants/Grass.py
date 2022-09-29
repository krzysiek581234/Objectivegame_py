from OrganismType import OrganismType
from Plant import Plant


class Grass(Plant):
    def __init__(self,position,World):
        super(Grass, self).__init__(position,World)
        self.strength = 0
        self.kod = "G"
        self.type = OrganismType.GRASS
        self.color = (136, 176, 75)
    def newChild(self,position,world):
        return Grass(position,world)