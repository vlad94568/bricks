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


# Player.
class Player(SceneElement):
    def __init__(self, x, y):
        SceneElement.__init__(self, x, y)

    # Draws grass patch.
    def draw(self, screen):
        pygame.draw.rect(screen, GREEN_COLOR, (self.x, 450, 20, 20), 5)  # Base.
        pygame.draw.line(screen, GREEN_COLOR, [self.x + 9, 450], [self.x + 9, 435], 5)  # Turret.
