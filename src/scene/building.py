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


class Building(SceneElement):
    # rows - how many rows of windows
    # floors - how many windows at each rows
    def __init__(self, x, rows, floors):
        SceneElement.__init__(self, x, screen_height)

        self.rows = rows
        self.floors = floors

    # Draw building.
    def draw(self, screen):
        # TODO
        pass

