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
from src.common import *


# Grass patch.
class Grass(SceneElement):
    def __init__(self, x, min_height, max_height, num_of_stalks, color):
        SceneElement.__init__(self, x, screen_height)

        self.max_grass_height = max_height
        self.min_grass_height = min_height
        self.num_of_stalks = num_of_stalks
        self.grass_color = color
        self.stalks = []  # List of stalks heights in px.

        for _ in range(0, self.num_of_stalks):
            self.stalks.append(random.randint(self.min_grass_height, self.max_grass_height))

    # Draws grass patch.
    def draw(self, screen):
        stalk_x = self.x

        for h in self.stalks:
            pygame.draw.rect(screen, self.grass_color, (stalk_x, screen_height - h, 2, h))

            stalk_x = stalk_x + 4
