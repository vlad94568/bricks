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

import random
import pygame
import math
import time
from pygame import gfxdraw

# Common colors.
RED_COLOR = (255, 0, 0)
RED2_COLOR = (255, 65, 25)
GREEN_COLOR = (0, 255, 0)
WHITE_COLOR = (255, 255, 255)
CLOUD_COLOR = (239, 239, 239)
YELLOW_COLOR = (255, 255, 0)
BLACK_COLOR = (0, 0, 0)
DARK_GREY_COLOR = (31, 31, 31)
GREY_COLOR = (128, 128, 128)
SLACK_COLOR = (30, 22, 29)
BLUE_COLOR = (215, 220, 250)
DARK_GREEN_COLOR = (60, 160, 40)
PINK_COLOR = (255, 105, 130)
DARK_BLUE_COLOR = (1, 22, 56)
BROWN_COLOR = (130, 65, 65)
BLUE_COLOR_2 = (66, 173, 244)
GREY_COLOR_2 = (150, 90, 100)

# Global vars.
screen_width = 640
screen_height = 480


# Generates random color.
def mk_random_color():
    # Start with 32 to make sure that random colors are minimally bright.
    r = random.randint(32, 255)
    g = random.randint(32, 255)
    b = random.randint(32, 255)

    return r, g, b


# Draws a square with (x, y) center, 2*size diagonal, and turned at the angle.
def draw_turned_square(x, y, size, color, angle, screen):
    x1, y1 = transform(x, y, size, angle % 360)
    x2, y2 = transform(x, y, size, (angle + 90) % 360)
    x3, y3 = transform(x, y, size, (angle + 180) % 360)
    x4, y4 = transform(x, y, size, (angle + 270) % 360)

    pygame.gfxdraw.aapolygon(screen, [(x1, y1), (x2, y2), (x3, y3), (x4, y4)], color)


# Transforms (x, y) coordinate to distance at a given angle.
# Returns new (x, y) coordinate for the new location.
def transform(x, y, distance, angle):
    if angle <= 90:
        rad = math.radians(angle)

        new_x = x + distance * math.sin(rad)
        new_y = y - distance * math.cos(rad)
    elif angle <= 180:
        rad = math.radians(180 - angle)

        new_x = x + distance * math.sin(rad)
        new_y = y + distance * math.cos(rad)
    elif angle <= 270:
        rad = math.radians(270 - angle)

        new_x = x - distance * math.cos(rad)
        new_y = y + distance * math.sin(rad)
    else:
        rad = math.radians(360 - angle)

        new_x = x - distance * math.sin(rad)
        new_y = y - distance * math.cos(rad)

    return new_x, new_y


# Base class for all scene elements.
class SceneElement:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        assert True, "Not implemented"



