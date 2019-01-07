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

import math
import sys
import pygame
from pygame import gfxdraw

# Import all scene elements.
from src.common import *
from src.scene.star import *
from src.scene.brick import *
from src.scene.flower import *
from src.scene.rocket import *
from src.scene.grass import *
from src.scene.tree import *

from src.sound_mixer import *

# Initialize pygame & its modules.
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.joystick.init()

# Sounds.
bg_sound_1 = pygame.mixer.Sound("sounds/background_sound0.1.ogg")
title_bg_sound = pygame.mixer.Sound("sounds/background_sound1.ogg")
final_bg_sound = pygame.mixer.Sound("sounds/background_sound2.ogg")


# Grabbing fonts from 'fonts' sub-folder to be 100% cross-platform compatible.
header_font = pygame.font.Font("fonts/Anonymous.ttf", 13)
title_font = pygame.font.Font("fonts/Anonymous.ttf", 13)
final_font1 = pygame.font.Font("fonts/Anonymous.ttf", 13)
final_font2 = pygame.font.Font("fonts/Anonymous.ttf", 16)

# Game.
game = Game(
    20,  # Initial number of lives given to the user.
    title_bg_sound,
    final_bg_sound
)

mixer = SoundMixer()


# Waits until given keyboard key is pressed.
def wait_key_pressed(key):
    is_pressed = False

    while not is_pressed:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                end_game()
            elif evt.type == pygame.KEYDOWN and evt.key == key:
                is_pressed = True


def end_game():
    ()


# Draws the game's title.
def draw_title():
    name = [
        "    _/_/_/    _/_/_/    _/_/_/    _/_/_/  _/    _/    _/_/_/",
        "   _/    _/  _/    _/    _/    _/        _/  _/    _/",
        "  _/_/_/    _/_/_/      _/    _/        _/_/        _/_/",
        " _/    _/  _/    _/    _/    _/        _/  _/          _/",
        "_/_/_/    _/    _/  _/_/_/    _/_/_/  _/    _/  _/_/_/"
    ]

    x = 50
    y = 50

    game.screen.fill(SLACK_COLOR)

    for line in name:
        game.screen.blit(title_font.render(line, 1, mk_random_color()), (x, y))
        y += 15

        game.screen.blit(title_font.render("--== Copyright 2018 (C) by Vlad Ivanov ==--", 1, YELLOW_COLOR), (115, 150))

    x2 = 260
    y2 = 225

    Brick(x2, y2, 0, 1).draw(game.screen)
    game.screen.blit(title_font.render("+1 score", 1, YELLOW_COLOR), (x2 + 30, y2))

    y2 += 20

    Brick(x2, y2, 0, 2).draw(game.screen)
    game.screen.blit(title_font.render("+5 ammo", 1, YELLOW_COLOR), (x2 + 30, y2))

    y2 += 20

    Brick(x2, y2, 0, 3).draw(game.screen)
    game.screen.blit(title_font.render("+1 live", 1, YELLOW_COLOR), (x2 + 30, y2))

    game.screen.blit(title_font.render("SPACE to shoot | ARROW KEYS to move", 1, YELLOW_COLOR), (150, 330))

    if game.is_joystick_found:
        game.screen.blit(title_font.render("Supported joystick found", 1, YELLOW_COLOR), (200, 370))

    game.screen.blit(title_font.render("Press ENTER to start", 1, WHITE_COLOR), (220, 410))

    # Start title background music.
    mixer.background_sound(game.title_sound)

    # Update (refresh) screen.
    pygame.display.update()

    wait_key_pressed(pygame.K_RETURN)


def main_game_loop():
    ()

# +=================+
# | Start the game. |
# +=================+
draw_title()
main_game_loop()

