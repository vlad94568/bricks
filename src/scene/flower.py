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

        self.stem_height = random.randint(40,80)
        self.petal_color = mk_random_color()
        self.center_color = YELLOW_COLOR
        self.stem_color = DARK_GREEN_COLOR

    def draw(self, screen):
        # Drawing petals.
        pygame.draw.rect(screen, self.petal_color, (self.x, 427 - self.stem_height + 10, 10, 10))
        pygame.draw.rect(screen, self.petal_color, (self.x - 10, 417 - self.stem_height + 10, 10, 10))
        pygame.draw.rect(screen, self.petal_color, (self.x - 10, 437 - self.stem_height + 10, 10, 10))
        pygame.draw.rect(screen, self.petal_color, (self.x - 20, 427 - self.stem_height + 10, 10, 10))
        # Drawing center of flower.
        pygame.draw.rect(screen, self.center_color, (self.x - 10, 427 - self.stem_height + 10, 10, 10))
        # Drawing stem.
        pygame.draw.rect(screen, self.stem_color, (self.x - 7, 447 - self.stem_height + 10, 4, self.stem_height + 10))
        # Drawing leaves.
        pygame.draw.rect(screen, self.stem_color, (self.x - 17, 425 + (self.stem_height % 2), 23, 8))

