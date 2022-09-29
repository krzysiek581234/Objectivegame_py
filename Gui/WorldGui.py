import math

import pygame
from pygame import font

from OrganismType import OrganismType
from World import World
class WorldGui(World):
    SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 750
    BOARD_WIDTH, BOARD_HEIGHT = 750, 750
    def __init__(self):
        super().__init__()
        self.window = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("World Simulator")
        self.field_width = self.BOARD_WIDTH / (self.width+1)
        self.field_height = self.BOARD_HEIGHT / (self.height+1)
        self.draw_world()
        self.fieldx =None
        self.fieldy =None
        self.type = None

    def addbuttons(self):
        textfont = pygame.font.SysFont('Corbel', 35)

        next_turn = pygame.draw.rect(self.window, (0,0,250),(750, 50, 200, 100))
        text = textfont.render('Start', True, (0,0,0))
        self.window.blit(text, (815, 75))

        save = pygame.draw.rect(self.window, (0,0,250),(750, 175, 200, 100))
        text = textfont.render('Save', True, (0,0,0))
        self.window.blit(text, (815, 200))

        textfont = pygame.font.SysFont('Corbel', 20)
        blueberries = pygame.draw.rect(self.window, (0,0,250),(750, 300, 100, 50))
        text = textfont.render('blueberries', True, (0,0,0))
        self.window.blit(text, (760, 310))

        borsch = pygame.draw.rect(self.window, (0,0,250),(750, 360, 100, 50))
        text = textfont.render('Borsch', True, (0,0,0))
        self.window.blit(text, (760, 370))

        dandelion = pygame.draw.rect(self.window, (0,0,250),(750, 420, 100, 50))
        text = textfont.render('dandelion', True, (0,0,0))
        self.window.blit(text, (760, 430))

        grass = pygame.draw.rect(self.window, (0,0,250),(750, 480, 100, 50))
        text = textfont.render('grass', True, (0,0,0))
        self.window.blit(text, (760, 490))

        guarana = pygame.draw.rect(self.window, (0,0,250),(750, 540, 100, 50))
        text = textfont.render('guarana', True, (0,0,0))
        self.window.blit(text, (760, 550))

        antelope = pygame.draw.rect(self.window, (0,0,250),(860, 300, 100, 50))
        text = textfont.render('antelope', True, (0,0,0))
        self.window.blit(text, (860, 310))

        cybersheep = pygame.draw.rect(self.window, (0,0,250),(860, 360, 100, 50))
        text = textfont.render('cybersheep', True, (0,0,0))
        self.window.blit(text, (860, 370))

        fox = pygame.draw.rect(self.window, (0,0,250),(860, 420, 100, 50))
        text = textfont.render('fox', True, (0,0,0))
        self.window.blit(text, (860, 430))

        sheep = pygame.draw.rect(self.window, (0,0,250),(860, 480, 100, 50))
        text = textfont.render('sheep', True, (0,0,0))
        self.window.blit(text, (860, 490))

        turtle = pygame.draw.rect(self.window, (0,0,250),(860, 540, 100, 50))
        text = textfont.render('turtle', True, (0,0,0))
        self.window.blit(text, (860, 550))

        wolf = pygame.draw.rect(self.window, (0,0,250),(860, 600, 100, 50))
        text = textfont.render('wolf', True, (0,0,0))
        self.window.blit(text, (860, 610))

        human = pygame.draw.rect(self.window, (0,0,250),(860, 660, 100, 50))
        text = textfont.render('human', True, (0,0,0))
        self.window.blit(text, (860, 670))

    def draw_world(self):
        self.window.fill((127, 205, 205))
        self.addbuttons()

        textfont = pygame.font.SysFont('Corbel', 50)
        for y in range(self.height):
            for x in range(self.width):
                color = (223, 207, 190)
                kod = ''
                text = textfont.render(kod, True, (0, 0, 0))
                pygame.draw.rect(self.window, color,(y * (self.field_width +1), x * (self.field_height+1), self.field_width, self.field_height))
                self.window.blit(text, (y * (self.field_width +1), x * (self.field_height+1)))

        for i in self.census:
            x = i.position.x
            y = i.position.y
            color = i.color
            kod = i.kod
            text = textfont.render(kod, True, (0, 0, 0))
            pygame.draw.rect(self.window, color, (y * (self.field_width + 1), x * (self.field_height + 1), self.field_width, self.field_height))
            self.window.blit(text, (y * (self.field_width + 1), x * (self.field_height + 1)))

                #pygame.draw.rect(self.window, (100,100,100),(y * self.field_width, x * self.field_height, self.field_width, self.field_height))

    def loop(self):
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                #print(mouseX)
                if mouseX >= 750 and mouseX <= 950 and mouseY >= 50 and mouseY <= 150:
                    self.nextturn()
                    print("NEXT")
                if mouseX >= 750 and mouseX <= 950 and mouseY >= 175 and mouseY <= 275:
                    print("SAVE")
                    self.save()

                if mouseX >= 750 and mouseX <= 850 and mouseY >= 300 and mouseY <= 400:
                    print("blueberries")
                    self.type = OrganismType.BLUEBERRIES
                if mouseX >= 750 and mouseX <= 850 and mouseY >= 360 and mouseY <= 400:
                    print("Borsch")
                    self.type = OrganismType.BORSCH
                if mouseX >= 750 and mouseX <= 850 and mouseY >= 420 and mouseY <= 470:
                    print("dandelion")
                    self.type = OrganismType.DANDELION
                if mouseX >= 750 and mouseX <= 850 and mouseY >= 480 and mouseY <= 530:
                    print("grass")
                    self.type = OrganismType.GRASS
                if mouseX >= 750 and mouseX <= 850 and mouseY >= 540 and mouseY <= 590:
                    print("guarana")
                    self.type = OrganismType.GUARANA
                if mouseX >= 860 and mouseX <= 960 and mouseY >= 300 and mouseY <= 400:
                    print("antelope")
                    self.type = OrganismType.ANTELOPE
                if mouseX >= 860 and mouseX <= 960 and mouseY >= 360 and mouseY <= 400:
                    print("cybersheep")
                    self.type = OrganismType.CYBER_SHEEP
                if mouseX >= 860 and mouseX <= 960 and mouseY >= 420 and mouseY <= 470:
                    print("fox")
                    self.type = OrganismType.FOX
                if mouseX >= 860 and mouseX <= 960 and mouseY >= 480 and mouseY <= 530:
                    print("sheep")
                    self.type = OrganismType.SHEEP
                if mouseX >= 860 and mouseX <= 960 and mouseY >= 540 and mouseY <= 590:
                    print("turtle")
                    self.type = OrganismType.TURTLE
                if mouseX >= 860 and mouseX <= 960 and mouseY >= 600 and mouseY <= 650:
                    print("wolf")
                    self.type = OrganismType.WOLF
                if mouseX >= 860 and mouseX <= 960 and mouseY >= 660 and mouseY <= 710:
                    print("human")
                    self.type = OrganismType.HUMAN

                if mouseX < 750:
                    fieldx = math.floor(mouseX / (self.field_width +1))
                    fieldy = math.floor(mouseY / (self.field_height +1))
                    print(fieldx, fieldy)
                    if self.type != None:
                        self.census.append(self.createOrg(self.type, fieldy,fieldx,None))
                        self.numberofOrganizm += 1
            human = self.isHuman()
            if (human != None):
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        human.nextmove = 0
                    elif e.key == pygame.K_DOWN:
                        human.nextmove = 1
                    elif e.key == pygame.K_LEFT:
                        human.nextmove = 2
                    elif e.key == pygame.K_RIGHT:
                        human.nextmove = 3
                    elif e.key == pygame.K_s:
                        human.activateSuperPower()

    def display(self):
        fps = 10
        clock = pygame.time.Clock()
        self.active = True
        def redraw_window():
            self.draw_world()
            pygame.display.update()
        while self.active:
            clock.tick(fps)
            self.loop()
            redraw_window()
        #Save.update_world_state(self.organisms, self.round, self.rows, self.columns)
    def save(self):
        with open("save.txt", "w") as file:
            file.write(str(self.height))
            file.write(" ")
            file.write(str(self.width))
            file.write(" ")
            file.write(str(self.turn))
            file.write(" ")
            file.write(str(self.numberofOrganizm))
            file.write(" ")
            file.write("\n")
            for organism in self.census:
                organism.save(file)
    def load(self):
        with open("save.txt", "r") as file:
            index =0
            list = file.readline().split(' ')
            self.height = int(list[0])
            self.width = int(list[1])
            self.turn = int(list[2])
            self.numberofOrganizm = int(list[3])
            self.field_width = self.BOARD_WIDTH / (self.width + 1)
            self.field_height = self.BOARD_HEIGHT / (self.height + 1)
            for x in range(self.numberofOrganizm):
                line = file.readline().split(' ')
                kod = line[0]
                if kod == 'H':
                    type = OrganismType.HUMAN
                elif kod == 'W':
                    type = OrganismType.WOLF
                elif kod == 'T':
                    type = OrganismType.TURTLE
                elif kod == 'F':
                    type = OrganismType.FOX
                elif kod == 'A':
                    type = OrganismType.ANTELOPE
                elif kod == 'C':
                    type = OrganismType.CYBER_SHEEP
                elif kod == 'S':
                    type = OrganismType.SHEEP
                elif kod == 'B':
                    type = OrganismType.BLUEBERRIES
                elif kod == 'X':
                    type = OrganismType.BORSCH
                elif kod == 'D':
                    type = OrganismType.DANDELION
                elif kod == 'G':
                    type = OrganismType.GRASS
                elif kod == '+':
                    type = OrganismType.GUARANA
                else:
                    type = None
                self.census.append(self.createOrg(type, 0, 0,index))
                self.census[x].load(line)
                index += 1



