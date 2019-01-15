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


class Flower(SceneElement):
    def __init__(self, x, min_stem_height=40, max_stem_height=60):
        SceneElement.__init__(self, x, screen_height)

        self.stem_height = random.randint(min_stem_height, max_stem_height)
        self.petal_color = mk_random_color()
        self.center_color = YELLOW_COLOR
        self.stem_color = DARK_GREEN_COLOR

    def draw(self, screen):
        # Drawing stem.
        pygame.draw.rect(screen, self.stem_color, (self.x - 7, screen_height - self.stem_height, 4, self.stem_height))
        # Drawing petals.
        pygame.draw.rect(screen, self.petal_color, (self.x, screen_height - self.stem_height - 10, 10, 10))
        pygame.draw.rect(screen, self.petal_color, (self.x - 10, screen_height - self.stem_height - 20, 10, 10))
        pygame.draw.rect(screen, self.petal_color, (self.x - 10, screen_height - self.stem_height, 10, 10))
        pygame.draw.rect(screen, self.petal_color, (self.x - 20, screen_height - self.stem_height - 10, 10, 10))
        # Drawing center of flower.
        pygame.draw.rect(screen, self.center_color, (self.x - 10, screen_height - self.stem_height - 10, 10, 10))
        # Drawing leaves.
        pygame.draw.rect(screen, self.stem_color, (self.x - 12, screen_height - (self.stem_height - 15), 7, 5))
        pygame.draw.rect(screen, self.stem_color, (self.x - 4, screen_height - (self.stem_height - 20), 7, 5))

