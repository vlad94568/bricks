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


# Sparkling star.
class Star(SceneElement):
    # Initializes this star.
    def __init__(self, x, y,
                 star_color,
                 max_size):
        SceneElement.__init__(self, x, y)

        self.curr_sparkle_size = 0
        self.star_color = star_color
        self.max_size = max_size

    # Draws this star.
    def draw(self, screen):
        s1 = self.max_size * 1.5

        #
        # Main lines.
        #
        pygame.draw.line(
            screen,
            self.star_color,
            (self.x, self.y + s1),
            (self.x, self.y - s1)
        )
        pygame.draw.line(
            screen,
            self.star_color,
            (self.x - s1, self.y),
            (self.x + s1, self.y)
        )

        #
        # Sparkle lines.
        #
        pygame.draw.line(
            screen,
            mk_random_color(),
            (self.x + self.curr_sparkle_size, self.y + self.curr_sparkle_size),
            (self.x - self.curr_sparkle_size, self.y - self.curr_sparkle_size)
        )
        pygame.draw.line(
            screen,
            mk_random_color(),
            (self.x + self.curr_sparkle_size, self.y - self.curr_sparkle_size),
            (self.x - self.curr_sparkle_size, self.y + self.curr_sparkle_size)
        )

        if self.curr_sparkle_size > self.max_size:
            self.curr_sparkle_size = 0
        else:
            self.curr_sparkle_size = self.curr_sparkle_size + 0.4

