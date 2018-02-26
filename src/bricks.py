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

        self.frameCnt = 0
        self.color = mk_random_color()


class Brick:
    # kinds:
    # 1 - normal brick (RED)
    # 2 - ammo brick (WHITE)
    # 3 - live break (GREEN)
    def __init__(self, x, y, y_speed, kind):
        self.x = x
        self.y = y
        self.y_speed = y_speed
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

fps = 30
score = 0
lives = 20
ammo = 100
playerX = 0
rockets = []
bricks = []

# Initialize pygame & its modules.
pygame.init()
pygame.mixer.init()
pygame.font.init()

# Mixer channels:
# 0 - background (title and main game)
# 1 - rocket fire
# 2 - brick kill
# 3 - brick squished (reached the bottom)

# Sounds.
main_bg_sound = pygame.mixer.Sound("sounds/background_sound0.ogg")
title_bg_sound = pygame.mixer.Sound("sounds/background_sound1.ogg")
final_bg_sound = pygame.mixer.Sound("sounds/background_sound2.ogg")
rocket_fire_sound = pygame.mixer.Sound("sounds/rocket_fired.ogg")
brick_kill_sound = pygame.mixer.Sound("sounds/brick_kill.ogg")
brick_squish_sound = pygame.mixer.Sound("sounds/brick_squished.ogg")

# Pygame initialization.
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Grabbing fonts from 'fonts' sub-folder to be 100% cross-platform compatible.
headerFont = pygame.font.Font("fonts/Anonymous.ttf", 13)
title_font = pygame.font.Font("fonts/Anonymous.ttf", 13)
final_font1 = pygame.font.Font("fonts/Anonymous.ttf", 13)
final_font2 = pygame.font.Font("fonts/Anonymous.ttf", 16)

# Window title.
pygame.display.set_caption("--==B.R.I.C.K.S==--")


# Sounds kill of the brick.
def boom_sound():
    pygame.mixer.Channel(2).play(brick_kill_sound)


# Sounds of the brick hitting the bottom.
def squish_sound():
    pygame.mixer.Channel(3).play(brick_squish_sound)


# Sounds the rocket firing.
def rocket_sound():
    pygame.mixer.Channel(1).set_volume(0.3)
    pygame.mixer.Channel(1).play(rocket_fire_sound)


# Generates random color.
def mk_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


# Draws the player at 'x' coordinate.
def draw_player(x):
    pygame.draw.rect(screen, GREEN_COLOR, (x, 450, 20, 20), 5)  # Base.
    pygame.draw.line(screen, GREEN_COLOR, [x + 9, 450], [x + 9, 435], 5)  # Turret.


# Draws all the rockets in 'rockets' list.
def draw_rockets():
    rockets[:] = [rocket for rocket in rockets if rocket.y > 5]  # Filter out out of screen rockets.

    for rocket in rockets:
        if rocket.frameCnt % 5 == 0:
            rocket.color = mk_random_color()

        pygame.draw.rect(screen, rocket.color, (rocket.x, rocket.y, 5, 8), 1)

        rocket.y -= 6
        rocket.frameCnt += 1


# Draws a brick with given (x, y) coordinates and color.
def draw_brick(x, y, color):
    pygame.draw.rect(screen, color, (x, y, 15, 10), 3)


# Draws all the bricks in 'bricks' list.
def draw_bricks():
    global lives
    global ammo

    old_cnt = len(bricks)
    bricks[:] = [brick for brick in bricks if brick.y < 470]  # Filter out fallen bricks.
    new_cnt = len(bricks)

    if old_cnt != new_cnt:
        squished = True
        lives -= old_cnt - new_cnt
    else:
        squished = False

    for brick in bricks:
        if brick.kind == 1:
            draw_brick(brick.x, brick.y, RED_COLOR)
        elif brick.kind == 2:
            draw_brick(brick.x, brick.y, WHITE_COLOR)
        else:  # kind == 3
            draw_brick(brick.x, brick.y, GREEN_COLOR)

        brick.frameCnt += 1

        # Move white brick left or right (change direction every 15 frames, i.e. every second).
        if brick.kind == 2 and brick.frameCnt % 15 == 0:
            if random.randint(0, 100) > 50:
                brick.x_adj = brick.y_speed
            else:
                brick.x_adj = -brick.y_speed

        # Brick is still falling down.
        brick.y += brick.y_speed
        brick.x += brick.x_adj

    if squished:
        squish_sound()


# Checking for crashes between rockets and bricks.
def check_bricks_rockets():
    global score, ammo, lives

    bricks_to_remove = []
    rockets_to_remove = []

    for brick in bricks:
        if brick not in bricks_to_remove:
            for rocket in rockets:
                if rocket not in rockets_to_remove:
                    if brick.x - 5 <= rocket.x <= brick.x + 15 and rocket.y <= brick.y + 10:
                        # Rocket hit that brick...
                        rockets_to_remove.append(rocket)
                        bricks_to_remove.append(brick)

                        if brick.kind == 1:  # RED brick.
                            # Add score for normal killed brick.
                            score += 1
                        elif brick.kind == 2:  # WHITE brick.
                            # Add ammo.
                            ammo += 5
                        elif brick.kind == 3:  # GREEN brick.
                            # Add lives.
                            lives += 1

    if len(bricks_to_remove) > 0:
        boom_sound()

    bricks[:] = [brick for brick in bricks if brick not in bricks_to_remove]
    rockets[:] = [rocket for rocket in rockets if rocket not in rockets_to_remove]


# Draw score, live and ammo.
def draw_header():
    score_label = headerFont.render("score: " + str(score), 1, RED_COLOR)
    lives_label = headerFont.render("lives: " + str(lives), 1, GREEN_COLOR)
    ammo_label = headerFont.render("ammo: " + str(ammo), 1, WHITE_COLOR)

    screen.blit(score_label, (10, 10))
    screen.blit(lives_label, (150, 10))
    screen.blit(ammo_label, (290, 10))


# Ends the game.
def end_game():
    pygame.quit()
    sys.exit()


# Fires the rocket.
def fire_rocket(x):
    global ammo

    # Add new rocket.
    rockets.append(Rocket(x, START_ROCKET_Y - 20))

    # Decrease ammo.
    ammo = ammo - 1

    # BANG!
    rocket_sound()


# Waits until given keyboard key is pressed.
def wait_key_pressed(key):
    is_pressed = False

    while not is_pressed:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                end_game()
            elif evt.type == pygame.KEYDOWN and evt.key == key:
                is_pressed = True


# Draws the game's welcome screen (aka title).
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
        screen.blit(title_font.render(line, 1, mk_random_color()), (x, y))
        y += 15

    screen.blit(title_font.render("--== Copyright 2018 (C) by Vlad Ivanov ==--", 1, YELLOW_COLOR), (115, 150))

    x2 = 260
    y2 = 225

    draw_brick(x2, y2, RED_COLOR)
    screen.blit(title_font.render("+1 score", 1, YELLOW_COLOR), (x2 + 30, y2))

    y2 += 20

    draw_brick(x2, y2, WHITE_COLOR)
    screen.blit(title_font.render("+5 ammo", 1, YELLOW_COLOR), (x2 + 30, y2))

    y2 += 20

    draw_brick(x2, y2, GREEN_COLOR)
    screen.blit(title_font.render("+1 live", 1, YELLOW_COLOR), (x2 + 30, y2))

    screen.blit(title_font.render("SPACE to shoot | MOUSE to move", 1, YELLOW_COLOR), (180, 330))
    screen.blit(title_font.render("Press ENTER to start", 1, WHITE_COLOR), (220, 400))

    # Start title background music.
    pygame.mixer.Channel(0).play(title_bg_sound, -1)

    # Update (refresh) screen.
    pygame.display.update()

    wait_key_pressed(pygame.K_RETURN)


# Shows final score. Wait for 'ESC' button to end the game.
def draw_final_score():
    # Stop all sounds.
    pygame.mixer.stop()

    lines = [
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

    for line in lines:
        screen.blit(final_font1.render(line, 1, mk_random_color()), (x, y))
        y += 15

    screen.blit(final_font2.render("Your final score: " + str(score), 1, RED_COLOR), (205, 240))
    screen.blit(final_font1.render("Press ESC to exit the game", 1, WHITE_COLOR), (200, 360))

    # Start title background music.
    pygame.mixer.Channel(0).play(final_bg_sound, -1)

    pygame.display.update()

    wait_key_pressed(pygame.K_ESCAPE)


# Main game loop.
def main_game_loop():
    # Start main background music.
    pygame.mixer.Channel(0).play(main_bg_sound, -1)

    player_x = 0

    # Main game loop.
    while True:
        # Clear the screen.
        screen.fill(BLACK_COLOR)

        if lives == 0 or ammo == 0:
            game_over = True
        else:
            game_over = False

        if game_over:
            game_over_delay = 3 * 1000  # 3 seconds delays.

            pygame.mixer.Channel(0).fadeout(game_over_delay - 250)
            pygame.time.delay(game_over_delay)

            # Clear data.
            bricks.clear()
            rockets.clear()

            # Draw final score.
            draw_final_score()

            # End the game.
            end_game()
        else:
            for event in pygame.event.get():
                typ = event.type

                if typ == pygame.QUIT:
                    end_game()
                elif typ == pygame.MOUSEMOTION:
                    # Move the player.
                    player_x = event.pos[0]
                elif typ == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Fire the rocket with mouse X coordinate.
                    fire_rocket(event.pos[0] + 8)
                elif typ == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # Fire the rocket using last 'playerX'.
                    fire_rocket(player_x + 8)

            # Randomly place bricks.
            if len(bricks) < 5:
                brick_x = random.randint(20, 620)

                rnd = random.randint(0, 100)

                if rnd < 10:
                    kind = 3
                    speed = 4  # Lives bricks have constant "medium" speed.
                elif rnd < 35:
                    kind = 2
                    speed = 2  # Ammo bricks have constant "slow" speed but they move left to right.
                else:
                    kind = 1
                    speed = random.randint(1, 4)  # Random speed for red bricks.

                bricks.append(Brick(brick_x, 0, speed, kind))

            # Check bricks and rockets for collision.
            check_bricks_rockets()

            # Draw player, bricks & rockets & headers.
            draw_player(player_x)
            draw_rockets()
            draw_bricks()
            draw_header()

        # Update (refresh) screen.
        pygame.display.update()

        # Wait for FPS.
        clock.tick(fps)


# +=================+
# | Start the game. |
# +=================+
draw_title()
main_game_loop()



