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


# Explosion air fragment.
class AirFragment(SceneElement):
    def __init__(self, x, y):
        SceneElement.__init__(self, x, y)

        self.speed = random.randint(2, 4)  # Speed in pixels per frame.
        self.angle = random.randint(0, 360)  # Angle of movement.
        self.turn_angle = random.randint(0, 360)  # Angle of turning.
        self.frame_cnt = 0
        self.size = random.randint(3, 10)  # Size of the square in pixels.

    # Draws fragment.
    def draw(self, screen):
        draw_turned_square(self.x, self.y, self.size, mk_random_color(), self.turn_angle, screen)

        self.turn_angle += self.speed + 10
        self.frame_cnt += 1

        self.x, self.y = transform(self.x, self.y, self.speed, self.angle)
