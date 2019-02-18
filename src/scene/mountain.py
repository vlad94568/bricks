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

        point_list_1 = [self.x, screen_height - 10],\
                     [(self.w / 2) + self.x , screen_height - 10 - self.h],\
                     [self.x + self.w,screen_height - 10 ]


        point_list_2 = [self.x, screen_height - 10],\
                       [(self.w / 2) + self.x - 30,screen_height - 10 - self.h + 90 ],\
                       [(self.w / 2) + self.x + 30, screen_height - 10 - self.h + 90], \
                       [self.x + self.w, screen_height - 10]

        pygame.draw.polygon(screen, self.top_col, point_list_1)
        #pygame.draw.polygon(screen, self.base_col,point_list_2)
