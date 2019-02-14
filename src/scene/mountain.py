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


# Mountain.
class Mountain(SceneElement):
    def __init__(self, x, w, h, base_col, top_col):
        SceneElement.__init__(self, x, screen_height)

        self.w = w
        self.h = h
        self.base_col = base_col
        self.top_col = top_col

    # Draws this Mountain.
    def draw(self, screen):
        pygame.draw.polygon(screen, self.base_col,[self.x,screen_height - 10],[self.x])
