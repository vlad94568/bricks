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


from src.common import *


# Definition of a single level.
class Level:
    def __init__(self,
                 lvl_num,  # E.g. 1
                 bg_color,
                 player_color,
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
        self.player_color = player_color
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
        self.player_x = screen_width / 2
        self.rockets = []

    # Gets level complete percentage.
    def level_complete(self):
        return 0

    # Adds new rocket.
    def add_rocket(self, rocket):
        # Add new rocket.
        self.rockets.append(rocket)
