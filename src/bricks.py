#
#      _/_/_/    _/_/_/    _/_/_/    _/_/_/  _/    _/    _/_/_/
#     _/    _/  _/    _/    _/    _/        _/  _/    _/
#    _/_/_/    _/_/_/      _/    _/        _/_/        _/_/
#   _/    _/  _/    _/    _/    _/        _/  _/          _/
#  _/_/_/    _/    _/  _/_/_/    _/_/_/  _/    _/  _/_/_/
#
#  By Vlad Ivanov, 2018.
#  Email: vlad94568@gmail.com

import pygame
import random
import sys


class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Brick:
    # kinds:
    # 1 - normal brick (RED)
    # 2 - ammo brick (WHITE)
    # 3 - live break (GREEN)
    def __init__(self, x, y, speed, kind):
        self.x = x
        self.y = y
        self.speed = speed
        self.kind = kind

        self.state = 1  # 1 - falling (normal), 2 - explosion
        self.frameCnt = 0
        self.x_adj = 0


RED_COLOR = (255, 0, 0)
GREEN_COLOR = (0, 255, 0)
WHITE_COLOR = (255, 255, 255)
YELLOW_COLOR = (255, 255, 0)
BLACK_COLOR = (0, 0, 0)

START_ROCKET_Y = 450
START_BRICK_Y = 0

FPS = 30
score = 0
lives = 20
ammo = 100
playerX = 0
click=0
rockets = []
bricks = []

# Initialize the game & modules.
pygame.init()
pygame.mixer.init()
pygame.font.init()

bg_sound = pygame.mixer.Sound("sounds/background_sound.ogg")

# Pygame initialization.
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Grabbing fonts from 'fonts' sub-folder to be 100% cross-platform compatible.
headerFont = pygame.font.Font("fonts/Anonymous.ttf", 13)
title_font = pygame.font.Font("fonts/Anonymous.ttf", 13)
final_font1 = pygame.font.Font("fonts/Anonymous.ttf", 13)
final_font2 = pygame.font.Font("fonts/Anonymous.ttf", 16)
pygame.display.set_caption("--==B.R.I.C.K.S==--")


def boom_sound():
    # pygame.mixer.music.load("sounds/0342.ogg")
    # pygame.mixer.music.play()
    pass


def squish_sound():
    # pygame.mixer.music.load("sounds/0342.ogg")
    # pygame.mixer.music.play()
    pass


# Generate random color.
def mk_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


# Draws the player at 'playerX' coordinate.
def draw_player():
    if ammo > 0:
        player_color = GREEN_COLOR
    else:
        player_color = WHITE_COLOR

    pygame.draw.rect(screen, player_color, (playerX, 450, 20, 20), 5) # Base.
    pygame.draw.line(screen, player_color, [playerX + 9, 450], [playerX + 9, 435], 5) # Turret.


# Draws all the rockets in 'rockets' list.
def draw_rockets():
    for rocket in rockets:
        pygame.draw.rect(screen, mk_random_color(), (rocket.x, rocket.y, 5, 8), 1)

        rocket.y -= 6

        if rocket.y < 0:
            rockets.remove(rocket)


def draw_brick(x, y, color):
    pygame.draw.rect(screen, color, (x, y, 15, 10), 3)


# Draws all the bricks in 'bricks' list.
def draw_bricks():
    global lives
    global ammo

    for brick in bricks:
        if brick.kind == 1:
            draw_brick(brick.x, brick.y, RED_COLOR)
        elif brick.kind == 2:
            draw_brick(brick.x, brick.y, WHITE_COLOR)
        else: # kind == 3
            draw_brick(brick.x, brick.y, GREEN_COLOR)

        brick.frameCnt += 1

        if brick.y >= 480:
            # Bricks reached the bottom.
            lives -= 1
            bricks.remove(brick)
            squish_sound()
        else:
            # Move white brick left or right (change direction every 15 frames, i.e. every second).
            if brick.kind == 2 and brick.frameCnt % 15 == 0:
                if random.randint(0, 100) > 50:
                    brick.x_adj = brick.speed
                else:
                    brick.x_adj = -brick.speed

            # Brick is still falling down.
            brick.y += brick.speed
            brick.x += brick.x_adj


# Checking for a crash with the rocket and brick.
def check_bricks_rockets():
    global score, ammo, lives

    for brick in bricks:
        for rocket in rockets:
            if brick.x - 5 <= rocket.x <= brick.x + 15 and rocket.y <= brick.y:
                # Hide/remove brick and the rocket that killed it.
                rockets.remove(rocket)
                bricks.remove(brick)
                boom_sound()
                if brick.kind == 1: # RED brick.
                    # Add score for normal killed brick.
                    score = score + 1
                elif brick.kind == 2: # WHITE brick.
                    # Add ammo.
                    ammo += 20
                elif brick.kind == 3: # GREEN brick.
                    # Add lives.
                    lives += 3


# Draw score, live and ammo.
def draw_header():
    score_label = headerFont.render("score: " + str(score), 1, YELLOW_COLOR)
    lives_label = headerFont.render("lives: " + str(lives), 1, YELLOW_COLOR)
    ammo_label = headerFont.render("ammo: " + str(ammo), 1, YELLOW_COLOR)

    screen.blit(score_label, (10, 10))
    screen.blit(lives_label, (150, 10))
    screen.blit(ammo_label, (290, 10))


# Ends the game.
def end_game():
    pygame.quit()
    sys.exit()


def fire_rocket(x):
    global ammo

    # Add new rocket using last 'playerX'.
    rockets.append(Rocket(x, START_ROCKET_Y - 20))

    # Decrease ammo.
    ammo = ammo - 1


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

    screen.fill(BLACK_COLOR)

    for line in name:
        screen.blit(title_font.render(line, 1, WHITE_COLOR), (x, y))
        y += 15

    screen.blit(title_font.render("--== Copyright 2018 (C) by Vlad Ivanov ==--", 1, YELLOW_COLOR), (115, 150))

    x2 = 260
    y2 = 225

    draw_brick(x2, y2, RED_COLOR)
    screen.blit(title_font.render("+1 score", 1, YELLOW_COLOR), (x2 + 30, y2 - 5))

    y2 += 20

    draw_brick(x2, y2, WHITE_COLOR)
    screen.blit(title_font.render("+5 ammo", 1, YELLOW_COLOR), (x2 + 30, y2 - 5))

    y2 += 20

    draw_brick(x2, y2, GREEN_COLOR)
    screen.blit(title_font.render("+1 live", 1, YELLOW_COLOR), (x2 + 30, y2 - 5))

    screen.blit(title_font.render("SPACE to shoot | MOUSE to move", 1, YELLOW_COLOR), (180, 330))
    screen.blit(title_font.render("Press ENTER to start", 1, WHITE_COLOR), (220, 400))

    # Update (refresh) screen.
    pygame.display.update()

    is_enter_pressed = False

    while not is_enter_pressed:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                end_game()
            elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_RETURN:
                is_enter_pressed = True


# Shows final score. Wait for 'ESC' button to end the game.
def draw_final_score():
    global click

    game_over=[
        "  ________",
        " /  _____/_____    _____   ____     _______  __ ___________",
        "/   \  ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \\",
        "\    \_\  \/ __ \|  v v  \  ___/  (  <_> )   /\  ___/|  | \/",
        " \______  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|",
        "        \/     \/      \/     \/                   \/"
    ]

    x = 54
    y = 50

    screen.fill(BLACK_COLOR)

    for line in game_over:
        screen.blit(final_font1.render(line, 1, WHITE_COLOR), (x, y))
        y += 15

    final_score_label = final_font2.render("Your final score: " + str(score), 1, YELLOW_COLOR)
    screen.blit(final_score_label, (215, 240))
    pygame.display.update()


draw_title()

pygame.mixer.Channel(0).play(bg_sound, -1)

# Main game loop.
while True:
    # Clear the screen.
    screen.fill(BLACK_COLOR)

    if lives == 0:
        bricks.clear()
        rockets.clear()

        draw_final_score()

    for event in pygame.event.get():
        typ = event.type

        if typ == pygame.QUIT:
            end_game()
        elif typ == pygame.MOUSEMOTION and lives > 0:
            playerX = event.pos[0]
        elif typ == pygame.MOUSEBUTTONDOWN and event.button == 1 and ammo > 0 and lives > 0:
            fire_rocket(event.pos[0] + 8)
        elif typ == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ammo > 0 and lives > 0:
                # Add new rocket using last 'playerX'.
                fire_rocket(playerX + 8)
            elif event.key == pygame.K_ESCAPE and lives == 0:
                # If 'ESC' is pressed and live is zero - we end the game.
                end_game()

    if lives > 0:
        # Randomly place bricks.
        if len(bricks) < 4 and random.randint(0, 100) < 20:
            brickX = random.randint(20, 620)

            rnd = random.randint(0, 100)

            if rnd < 10:
                kind = 3
                speed = 4 # Live bricks have constant "medium" speed.
            elif rnd < 20:
                kind = 2
                speed = 2 # Ammo bricks have constant "slow" speed but they move left to right.
            else:
                kind = 1
                speed = random.randint(2, 4) # Random speed for red bricks.

            bricks.append(Brick(brickX, 0, speed, kind))

        # Check bricks and rockets for collision.
        check_bricks_rockets()

        # Draw player, bricks & rockets & score & lives.
        draw_player()
        draw_rockets()
        draw_bricks()
        draw_header()

    # Update (refresh) screen.
    pygame.display.update()

    # Wait for FPS.
    clock.tick(FPS)


