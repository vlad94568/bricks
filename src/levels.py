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

# Import all scene elements.
from src.scene.flower import *
from src.scene.simple_ground import *

game_lvl1 = Level(
    1,
    DARK_BLUE_COLOR,
    pygame.mixer.Sound("sounds/background_sound0.1.ogg"),
    num_red_bricks=20,
    num_green_bricks=20,
    num_white_bricks=5,
    red_bricks_max_speed=4,
    red_bricks_min_speed=1,
    green_bricks_max_speed=4,
    green_bricks_min_speed=4,
    white_bricks_max_speed=2,
    white_bricks_min_speed=2,
    scene_elements=[
        SimpleGround(10, DARK_GREEN_COLOR),
        Flower(50, 40, 60),
        Flower(250, 40, 80),
        Flower(350, 50, 50),
        Flower(550, 40, 40)
    ]
)