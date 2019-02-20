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
        alpha = math.acos(self.w / 2 / math.sqrt(math.pow(self.w / 2, 2) + math.pow(self.h, 2)))

        w_prime = math.tan(alpha) * 2 / 3 * self.h

        x_delta = (self.w / 2 - w_prime) / 2

        print(x_delta)

        # Point #0
        x0 = self.x
        y0 = self.y - 10

        # Point #1
        x1 = self.x + w_prime
        y1 = self.y - self.h * 2 / 3

        # Point #2
        x2 = x1 + x_delta
        y2 = y1 + 10

        # Point #3
        x3 = x2 + x_delta
        y3 = y1

        # Point #4
        x4 = x3 + x_delta
        y4 = y1 + 10

        # Point #5
        x5 = x4 + x_delta
        y5 = y1

        # Point #6
        x6 = self.x + self.w
        y6 = y0

        # Point #7
        x7 = self.x + self.w / 2
        y7 = self.y - self.h

        list1 = [x0, y0], [x7, y7], [x6, y6]
        list2 = [x0, y0], [x1, y1], [x2, y2], [x3, y3], [x4, y4], [x5, y5], [x6, y6],

        pygame.draw.polygon(screen, self.top_col, list1)
        pygame.draw.polygon(screen, self.base_col,list2)
