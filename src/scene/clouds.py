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


class Clouds(SceneElement):
    def __init__(self, x, y):
        SceneElement.__init__(self, x, y)

        self.frame = 0
        self.xx = x

    # Draws the clouds.
    def draw(self, screen):
        if self.frame == 2:
            self.frame = 0
            self.xx += 1

        pygame.draw.circle(
            screen,
            CLOUD_COLOR,
            (
                self.xx,
                self.y
            ),
            20
        )
        pygame.draw.circle(
            screen,
            GREY_COLOR,
            (
                self.xx,
                self.y
            ),
            20,
            1
        )

        pygame.draw.circle(
            screen,
            CLOUD_COLOR,
            (
                self.xx + 20,
                self.y + 10
            ),
            20
        )
        pygame.draw.circle(
            screen,
            GREY_COLOR,
            (
                self.xx + 20,
                self.y + 10
            ),
            20,
            1
        )

        pygame.draw.circle(
            screen,
            CLOUD_COLOR,
            (
                self.xx + 30,
                self.y - 10
            ),
            20
        )

        self.frame += 1

