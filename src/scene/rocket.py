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


# Fired rocket.
class Rocket(SceneElement):
    def __init__(self, x, y):
        SceneElement.__init__(self, x, y)

        self.color = mk_random_color()
        self.draw_count = 0

    # Draws the rocket.
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 5, 8), 1)

        self.draw_count = self.draw_count + 1

        if self.draw_count % 3 == 0:
            self.color = mk_random_color()
