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


from src.basics import *


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
