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


# Tree.
class Tree(SceneElement):
    def __init__(self, x, y, tree_size):
        SceneElement.__init__(self, x, y)

        self.tree_size = tree_size
        self.wood_color = BROWN_COLOR
        self.leave_color = GREEN_COLOR

    # Draws this tree.
    def draw(self, screen):
        ()
        # TODO
