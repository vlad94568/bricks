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
from pygame import gfxdraw

# Import all scene elements.
from src.scene.star import *
from src.scene.brick import *
from src.scene.flower import *

# Initializing the joystick.
pygame.joystick.init()

START_ROCKET_Y = 450
START_BRICK_Y = 0

# Horizontal speed in pixels.
HOR_PIXELS = 8

left = 0
right = 0

fps = 30
score = 0
lives = 20
ammo = 100
playerX = 320

# List of rockets, bricks and explosions.
rockets = []
bricks = []
explosions = []

# Initialize pygame & its modules.
pygame.init()
pygame.mixer.init()
pygame.font.init()

# Mixer channels:
# 0 - background (title and main game)
# 1 - rocket fire
# 2 - brick air-kill (killed by rocket)
# 3 - brick ground-kill (reached the bottom)

# Sounds.
main_bg_sound = pygame.mixer.Sound("sounds/background_sound0.1.ogg")
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

# Whether or not a supported joystick is found.
is_joystick_found = False

# Window title.
pygame.display.set_caption("--==B.R.I.C.K.S==--")


def init_joystick():
    global is_joystick_found

    joystick_count = pygame.joystick.get_count()

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()

        if name.startswith("USB,2-axis 8-button gamepad"):
            is_joystick_found = True


def draw_grass_blades(grass_x):
    pygame.draw.rect(screen, DARK_GREEN_COLOR, (grass_x + 3, 450, 2, 20))
    pygame.draw.rect(screen, DARK_GREEN_COLOR, (grass_x + 6, 450, 2, 20))
    pygame.draw.rect(screen, DARK_GREEN_COLOR, (grass_x + 9, 450, 2, 20))


# TODO
star1 = Star(100, 100, WHITE_COLOR, 15)
star2 = Star(130, 150, YELLOW_COLOR, 10)
star3 = Star(180, 190, RED2_COLOR, 5)

flower1 = Flower(100)
flower2 = Flower(200)
flower3 = Flower(300)
flower4 = Flower(400)


def draw_background():
    # Drawing the ground.
    pygame.draw.rect(screen, DARK_GREEN_COLOR, (0, 460, 640, 200))

    # Drawing grass.
    draw_grass_blades(10)
    draw_grass_blades(100)
    draw_grass_blades(345)
    draw_grass_blades(550)
    draw_grass_blades(200)

    # Drawing flowers.
    flower1.draw(screen)
    flower2.draw(screen)
    flower3.draw(screen)
    flower4.draw(screen)

    # Drawing stars.
    star1.draw(screen)
    star2.draw(screen)
    star3.draw(screen)


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


# Draws the player at 'x' coordinate.
def draw_player(x):
    pygame.draw.rect(screen, GREEN_COLOR, (x, 450, 20, 20), 5)  # Base.
    pygame.draw.line(screen, GREEN_COLOR, [x + 9, 450], [x + 9, 435], 5)  # Turret.


# Draws all the rockets in 'rockets' list.
def draw_rockets():
    rockets[:] = [rocket for rocket in rockets if rocket.y > 5]  # Filter out out of screen rockets.

    for rocket in rockets:
        if rocket.frame_cnt % 5 == 0:
            rocket.color = mk_random_color()

        pygame.draw.rect(screen, rocket.color, (rocket.x, rocket.y, 5, 8), 1)

        rocket.y -= 6
        rocket.frame_cnt += 1


# Draws all the explosions.
def draw_explosions():
    exp_to_remove = []

    for exp in explosions:
        if exp.is_done():
            exp_to_remove.append(exp)
        else:
            for frag in exp.frags:
                draw_fragment(frag)

    explosions[:] = [exp for exp in explosions if exp not in exp_to_remove]


# Draws an individual fragment.
def draw_fragment(frag):
    if type(frag) is AirFragment:
        draw_turned_square(frag.x, frag.y, frag.size, mk_random_color(), frag.turn_angle)

        frag.turn_angle += frag.speed + 10
        frag.frame_cnt += 1

        frag.x, frag.y = transform(frag.x, frag.y, frag.speed, frag.angle)
    else:  # GroundFragment
        draw_turned_square(frag.x, frag.y, frag.size, frag.color, frag.turn_angle)

        frag.turn_angle += frag.speed + 10
        frag.frame_cnt += 1

        # Transform with the angle in [280, 80] range (upper two quadrants).
        frag.x, frag.y = transform(frag.x, frag.y, frag.speed, (360 + frag.angle - 90) % 360)


# Draws a square with (x, y) center, 2*size diagonal, and turned at the angle.
def draw_turned_square(x, y, size, color, angle):
    x1, y1 = transform(x, y, size, angle % 360)
    x2, y2 = transform(x, y, size, (angle + 90) % 360)
    x3, y3 = transform(x, y, size, (angle + 180) % 360)
    x4, y4 = transform(x, y, size, (angle + 270) % 360)

    pygame.gfxdraw.aapolygon(screen, [(x1, y1), (x2, y2), (x3, y3), (x4, y4)], color)


# Transforms (x, y) coordinate to distance at a given angle.
# Returns new (x, y) coordinate for the new location.
def transform(x, y, distance, angle):
    if angle <= 90:
        rad = math.radians(angle)

        new_x = x + distance * math.sin(rad)
        new_y = y - distance * math.cos(rad)
    elif angle <= 180:
        rad = math.radians(180 - angle)

        new_x = x + distance * math.sin(rad)
        new_y = y + distance * math.cos(rad)
    elif angle <= 270:
        rad = math.radians(270 - angle)

        new_x = x - distance * math.cos(rad)
        new_y = y + distance * math.sin(rad)
    else:
        rad = math.radians(360 - angle)

        new_x = x - distance * math.sin(rad)
        new_y = y - distance * math.cos(rad)

    return new_x, new_y


# Draws all the bricks in 'bricks' list.
def draw_bricks():
    global lives
    global ammo

    explosions.extend(
        [
            Explosion(
                [
                    GroundFragment(brick.x, brick.y, brick.kind) for _ in range(5)
                ]
            )
            for brick in bricks if brick.y >= 470
        ]
    )

    old_cnt = len(bricks)
    bricks[:] = [brick for brick in bricks if brick.y < 470]  # Filter out fallen bricks.
    new_cnt = len(bricks)

    if old_cnt != new_cnt:
        squished = True
        lives -= old_cnt - new_cnt
    else:
        squished = False

    for brick in bricks:
        brick.draw(screen)

        brick.frame_cnt += 1

        # Move white brick left or right (change direction every 15 frames, i.e. every second).
        if brick.kind == 2 and brick.frame_cnt % 15 == 0:
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

                        frag_x = brick.x + 7
                        frag_y = brick.y + 5

                        explosions.append(Explosion([AirFragment(frag_x, frag_y) for _ in range(5)]))

    if len(bricks_to_remove) > 0:
        boom_sound()

    bricks[:] = [brick for brick in bricks if brick not in bricks_to_remove]
    rockets[:] = [rocket for rocket in rockets if rocket not in rockets_to_remove]


# Draw score, live and ammo.
def draw_header():
    score_label = headerFont.render("score: " + str(score), 1, RED2_COLOR)
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
    ammo -= 1

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

    screen.fill(SLACK_COLOR)

    for line in name:
        screen.blit(title_font.render(line, 1, mk_random_color()), (x, y))
        y += 15

    screen.blit(title_font.render("--== Copyright 2018 (C) by Vlad Ivanov ==--", 1, YELLOW_COLOR), (115, 150))

    x2 = 260
    y2 = 225

    Brick(x2, y2, 0, 1).draw(screen)
    screen.blit(title_font.render("+1 score", 1, YELLOW_COLOR), (x2 + 30, y2))

    y2 += 20

    Brick(x2, y2, 0, 2).draw(screen)
    screen.blit(title_font.render("+5 ammo", 1, YELLOW_COLOR), (x2 + 30, y2))

    y2 += 20

    Brick(x2, y2, 0, 3).draw(screen)
    screen.blit(title_font.render("+1 live", 1, YELLOW_COLOR), (x2 + 30, y2))

    screen.blit(title_font.render("SPACE to shoot | ARROW KEYS to move", 1, YELLOW_COLOR), (150, 330))

    if is_joystick_found:
        screen.blit(title_font.render("Supported joystick found", 1, YELLOW_COLOR), (200, 370))

    screen.blit(title_font.render("Press ENTER to start", 1, WHITE_COLOR), (220, 410))

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

    screen.fill(SLACK_COLOR)

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

    global left
    global right

    player_x = 320
    left = 0
    right = 0

    # Main game loop.
    while True:
        # Clear the screen.
        screen.fill(DARK_BLUE_COLOR)

        # Draw the world.
        draw_background()

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
                if typ == pygame.JOYBUTTONDOWN:
                    print("Joystick button pressed.")

            if left == 1:
                player_x = player_x - HOR_PIXELS
            elif right == 1:
                player_x = player_x + HOR_PIXELS

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

            # Checking if player touches wall.
            if player_x == 0 or player_x < 0:
                player_x = 0
            elif player_x == 640 or player_x > 640:
                player_x = 640

            # Check bricks and rockets for collision.
            check_bricks_rockets()

            # Draw player, bricks, rockets & headers.
            draw_player(player_x)
            draw_rockets()
            draw_bricks()
            draw_header()
            draw_explosions()
            print()

        # Update (refresh) screen.
        pygame.display.update()

        # Wait for FPS.
        clock.tick(fps)


# +=================+
# | Start the game. |
# +=================+
init_joystick()
draw_title()
main_game_loop()

