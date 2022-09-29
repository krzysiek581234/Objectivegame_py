import random
from Coordinates import *
class Organism:
    type = None
    kod = None
    position = None
    color = None
    world = None
    def __init__(self, position, World):
        self.turn = World.turn
        self.position = position
        self.strength = 0
        self.initiative = 0
        self.world = World
        self.color = (255,255,255)
        self.alive =True

    def addStrength(self,strength):
        self.strength += strength
    def collision(self,attacker):
        pass
    def newChild(self,position,World):
        pass
    def load(self,file):
        self.turn = int(file[1])
        self.strength = int(file[2])
        self.initiative = int(file[3])
        self.position.x = int(file[4])
        self.position.y = int(file[5])
    def save(self,file):
        file.write(str(self.kod))
        file.write(" ")
        file.write(str(self.turn))
        file.write(" ")
        file.write(str(self.strength))
        file.write(" ")
        file.write(str(self.initiative))
        file.write(" ")
        file.write(str(self.position.x))
        file.write(" ")
        file.write(str(self.position.y))
        file.write(" ")
        file.write("\n")

