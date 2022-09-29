from Animal import Animal
from Call import Call
from Coordinates import Coordinates
from Event import Event
from OrganismType import OrganismType

durationSuperPower = 5
superPowerRechargeTime = 5 + durationSuperPower
nextmove = -1
superpower = None
loadingSuperPower = 0
timeofSuperPower = 0
class Human(Animal):
    def __init__(self,position,World):
        super(Human, self).__init__(position,World)
        self.strength = 15
        self.initiative = 4
        self.kod = "H"
        self.type = OrganismType.HUMAN
        self.superpower = 0
        self.timeofSuperPower = 0
        self.loadingSuperPower = 0
        self.color = (0, 155, 119)
        self.nextmove = -1
    def newChild(self,position,world):
        return None
    def action(self):

        self.superPower()
        if self.nextmove != -1:
            newCord = Coordinates(self.position.x,self.position.y)
            if self.nextmove == 0:
                newCord.x -= 1
            elif self.nextmove == 1:
                newCord.x += 1
            elif self.nextmove == 2:
                newCord.y -= 1
            elif self.nextmove == 3:
                newCord.y += 1
            self.nextmove = -1
            if self.world.checkcordsAnimals(newCord.x,newCord.y):
                return Event(self.position, Call.move, newCord)
        return None
    def superPower(self):
        if self.superpower == 1:
            self.timeofSuperPower -=1
            self.world.eventManager(Event(self.position,Call.killAll, self.position))

        if self.timeofSuperPower ==0:
            self.superpower =0

        if self.loadingSuperPower != 0:
            self.loadingSuperPower -=1

        if self.loadingSuperPower != 0:
            self.loadingSuperPower -=1

    def activateSuperPower(self):
        if loadingSuperPower == 0:
            print("SuperPowerActiavte")
            self.superpower = 1
            self.loadingSuperPower = superPowerRechargeTime
            self.timeofSuperPower = durationSuperPower
        self.superPower()
    def save(self,file):
        file.write(self.kod)
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
        file.write(str(self.timeofSuperPower))
        file.write(" ")
        file.write(str(self.loadingSuperPower))
        file.write(" ")
        file.write(str(self.superpower))
        file.write(" ")
        file.write("\n")
    def load(self,file):
        self.turn = int(file[1])
        self.strength = int(file[2])
        self.initiative = int(file[3])
        self.position.x = int(file[4])
        self.position.y = int(file[5])
        self.timeofSuperPower = int(file[6])
        self.loadingSuperPower = int(file[7])
        self.superpower = int(file[8])


