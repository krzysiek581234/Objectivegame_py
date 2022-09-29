from Animal import Animal
from Call import Call
from Coordinates import Coordinates
from Event import Event
from OrganismType import OrganismType

class CyberSheep(Animal):
    barszczx = None
    barszczy = None
    distance = 99
    def __init__(self,position,World):
        super(CyberSheep, self).__init__(position,World)
        self.strength = 11
        self.initiative = 4
        self.kod = "C"
        self.type = OrganismType.CYBER_SHEEP
        self.color = (214, 80, 118)
    def newChild(self,position,world):
        return CyberSheep(position,world)
    def action(self):
        BorschPos = self.locateBarszcz()
        nextCods = Coordinates(self.position.x, self.position.y)
        #nextCods = self.randmoveCords(1)
        if BorschPos != None:
            if BorschPos.x - self.position.x > 0:
                x = 1
            elif BorschPos.x - self.position.x < 0:
                x = -1
            else:
                x =0
            if BorschPos.y - self.position.y > 0:
                y = 1
            elif BorschPos.y - self.position.y < 0:
                y = -1
            else:
                y =0

            nextCods.x = self.position.x +x
            nextCods.y = self.position.y +y
        else:
            nextCods = self.randmoveCords(1)
        if self.distance == 1:
            self.distance =99
        return Event(self.position,Call.move,nextCods)
    def locateBarszcz(self):
        for animal in self.world.census:
            if animal.type == OrganismType.BORSCH: ###
                if self.distance > self.greter(abs(self.position.x - animal.position.x),abs(self.position.y - animal.position.y) ):
                    self.distance = abs(self.position.x - animal.position.x) + abs(self.position.y - animal.position.y)
                    return Coordinates(animal.position.x, animal.position.y)
        return None
    def greter(self,a,b):
        if a>=b:
            return a
        else:
            return b