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


# Simple (rectangular) ground.
class SimpleGround(SceneElement):
    def __init__(self, height, color):
        SceneElement.__init__(self, 0, screen_height - height)

        self.height = height
        self.color = color

    # Draws ground.
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, screen_width, self.height))
