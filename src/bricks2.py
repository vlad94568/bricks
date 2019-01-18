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
import time
from pygame import gfxdraw

# Initialize pygame & its modules.
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.joystick.init()

# Import all scene elements.
from src.common import *
from src.levels import *
from src.scene.star import *
from src.scene.brick import *
from src.scene.flower import *
from src.scene.rocket import *
from src.scene.grass import *
from src.scene.tree import *

from src.sound_mixer import *

# Window title.
pygame.display.set_caption("--==B.R.I.C.K.S==--")

# Sounds.
bg_sound_1 = pygame.mixer.Sound("sounds/background_sound0.1.ogg")
title_bg_sound = pygame.mixer.Sound("sounds/background_sound1.ogg")
final_bg_sound = pygame.mixer.Sound("sounds/background_sound2.ogg")


# Grabbing fonts from 'fonts' sub-folder to be 100% cross-platform compatible.
header_font = pygame.font.Font("fonts/Anonymous.ttf", 13)
title_font = pygame.font.Font("fonts/Anonymous.ttf", 13)
ver_font = pygame.font.Font("fonts/Anonymous.ttf", 10)
final_font1 = pygame.font.Font("fonts/Anonymous.ttf", 13)
final_font2 = pygame.font.Font("fonts/Anonymous.ttf", 16)
level_font = pygame.font.Font("fonts/Anonymous.ttf", 16)

# Game.
game = Game(
    20,  # Initial number of lives given to the user.
    20,  # Initial ammo amount.
    title_bg_sound,
    final_bg_sound,
    [
        game_lvl1
    ]
)

# Soundtrack mixer.
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
    pygame.quit()
    sys.exit()


# Draws the game's title.
def draw_title():
    ascii_name = [
        "    _/_/_/    _/_/_/    _/_/_/    _/_/_/  _/    _/    _/_/_/",
        "   _/    _/  _/    _/    _/    _/        _/  _/    _/",
        "  _/_/_/    _/_/_/      _/    _/        _/_/        _/_/",
        " _/    _/  _/    _/    _/    _/        _/  _/          _/",
        "_/_/_/    _/    _/  _/_/_/    _/_/_/  _/    _/  _/_/_/"
    ]

    x = 50
    y = 50

    game.screen.fill(SLACK_COLOR)

    # Shortcut function.
    def pri(s, s_x, s_y, color=YELLOW_COLOR, font=title_font):
        game.screen.blit(font.render(s, 1, color), (s_x, s_y))

    for line in ascii_name:
        pri(line, x, y, mk_random_color())
        y += 15

    pri("--== Copyright 2018-2019 (C) by Vlad Ivanov ==--", 105, 150)
    pri("ver. 2.0.0", 270, 170, font=ver_font)

    x2 = 260
    y2 = 225

    Brick(x2, y2, 0, 1).draw(game.screen)
    pri("+1 score", x2 + 30, y2)

    y2 += 20

    Brick(x2, y2, 0, 2).draw(game.screen)
    pri("+5 ammo", x2 + 30, y2)

    y2 += 20

    Brick(x2, y2, 0, 3).draw(game.screen)
    pri("+1 live", x2 + 30, y2)

    pri("SPACE to shoot | ARROW KEYS to move", 150, 330)

    if game.is_joystick_found:
        pri("Supported joystick found", 200, 370)

    pri("Press ENTER to start", 220, 410)

    # Start title background music.
    mixer.background_sound(game.title_sound)

    # Update (refresh) screen.
    pygame.display.update()

    wait_key_pressed(pygame.K_RETURN)


# Draw score, live and ammo.
def draw_header(lvl):
    score_label = header_font.render("score: " + str(game.score), 1, RED2_COLOR)
    lives_label = header_font.render("lives: " + str(game.lives), 1, GREEN_COLOR)
    ammo_label = header_font.render("ammo: " + str(game.ammo), 1, WHITE_COLOR)
    level_label = header_font.render("level: " + str(lvl.level_complete()) + "%", 1, YELLOW_COLOR)

    game.screen.blit(score_label, (70, 10))
    game.screen.blit(lives_label, (210, 10))
    game.screen.blit(ammo_label, (350, 10))
    game.screen.blit(level_label, (480, 10))


# Animations to switch to a given level.
def switch_to_level(lvl):
    mixer.fadeout_all()

    ani = True

    x = screen_width / 2 - 2
    y = screen_height / 2 - 2
    w = 4
    h = 4

    # Slow growing black rectangle.
    while ani:
        pygame.draw.rect(game.screen, DARK_GREY_COLOR, (x, y, w, h))

        w += 30  # Grow faster horizontally since screen isn't perfect square.
        h += 20
        x -= 15  # Grow faster horizontally since screen isn't perfect square.
        y -= 10

        # Quite loop when rectangle covers all screen.
        if w > screen_width and h > screen_height:
            ani = False

        pygame.event.get()
        pygame.display.update()

        game.tick_clock()

    # Draw level number.
    game.screen.fill(DARK_GREY_COLOR)
    game.screen.blit(level_font.render("--== level " + str(lvl.lvl_num) + " ==--", 1, DARK_GREEN_COLOR), (220, 210))

    pygame.display.update()
    pygame.event.get()

    # Sleep for 3 seconds.
    time.sleep(3)


# Plays given level.
def play_level(lvl):
    mixer.background_sound(lvl.bg_sound)

    scr = game.screen

    intro_ani = True

    x = 0
    y = 0
    w = screen_width
    h = screen_height

    # Intro-animation: shrinking black rectangle.
    while intro_ani:
        # Clear the screen.
        scr.fill(lvl.bg_color)

        # Draw the scene elements.
        for scene_elem in lvl.scene_elements:
            scene_elem.draw(scr)

        draw_header(lvl)

        pygame.draw.rect(scr, DARK_GREY_COLOR, (x, y, w, h))

        w -= 30  # Shrink faster horizontally since screen isn't perfect square.
        h -= 20
        x += 15  # Shrink faster horizontally since screen isn't perfect square.
        y += 10

        # Quite loop when rectangle covers all screen.
        if w <= 0 and h <= 0:
            intro_ani = False

        pygame.event.get()
        pygame.display.update()

        game.tick_clock()

    left = 0
    right = 0

    # Main level loop.
    while True:
        if game.lives == 0 or game.ammo == 0:
            game_over = True
        else:
            game_over = False

        if game_over:
            # Fade out all sounds.
            mixer.fadeout_all()

            # Clear data.
            game.clear_data()

            # Draw final score.
            end_it = draw_final_score()

            if end_it:
                # End the game.
                end_game()
            else:
                ()  # TODO
        else:
            # Clear the screen.
            scr.fill(lvl.bg_color)

            # Draw the scene elements.
            for scene_elem in lvl.scene_elements:
                scene_elem.draw(scr)

            for event in pygame.event.get():
                typ = event.type

                if typ == pygame.QUIT:
                    end_game()
                elif typ == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # Fire the rocket using last 'playerX'.
                    fire_rocket(player_x + 7)
                elif typ == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    # Move the player left.
                    left = 1
                    right = 0
                elif typ == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    # Move the player right.
                    right = 1
                    left = 0
                elif typ == pygame.KEYUP and event.key == pygame.K_LEFT:
                    # Stop left movement.
                    left = 0
                elif typ == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    # Stop right movement.
                    right = 0

            if left == 1:
                game.move_player_left()
            elif right == 1:
                game.move_player_right()

            draw_header(lvl)
            game.draw_player(lvl)

            # Update (refresh) screen.
            pygame.display.update()

            # Wait for FPS.
            game.tick_clock()


def main_game_loop():
    for lvl in game.levels:
        switch_to_level(lvl)
        play_level(lvl)


draw_title()
main_game_loop()

