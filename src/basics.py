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

from src.colors import *

#
# Contains basic functions and classes for the game.
#


# Generates random color.
def mk_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


# Base class for all scene elements.
class SceneElement:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Colorful flower.
class Flower(SceneElement):
    def __init__(self, x):
        SceneElement.__init__(self, x, 427)

        self.stem_height = 40
        self.petal_color = mk_random_color()
        self.center_color = YELLOW_COLOR
        self.stem_color = DARK_GREEN_COLOR

    def draw(self, screen):
        pygame.draw.rect(screen, self.petal_color, (self.x, 427, 10, 10))
        pygame.draw.rect(screen, self.petal_color, (self.x - 10, 417, 10, 10))
        pygame.draw.rect(screen, self.petal_color, (self.x - 10, 437, 10, 10))
        pygame.draw.rect(screen, self.petal_color, (self.x - 20, 427, 10, 10))
        pygame.draw.rect(screen, self.center_color, (self.x - 10, 427, 10, 10))
        pygame.draw.rect(screen, self.stem_color, (self.x - 7, 447, 4, 40))


# Tree
class Tree(SceneElement):
    def __init__(self, x, y, tree_size):
        SceneElement.__init__(self, x, y)

        self.tree_size = tree_size
        self.wood_color = BROWN_COLOR
        self.leave_color = GREEN_COLOR

    def draw(self, screen):
        a=0
        # TODO: add implementation


# Patch of grass.
class Grass(SceneElement):
    def __init__(self, x, y,
                 max_grass_height,
                 min_grass_height,
                 num_of_stalks,
                 grass_color):
        SceneElement.__init__(self, x, y)

        self.max_grass_height = max_grass_height
        self.least_grass_height = min_grass_height
        self.num_of_stalks = num_of_stalks
        self.grass_color = grass_color

    # Gets the list of all pre-created grass stalks.
    def get_stalks(self):
        return []  # TODO


class Rocket(SceneElement):
    def __init__(self, x, y):
        SceneElement.__init__(self, x, y)

        self.frame_cnt = 0
        self.color = mk_random_color()


class Explosion:
    def __init__(self, frags):
        self.frags = frags

    def is_done(self):
        return self.frags[0].frame_cnt == 30


class AirFragment(SceneElement):
    def __init__(self, x, y):
        SceneElement.__init__(self, x, y)

        self.speed = random.randint(2, 4)  # Speed in pixels per frame.
        self.angle = random.randint(0, 360)  # Angle of movement.
        self.turn_angle = random.randint(0, 360)  # Angle of turning.
        self.frame_cnt = 0
        self.size = random.randint(3, 10)  # Size of the square in pixels.


class GroundFragment(SceneElement):
    def __init__(self, x, y, brick_kind):
        SceneElement.__init__(self, x, y)

        if brick_kind == 1:
            self.color = RED_COLOR
        elif brick_kind == 2:
            self.color = WHITE_COLOR
        else:  # kind == 3
            self.color = GREEN_COLOR

        self.speed = random.randint(2, 4)  # Speed in pixels per frame.
        self.angle = random.randint(10, 170)  # Angle of movement.
        self.turn_angle = random.randint(0, 360)  # Angle of turning.
        self.frame_cnt = 0
        self.size = random.randint(3, 10)  # Size of the square in pixels.
