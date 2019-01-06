#
#      _/_/_/    _/_/_/    _/_/_/    _/_/_/  _/    _/    _/_/_/
#     _/    _/  _/    _/    _/    _/        _/  _/    _/
#    _/_/_/    _/_/_/      _/    _/        _/_/        _/_/
#   _/    _/  _/    _/    _/    _/        _/  _/          _/
#  _/_/_/    _/    _/  _/_/_/    _/_/_/  _/    _/  _/_/_/
#
#  By Vlad Ivanov, 2018.
#  By Nikita Ivanov, 2018
#
#  Email: vlad94568@gmail.com

import pygame
from src.basics import *


# Grass patch.
class Grass(SceneElement):
    def __init__(self, x, y):
        SceneElement.__init__(self, x, y)

        self.max_grass_height = 10
        self.min_grass_height = 5
        self.num_of_stalks = 100
        self.grass_color = GREEN_COLOR
        self.stalks = []  # List of stalks heights in px.

        for _ in range(0, self.num_of_stalks):
            self.stalks.append(random.randint(self.min_grass_height, self.max_grass_height))

    # Draws grass patch.
    def draw(self, screen):
        ()
        # TODO
