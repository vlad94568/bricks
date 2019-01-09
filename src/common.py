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
    # Start with 32 to make sure that random colors are minimally bright.
    r = random.randint(32, 255)
    g = random.randint(32, 255)
    b = random.randint(32, 255)

    return r, g, b


# Base class for all scene elements.
class SceneElement:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Definition of a single level.
class Level:
    def __init__(self,
                 lvl_num,  # E.g. 1
                 lvl_name,  # E.g. "Tokyo" or "Moscow"
                 bg_color,
                 bg_sound,
                 num_red_bricks,  # Total number of red bricks to be dropped at this level.
                 num_green_bricks,  # Total number of green bricks to be dropped at this level.
                 num_white_bricks,  # Total number of white bricks to be dropped at this level.
                 red_bricks_max_speed,  # Speed is in pixels per frame.
                 red_bricks_min_speed,  # Speed is in pixels per frame.
                 green_bricks_max_speed,  # Speed is in pixels per frame.
                 green_bricks_min_speed,  # Speed is in pixels per frame.
                 white_bricks_max_speed,  # Speed is in pixels per frame.
                 white_bricks_min_speed,  # Speed is in pixels per frame.
                 scene_elements  # List of different scene elements for this level world.
                 ):
        self.lvl_num = lvl_num
        self.lvl_name = lvl_name
        self.bg_color = bg_color
        self.bg_sound = bg_sound
        self.num_red_bricks = num_red_bricks
        self.num_green_bricks = num_green_bricks
        self.num_white_bricks = num_white_bricks
        self.scene_elements = scene_elements
        self.red_bricks_max_speed = red_bricks_max_speed
        self.red_bricks_min_speed = red_bricks_min_speed
        self.green_bricks_max_speed = green_bricks_max_speed
        self.green_bricks_min_speed = green_bricks_min_speed
        self.white_bricks_max_speed = white_bricks_max_speed
        self.white_bricks_min_speed = white_bricks_min_speed


# Global game data holder.
class Game:
    def __init__(self,
                 init_lives,
                 title_sound,
                 end_sound,
                 levels
                 ):
        self.score = 0
        self.lives = init_lives
        self.is_joystick_found = self.detect_joystick()
        self.title_sound = title_sound
        self.end_sound = end_sound
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.levels = levels
        self.lvl_idx = 0

    # Detects if supported joystick is found.
    @staticmethod
    def detect_joystick():
        is_joystick_found = False

        joystick_count = pygame.joystick.get_count()

        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            # Get the name from the OS for the controller/joystick
            name = joystick.get_name()

            if name.startswith("USB,2-axis 8-button gamepad"):
                is_joystick_found = True

        return is_joystick_found


# TODO: refactor
class Explosion:
    def __init__(self, frags):
        self.frags = frags

    def is_done(self):
        return self.frags[0].frame_cnt == 30


# TODO: refactor
class AirFragment(SceneElement):
    def __init__(self, x, y):
        SceneElement.__init__(self, x, y)

        self.speed = random.randint(2, 4)  # Speed in pixels per frame.
        self.angle = random.randint(0, 360)  # Angle of movement.
        self.turn_angle = random.randint(0, 360)  # Angle of turning.
        self.frame_cnt = 0
        self.size = random.randint(3, 10)  # Size of the square in pixels.


# TODO: refactor
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
