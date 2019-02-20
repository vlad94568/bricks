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


# Tree.
class Tree(SceneElement):
    def __init__(self, x, branch_height, branch_width, wood_color, leaf_color):
        SceneElement.__init__(self, x, screen_height)

        self.branch_height = branch_height
        self.branch_width = branch_width
        self.leaf_size = branch_width * 2
        self.wood_color = wood_color
        self.leaf_color = leaf_color

    # Draws the wood part of the tree.
    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.wood_color,
            (
                self.x,
                screen_height - 10 - self.branch_height,
                self.branch_width,
                self.branch_height
            )
        )
        # Draws the first leaf.
        pygame.draw.circle(
            screen,
            self.leaf_color,
            (
                self.x,
                screen_height - 10 - self.branch_height
            ),
            self.leaf_size
        )
        # Draws the second leaf.
        pygame.draw.circle(
            screen,
            self.leaf_color,
            (
                round(self.x + (self.branch_width / 2)),
                screen_height - 30 - self.branch_height
            ),
            self.leaf_size
        )

# Draws the third leaf.
        pygame.draw.circle(
            screen,
            self.leaf_color,
            (
                self.x + self.branch_width,
                screen_height - 10 - self.branch_height
            ),
            self.leaf_size
        )
