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
    def __init__(self, y, mounain_size):
        SceneElement.__init__(self, x, y)

        self.mountain_size = mounain_size
        self.mountain_color = DARK_GREY_COLOR
        self.snow_color = WHITE_COLOR

    # Draws this Mountain.
    def draw(self, screen):
        pygame.draw.polygon(screen, self.mountain_color,[10,self.y],[])
        # TODO
