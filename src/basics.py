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
    def __init__(self, x, y, stem_height, petal_color, center_color):
        SceneElement.__init__(self, x, y)

        self.stem_height = stem_height
        self.petal_color = petal_color
        self.center_color = center_color


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