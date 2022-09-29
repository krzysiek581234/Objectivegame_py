import random

from Animals.CyberSheep import CyberSheep
from Animals.Fox import Fox
from Animals.Human import Human
from Animals.Sheep import Sheep
from Animals.Turtle import Turtle
from Animals.Wolf import Wolf
from Animals.Antelope import Antelope
from Call import Call
from Coordinates import Coordinates
from Event import Event
from OrganismType import OrganismType
from Plants.Blueberries import Blueberries
from Plants.Borsch import Borsch
from Plants.Dandelion import Dandelion
from Plants.Grass import Grass
from Plants.Guarana import Guarana


class World:
    height =10
    width = 10
    world_map =None
    def __init__(self):
        self.turn = 0
        self.census = []
        self.world_map = [[-1 for x in range(self.width)] for y in range(self.height)]
        self.numberofOrganizm = 0

    def driveWorld(self):
        print(" ____",end='')
        for i in range(self.width-1):
            print("____",end='')
        print("")
        for i in range(self.height):
            print("|",end='')
            for j in range(self.width):
                print(" ",end='')
                if(self.world_map[i][j] == -1):
                    print(" ",end='')
                else:
                    print(self.census[self.world_map[i][j]].getkod(),end='')
                print(" ",end='')
                if(j<self.width-1):
                    print("|",end='')
            print("|")
            if (i < self.height - 1):
                print("|", end='')
                for x in range(self.width-1):
                    print("----", end='')
                print("---", end='')
                print("|")
        print(" ____", end='')
        for x in range(self.width-1):
            print("____", end='')
        print("")

    def initMapa(self):
        for animaltype in OrganismType:
            self.census.append(self.createOrg(animaltype,None,None,None))
            self.numberofOrganizm += 1
        #self.census.append(self.createOrg(OrganismType.GUARANA, None, None))
        #self.numberofOrganizm += 1
        #self.census.append(self.createOrg(OrganismType.BORSCH, None, None))
        #self.numberofOrganizm += 1
        #self.census.append(self.createOrg(OrganismType.GRASS, None, None))
        #self.numberofOrganizm += 1
        self.driveWorld()

    def createOrg(self,TypeOrg,xpos,ypos,index):
        newOrg = None
        if xpos == None or ypos == None:
            Cords = self.randCords()
        else:
            Cords = Coordinates(xpos,ypos)
        if TypeOrg == OrganismType.ANTELOPE:
            newOrg = Antelope(Cords, self)
        elif TypeOrg == OrganismType.WOLF:
            newOrg = Wolf(Cords,self)
        elif TypeOrg == OrganismType.SHEEP:
            newOrg = Sheep(Cords,self)
        elif TypeOrg == OrganismType.CYBER_SHEEP:
            newOrg = CyberSheep(Cords,self)
        elif TypeOrg == OrganismType.TURTLE:
            newOrg = Turtle(Cords,self)
        elif TypeOrg == OrganismType.FOX:
            newOrg = Fox(Cords,self)
        elif TypeOrg == OrganismType.HUMAN:
            newOrg = Human(Cords,self)
        elif TypeOrg == OrganismType.BLUEBERRIES:
            newOrg = Blueberries(Cords,self)
        elif TypeOrg == OrganismType.BORSCH:
            newOrg = Borsch(Cords,self)
        elif TypeOrg == OrganismType.DANDELION:
            newOrg = Dandelion(Cords,self)
        elif TypeOrg == OrganismType.GRASS:
            newOrg = Grass(Cords,self)
        elif TypeOrg == OrganismType.GUARANA:
            newOrg = Guarana(Cords,self)
        if index == None:
            self.world_map[Cords.x][Cords.y] = self.numberofOrganizm
        else:
            self.world_map[Cords.x][Cords.y] = index

        return newOrg

    def randCords(self):
        while True:
            randx = random.randrange(self.width)
            randy = random.randrange(self.height)
            position = Coordinates(randx,randy)
            if self.ispositionfree(position):
                break
        return position
    def checkcords(self,x,y):
        if(x >= 0 and x < self.width and y >= 0 and y< self.height and self.world_map[x][y] == -1):
            return True
        else:
            return False
    def checkcordsAnimals(self,x,y):
        if(x >= 0 and x < self.width and y >= 0 and y< self.height):
            return True
        else:
            return False

    def ispositionfree(self,position):
        if self.world_map[position.x][position.y] == -1:
            return True
        else:
            return False
    def nextturn(self):
        self.turn +=1
        for i in self.census:
            if i.alive == True:
                event = i.action()
                #print(i.type)
                if event != None:
                    self.eventManager(event)
        self.sortOrg()

    def sortOrg(self):
        self.world_map = [[-1 for x in range(self.width)] for y in range(self.height)]
        self.census.sort(key=lambda x: x.initiative,reverse=True)
        for i in range(self.numberofOrganizm):
            self.world_map[self.census[i].position.x][self.census[i].position.y] = i

    def isHuman(self):
        for org in self.census:
            if org.type == OrganismType.HUMAN:
                return org
            else:
                return None

    def eventManager(self,event):
        if event == None:
            return
        else:
            who = event.who #position
            where = event.where #position
            what = event.what
            if who.x != None and who.y != None and self.world_map[who.x][who.y] != -1:
                if what == Call.move:
                    if self.world_map[where.x][where.y] == -1:
                        print(self.census[self.world_map[who.x][who.y]].type, "rusza sie", who.x, who.y ,"->", where.x, where.y)
                        Org = self.census[self.world_map[who.x][who.y]]
                        self.world_map[where.x][where.y] = self.world_map[who.x][who.y]
                        self.world_map[who.x][who.y] = -1
                        Org.position.update(where.x,where.y)
                        print(where.x,where.y)
                    else:
                        attacker = self.census[self.world_map[who.x][who.y]]
                        defender = self.census[self.world_map[where.x][where.y]]
                        if attacker != defender:
                            Returnevent = defender.collision(attacker)
                            if Returnevent != None:
                                self.eventManager(Returnevent)
                elif what == Call.kill:

                    attacker = self.census[self.world_map[who.x][who.y]]
                    defender = self.census[self.world_map[where.x][where.y]]
                    if attacker.type == OrganismType.CYBER_SHEEP and defender.type == OrganismType.BORSCH:
                        print("Barszcz zostaja zabity przez owce")
                        self.census[self.world_map[where.x][where.y]].alive = False
                        self.census.pop(self.world_map[where.x][where.y])
                        self.numberofOrganizm -=1
                        self.world_map[where.x][where.y] = -1
                        self.eventManager(Event(who,Call.move,where))
                        return
                    if attacker.strength > defender.strength:
                        print(attacker.type,"zabija",defender.type)

                        self.census[self.world_map[where.x][where.y]].alive = False
                        self.census.pop(self.world_map[where.x][where.y])
                        self.numberofOrganizm -=1
                        self.world_map[where.x][where.y] = -1
                        self.eventManager(Event(who,Call.move,where))
                    else:
                        #print(defender.type,"zabija",attacker.type)
                        #self.world_map[temp.x][temp.y] = -1
                        self.census[self.world_map[who.x][who.y]].alive = False
                        self.census.pop(self.world_map[who.x][who.y])
                        self.world_map[who.x][who.y] = -1
                        self.numberofOrganizm -=1
                elif what == Call.create:
                    if self.world_map[where.x][where.y] == -1:
                        parent = self.census[self.world_map[who.x][who.y]]
                        print(parent.type,"Create")
                        son = parent.newChild(where,self)
                        self.census.append(son)
                        self.world_map[where.x][where.y] = self.numberofOrganizm
                        self.numberofOrganizm += 1
                elif what == Call.poison:
                    print("Blueberries poision ", self.census[self.world_map[who.x][who.x]].type)
                    self.census[self.world_map[who.x][who.y]] = None
                    self.world_map[who.x][who.y] = -1
                elif what == Call.killAllAnimals:
                    print("Killall")
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if self.checkcordsAnimals(who.x +x, who.y +y) and (x != 0 and y !=0 ):
                                if self.world_map[who.x +x][who.y +y] != -1:
                                    Orgtype = self.census[self.world_map[who.x +x][who.y +y]].type
                                    if Orgtype == OrganismType.WOLF or Orgtype == OrganismType.FOX or Orgtype == OrganismType.SHEEP or Orgtype == OrganismType.HUMAN or Orgtype == OrganismType.TURTLE or Orgtype == OrganismType.ANTELOPE:
                                        self.census[self.world_map[who.x +x][who.y +y]].alive = False
                                        self.census.pop(self.world_map[who.x +x][who.y +y])
                                        self.numberofOrganizm -= 1
                                        self.world_map[who.x +x][who.y +y] = -1

                elif what == Call.killAll:
                    print("SuperPower")
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if x == 0 and y ==0 or self.census[self.world_map[who.x +x][who.y +y]].type == OrganismType.HUMAN:
                                continue
                            if self.checkcordsAnimals(who.y +y,who.x +x):
                                if self.world_map[who.y +y][who.x +x] != -1:
                                    self.census.pop(self.world_map[who.y +y][who.x +x])
                                    self.numberofOrganizm -= 1
                                    self.world_map[who.y +y][who.x +x] = -1
                                    self.sortOrg()
                self.sortOrg()
            else:
                return


