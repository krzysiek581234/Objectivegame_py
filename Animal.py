from Organism import *
from Call import *
from Event import Event

class Animal(Organism):
    def __init__(self,position,World):
        super().__init__(position,World)

    def randmoveCords(self,rangee):
        nextCords = Coordinates(self.position.x, self.position.y)
        do = True
        for x in range(-1, 2):
            for y in range(-1, 2):
                if self.world.checkcordsAnimals(self.position.x +x,self.position.y+ y) :
                    if  self.world.census[self.world.world_map[self.position.x +x][self.position.y+ y]].type != self.type:
                        do = False
                    if  self.world.world_map[self.position.x +x][self.position.y+ y] == -1:
                        do = False
        if do:
            return None
        notexit = True
        while notexit:
            randx = random.randrange(-rangee,rangee+1)
            randy = random.randrange(-rangee,rangee+1)
            nextCords.x = self.position.x + randx
            nextCords.y = self.position.y + randy
            if self.world.checkcordsAnimals(nextCords.x, nextCords.y):
                break
        return nextCords

    def action(self):
        nextCods = self.randmoveCords(1)
        if nextCods ==None:
            return None
        return Event(self.position,Call.move,nextCods)

    def collision(self, attacker):
        if(self.type == attacker.type):
            return self.newAnimal()
        else:
            return Event(attacker.position,Call.kill, self.position)

    def newAnimal(self):
        childCords = self.randmoveCords(1)
        if childCords ==None:
            return None
        else:
            return Event(self.position, Call.create, childCords)

    def newChild(self,position,World):
        pass
    def getkod(self):
        return self.kod