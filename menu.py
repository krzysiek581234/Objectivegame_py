import math

import pygame
import pygame_menu

from Gui.WorldGui import WorldGui
from World import World
import os


class Menu:
    MAIN_THEME = pygame_menu.themes.THEME_ORANGE.copy()
    def __init__(self):
        pygame.font.init()
        pygame.init()
        pygame.display.set_caption("World Simulator")
        self.surface = pygame.display.set_mode((750, 750))

    def start_simulation(self):
        #funWord = World()
        #funWord.initMapa()
        #funWord.sortOrg()
        #funWord.nextturn()
        #funWord.driveWorld()

        #funWord.display()

        world = WorldGui()
        world.initMapa()
        world.display()

    @staticmethod
    def load_simulation():
        world = WorldGui()
        world.load()
        world.display()
        print("LOAD")

    @staticmethod
    def save_height(height):
        height = math.floor(height)
        World.height = height
        print(height)
        #world.height = height

    @staticmethod
    def save_width(width):
        width = math.floor(width)
        World.width = width
        print(width)
        #world.height = height

    def display_menu(self):
        menu = pygame_menu.Menu('', 750, 750, theme=self.MAIN_THEME)
        menu.add.button('Play', self.start_simulation)
        menu.add.button('Load', self.load_simulation)
        menu.add.range_slider('ROWS: ', range_values=(5, 25), default=10, increment=1,onchange=self.save_width)
        menu.add.range_slider('COLUMS: ', range_values=(5, 25), default=10, increment=1,onchange=self.save_height)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.surface)