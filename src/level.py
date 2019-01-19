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


from src.scene.brick import *


# Definition of a single level.
class Level:
    def __init__(self,
                 lvl_num,  # E.g. 1
                 bg_color,
                 player_color,
                 bg_sound,
                 num_red_bricks,  # Total number of red bricks to be dropped at this level.
                 num_green_bricks,  # Total number of green bricks to be dropped at this level.
                 num_white_bricks,  # Total number of white bricks to be dropped at this level.
                 red_bricks_max_speed,  # Speed is in pixels per frame.
                 red_bricks_min_speed,  # Speed is in pixels per frame.
                 green_bricks_max_speed,  # Speed is in pixels per frame.
                 green_bricks_min_speed,  # Speed is in pixels per frame.
                 white_bricks_max_speed,  # Speed is in pixels per frame.
                 white_bricks_min_speed,  # Speed is in pixels per frame.
                 max_bricks_on_screen,  # Max number of bricks on the screen in the same time.
                 scene_elements  # List of different scene elements for this level world.
                 ):
        self.lvl_num = lvl_num
        self.player_color = player_color
        self.max_bricks_on_screen = max_bricks_on_screen
        self.bg_color = bg_color
        self.bg_sound = bg_sound
        self.num_red_bricks = num_red_bricks
        self.num_green_bricks = num_green_bricks
        self.num_white_bricks = num_white_bricks
        self.scene_elements = scene_elements
        self.red_bricks_max_speed = red_bricks_max_speed
        self.red_bricks_min_speed = red_bricks_min_speed
        self.green_bricks_max_speed = green_bricks_max_speed
        self.green_bricks_min_speed = green_bricks_min_speed
        self.white_bricks_max_speed = white_bricks_max_speed
        self.white_bricks_min_speed = white_bricks_min_speed
        self.rockets = []
        self.bricks = []
        self.explosions = []

        self.total_bricks = num_red_bricks + num_green_bricks + num_white_bricks
        self.used_bricks = 0
        self.level_completion = 0

    def reset_data(self):
        self.rockets = []
        self.bricks = []
        self.explosions = []
        self.used_bricks = 0
        self.level_completion = 0

    # Adds, if necessary, a new random brick.
    def add_new_bricks(self):
        # Randomly place bricks, if necessary.
        if len(self.bricks) < self.max_bricks_on_screen:
            brick_x = random.randint(20, 620)

            rnd = random.randint(0, 100)

            if rnd < 10:
                kind = 3
                speed = random.randint(self.green_bricks_min_speed, self.green_bricks_max_speed)
            elif rnd < 35:
                kind = 2
                speed = random.randint(self.white_bricks_min_speed, self.white_bricks_max_speed)
            else:
                kind = 1
                speed = random.randint(self.red_bricks_min_speed, self.red_bricks_max_speed)

            self.bricks.append(Brick(brick_x, 0, speed, kind))

    # Filters and returns the array of all still active rockets (to draw).
    def get_active_rockets(self):
        self.rockets[:] = [rocket for rocket in self.rockets if rocket.y > 5]

        return self.rockets

    # Moves all active rockets up.
    def move_up_rockets(self):
        for rocket in self.rockets:
            rocket.y -= 6

    # Adds new rocket.
    def add_rocket(self, rocket):
        # Add new rocket.
        self.rockets.append(rocket)
