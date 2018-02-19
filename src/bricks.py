#
#      _/_/_/    _/_/_/    _/_/_/    _/_/_/  _/    _/    _/_/_/
#     _/    _/  _/    _/    _/    _/        _/  _/    _/
#    _/_/_/    _/_/_/      _/    _/        _/_/        _/_/
#   _/    _/  _/    _/    _/    _/        _/  _/          _/
#  _/_/_/    _/    _/  _/_/_/    _/_/_/  _/    _/  _/_/_/
#
#  By Vlad Ivanov, 2018.
#  Email: vlad94568@gmail.com
#

import pygame
import random
import sys


class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Brick:
    # kinds:
    # 1 - normal brick
    # 2 - ammo brick
    def __init__(self, x, y, speed, kind):
        self.x = x
        self.y = y
        self.speed = speed
        self.kind = kind

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

rockets = []
bricks = []

# Initialize the game.
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
headerFont = pygame.font.SysFont("monospace", 15)

pygame.display.set_caption("BRICKS")


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

    pygame.draw.rect(screen, player_color, (playerX, 450, 20, 20), 5)
    pygame.draw.line(screen, player_color, [playerX + 9, 450], [playerX + 9, 435], 5)


# Draws all the rockets in 'rockets' list.
def draw_rockets():
    for rocket in rockets:
        pygame.draw.rect(screen, mk_random_color(), (rocket.x, rocket.y, 5, 8), 1)

        rocket.y -= 6

        if rocket.y < 0:
            rockets.remove(rocket)


# Draws all the bricks in 'bricks' list.
def draw_bricks():
    global lives
    global ammo

    for brick in bricks:
        if brick.kind == 1:
            pygame.draw.rect(screen, RED_COLOR, (brick.x, brick.y, 15, 10), 3)
        else:
            pygame.draw.rect(screen, WHITE_COLOR, (brick.x, brick.y, 15, 10), 3)

        brick.frameCnt += 1

        if brick.kind == 2 and brick.y > 450 and playerX - 15 <= brick.x <= playerX + 20:
            # Player touches ammo brick.
            ammo += 20
            bricks.remove(brick)
        elif brick.y >= 480:
            # Bricks reached the bottom.
            lives -= 1
            bricks.remove(brick)
        else:
            # Move white brick left or right.
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
    global score
    global ammo

    for brick in bricks:
        for rocket in rockets:
            if brick.x - 5 <= rocket.x <= brick.x + 15 and rocket.y <= brick.y:
                # Hide/remove brick and the rocket that killed it.
                rockets.remove(rocket)
                bricks.remove(brick)

                if brick.kind == 1:
                    # Add score for normal killed brick.
                    score = score + 1


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


# Main game loop.
while True:
    for event in pygame.event.get():
        typ = event.type

        if typ == pygame.QUIT:
            end_game()
        elif typ == pygame.MOUSEMOTION:
            playerX = event.pos[0]
        elif typ == pygame.MOUSEBUTTONDOWN and event.button == 1 and ammo > 0:
            fire_rocket(event.pos[0] + 8)
        elif typ == pygame.KEYDOWN and event.key == pygame.K_SPACE and ammo > 0:
            # Add new rocket using last 'playerX'.
            fire_rocket(playerX + 8)

    # Randomly place bricks.
    if random.randint(0, 255) < 5:
        brickX = random.randint(20, 620)
        if random.randint(0, 100) < 10:
            kind = 2
            speed = 2 # Ammo bricks have constant "slow" speed but they move left to right.
        else:
            kind = 1
            speed = random.randint(2, 6) # Random speed for red bricks.

        bricks.append(Brick(brickX, 0, speed, kind))

    # Clear the screen.
    screen.fill(BLACK_COLOR)

    # Check bricks and rockets for collision.
    check_bricks_rockets()

    # Draw player, bricks & rockets & score & lives.
    draw_player()
    draw_rockets()
    draw_bricks()
    draw_header()

    # Update (refresh) screen.
    pygame.display.update()

    if lives == 0:
        end_game()

    # Wait for FPS.
    clock.tick(FPS)


