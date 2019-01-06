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


# Falling brick.
class Brick(SceneElement):
    # kinds:
    # 1 - normal brick (RED)
    # 2 - ammo brick (WHITE)
    # 3 - live break (GREEN)
    def __init__(self, x, y, y_speed, kind):
        SceneElement.__init__(self, x, y)

        self.y_speed = y_speed
        self.kind = kind
        self.state = 1  # 1 - falling (normal), 2 - explosion
        self.frame_cnt = 0
        self.x_adj = 0

        if self.kind == 1:
            self.color = RED_COLOR
        elif self.kind == 2:
            self.color = WHITE_COLOR
        else:
            self.color = GREEN_COLOR

    # Draws the brick.
    def draw(self, screen):
        # TODO: add different visual depending on the kind of the brick.
        pygame.draw.rect(screen, self.color, (self.x, self.y, 15, 10), 3)