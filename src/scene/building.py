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


class Building(SceneElement):
    # Rows - how many rows of windows.
    # Rooms - how many windows at each row.
    def __init__(self, x, build_col, win_col, floors, rows, party_on):
        SceneElement.__init__(self, x, screen_height)

        self.build_col = build_col
        self.win_col = win_col
        self.rows = rows
        self.floors = floors
        self.party_on = party_on
        self.width = (rows * 2 + 1) * 10
        self.height = (floors - 1) * 5 + floors * 10 + 20
        self.row_start_y = self.y - self.height

    def draw_window(self, screen, x, y):
        if self.party_on:
            color = mk_random_color()
        else:
            color = self.win_col

        pygame.draw.rect(screen, color, (x, y, 10, 10))
        pygame.draw.line(screen, BLACK_COLOR, [x + 4, y], [x + 4, y + 10])
        pygame.draw.line(screen, BLACK_COLOR, [x, y + 5], [x + 10, y + 5])
        pygame.draw.rect(screen, BLACK_COLOR, (x, y, 10, 10), 1)

    def draw_row(self, screen, x):
        win_y = self.row_start_y

        for a in range(0, self.floors):
            self.draw_window(screen, x, win_y)
            win_y = win_y + 10 + 5

    def draw(self, screen):
        # Drawing the core of the building.
        pygame.draw.rect(
            screen,
            self.build_col,
            (
                    self.x,
                    self.y - 10 - self.height,
                    self.width,
                    self.height
            )
        )

        row_x = self.x + 10

        # Drawing all the windows.
        for r in range(0, self.rows):
            self.draw_row(screen, row_x)
            row_x = row_x + 10 + 10


