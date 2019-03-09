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

import sys
import time

# Import all scene elements.
from pygame.constants import K_RETURN

from src.scene.star import *
from src.scene.brick import *
from src.scene.flower import *
from src.scene.simple_ground import *
from src.scene.grass import *
from src.scene.rocket import *
from src.scene.air_fragment import *
from src.scene.ground_fragment import *
from src.scene.mountain import *
from src.scene.tree import *
from src.scene.clouds import *
from src.scene.building import *

# Initialize pygame & its modules.
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.joystick.init()


def detect_joystick():
    joystick_count = pygame.joystick.get_count()

    for i in range(joystick_count):
        jk = pygame.joystick.Joystick(i)
        jk.init()

        # Get the name from the OS for the controller/joystick
        name = jk.get_name()

        if name.startswith("USB,2-axis 8-button gamepad"):
            return jk

    return None

# Sounds from 'sounds' sub-folder.
bg_sound_1 = pygame.mixer.Sound("sounds/background_sound0.1.ogg")
title_bg_sound = pygame.mixer.Sound("sounds/background_sound1.ogg")
final_bg_sound = pygame.mixer.Sound("sounds/background_sound2.ogg")
rocket_fire_sound = pygame.mixer.Sound("sounds/rocket_fired.ogg")
brick_kill_sound = pygame.mixer.Sound("sounds/brick_kill.ogg")
brick_squish_sound = pygame.mixer.Sound("sounds/brick_squished.ogg")
you_won_sound = pygame.mixer.Sound("sounds/win_song.ogg")

# Definition of a single level.
class Level:
    def __init__(self,
                 lvl_num,  # E.g. 1
                 name,
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
        self.name = name
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

        self.total_bricks = self.num_red_bricks + self.num_white_bricks + self.num_green_bricks
        self.red_brick_factor = self.num_red_bricks / self.total_bricks
        self.white_brick_factor = self.num_white_bricks / self.total_bricks
        self.green_brick_factor = self.num_green_bricks / self.total_bricks

# Game levels.
game_lvl1 = Level(
    # Desert themed level.
    1,
    'Ancient Desert',
    BLUE_COLOR_2,
    WHITE_COLOR,
    bg_sound_1,
    num_red_bricks=12,
    num_green_bricks=16,
    num_white_bricks=10,
    red_bricks_max_speed=4,
    red_bricks_min_speed=2,
    green_bricks_max_speed=4,
    green_bricks_min_speed=2,
    white_bricks_max_speed=4,
    white_bricks_min_speed=2,
    max_bricks_on_screen=5,
    scene_elements=[
        SimpleGround(10, YELLOW_COLOR),
        Flower(50, 40, 60),
        Flower(250, 40, 80),
        Flower(350, 50, 50),
        Flower(550, 40, 40),
        Grass(60, 10, 20, 43, GREEN_COLOR),
        Grass(260, 10, 20, 18, GREEN_COLOR),
        Grass(360, 10, 20, 43, GREEN_COLOR),
        Tree(500, 125, 15, BROWN_COLOR, GREEN_COLOR),
        Tree(150, 150, 15, BROWN_COLOR, GREEN_COLOR)
    ]
)
game_lvl2 = Level(
    2,
    'Creepy Plains',
    (66, 123, 194),
    WHITE_COLOR,
    bg_sound_1,
    num_red_bricks=23,
    num_green_bricks=17,
    num_white_bricks=12,
    red_bricks_max_speed=5,
    red_bricks_min_speed=3,
    green_bricks_max_speed=5,
    green_bricks_min_speed=3,
    white_bricks_max_speed=5,
    white_bricks_min_speed=3,
    max_bricks_on_screen=6,
    scene_elements=[
        Mountain(300, 250, 250, BROWN_COLOR, (216, 244, 255)),
        Mountain(500, 275, 275, (192, 130, 157), (216, 244, 255)),
        Mountain(100, 275, 300, (155, 90, 90), (216, 244, 255)),
        Mountain(-30, 230, 230, (192, 191, 21), (216, 244, 255)),
        Clouds(-15, 35),
        Clouds(-400, 25),
        Clouds(-850, 45),
        Flower(50, 50, 65),
        Flower(250, 50, 80),
        Flower(350, 50, 70),
        Flower(550, 50, 75),
        Grass(0, 25, 40, 80, GREEN_COLOR),
        Grass(260, 25, 40, 100, GREEN_COLOR),
        Grass(360, 25, 40, 100, GREEN_COLOR),
        SimpleGround(10,BROWN_COLOR)
    ]
)

game_lvl3 = Level(
    3,
    'Rotten Covert',
    (71, 91, 123),
    WHITE_COLOR,
    bg_sound_1,
    num_red_bricks=38,
    num_green_bricks=21,
    num_white_bricks=14,
    red_bricks_max_speed=6,
    red_bricks_min_speed=3,
    green_bricks_max_speed=6,
    green_bricks_min_speed=3,
    white_bricks_max_speed=6,
    white_bricks_min_speed=3,
    max_bricks_on_screen=7,
    scene_elements=[
        Tree(275, 340, 25, (171, 64, 47), (18, 123, 56)),
        Tree(155, 350, 25, (213, 80, 59), (127, 123, 170)),
        Tree(75, 325, 25, (89, 33, 24), (116, 63, 123)),
        Tree(370, 330, 25, (213, 80, 59), (123, 46, 11)),
        Tree(500, 360, 25, (171, 64, 47), (180, 184, 195)),
        Tree(615, 310, 25, (213, 80, 59), (66, 123, 77)),
        Flower(50, 50, 65),
        Flower(250, 50, 80),
        Flower(350, 50, 70),
        Flower(550, 50, 75),
        Grass(0, 25, 40, 80, GREEN_COLOR),
        Grass(260, 25, 40, 100, GREEN_COLOR),
        Grass(360, 25, 40, 100, GREEN_COLOR),
        SimpleGround(10,BROWN_COLOR)

    ]
)

game_lvl4 = Level(
    4,
    'Neon City Lights',
    DARK_BLUE_COLOR,
    WHITE_COLOR,
    bg_sound_1,
    num_red_bricks=50,
    num_green_bricks=21,
    num_white_bricks=14,
    red_bricks_max_speed=7,
    red_bricks_min_speed=4,
    green_bricks_max_speed=7,
    green_bricks_min_speed=4,
    white_bricks_max_speed=7,
    white_bricks_min_speed=4,
    max_bricks_on_screen=7,
    scene_elements=[
        Building(30, (233, 238, 214), YELLOW_COLOR, 4, 3, False),
        Building(135, BROWN_COLOR, GREY_COLOR, 5, 3, False),
        Building(400, (238, 97, 200), YELLOW_COLOR, 13, 3, False),
        Building(250, (238, 44, 105), YELLOW_COLOR, 16, 3, True),
        Building(530, (120, 87, 238), GREY_COLOR, 7, 5, False),
        Star(130, 80, GREY_COLOR, 5),
        Star(320, 120, GREY_COLOR, 5),
        Star(380, 85, GREY_COLOR, 5),
        Star(590, 82, GREY_COLOR, 5),
        Star(50, 85, GREY_COLOR, 5),
        Clouds(-55, 75, GREY3_COLOR),
        Tree(355, 80, 10, BROWN_COLOR, (180,184, 95)),
        Tree(497, 80, 10, BROWN_COLOR, (127, 123, 170)),
        Tree(223, 80, 10, BROWN_COLOR, DARK_GREEN_COLOR),
        SimpleGround(10,GREY_COLOR)
    ]
)

game_lvl5 = Level(
    5,
    'City of Final Mayhem',
    (35, 0, 29),
    WHITE_COLOR,
    bg_sound_1,
    num_red_bricks=75,
    num_green_bricks=23,
    num_white_bricks=15,
    red_bricks_max_speed=8,
    red_bricks_min_speed=4,
    green_bricks_max_speed=8,
    green_bricks_min_speed=4,
    white_bricks_max_speed=8,
    white_bricks_min_speed=4,
    max_bricks_on_screen=8,
    scene_elements=[
        SimpleGround(10, DARK_BLUE_COLOR),
        Mountain(100, 275, 300, (185, 68, 8), (131, 118, 100)),
        Mountain(-30, 230, 230, (1, 123, 128), (131, 118, 100)),
        Flower(50, 50, 65),
        Flower(250, 50, 80),
        Building(430, (3, 60, 166), YELLOW_COLOR, 16, 3, True),
        Building(530, (128, 2, 108), YELLOW_COLOR, 12, 4, True),
        Star(130, 80, GREY_COLOR, 5),
        Star(320, 120, GREY_COLOR, 5),
        Star(380, 85, GREY_COLOR, 5),
        Star(590, 82, GREY_COLOR, 5),
        Star(50, 85, GREY_COLOR, 5),
        Clouds(-55, 75, (161, 36, 225)),
        Clouds(255, 75, (161, 36, 225)),
        Tree(390, 80, 10, BROWN_COLOR, (181, 143, 14)),
        Grass(0, 5, 30, 250, GREEN_COLOR)
    ]
)


# Explosion is just a container for fragments.
class Explosion:
    def __init__(self, frags):
        self.frags = frags

    def is_done(self):
        return self.frags[0].frame_cnt == 30

    # Draws explosion (i.e. its fragments).
    def draw(self, scr):
        for frag in self.frags:
            frag.draw(scr)


# Game levels.
levels = [
    # game_lvl1,
    # game_lvl2,
    # game_lvl3,
    # game_lvl4,
    game_lvl5
]

# Grabbing fonts from 'fonts' sub-folder to be 100% cross-platform compatible.
header_font = pygame.font.Font("fonts/Anonymous.ttf", 13)
title_font = pygame.font.Font("fonts/Anonymous.ttf", 13)
ver_font = pygame.font.Font("fonts/Anonymous.ttf", 10)
final_font1 = pygame.font.Font("fonts/Anonymous.ttf", 13)
final_font2 = pygame.font.Font("fonts/Anonymous.ttf", 13)
level_font = pygame.font.Font("fonts/Anonymous.ttf", 16)
level_font2 = pygame.font.Font("fonts/Anonymous.ttf", 24)

# Pygame globals.
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Initial lives & ammo.
init_ammo = 30
init_lives = 20

# Current stats.
lives = init_lives
ammo = init_ammo
score = 0
used_bricks = 0
level_completion = 0

joystick = detect_joystick()  # Auto-detect joystick at the start.
fps = 30
player_x = screen_width / 2 - 10

# Current playing level data.
bricks = []
rockets = []
explosions = []
used_green_bricks = 0
used_white_bricks = 0
used_red_bricks = 0

# Window title.
pygame.display.set_caption("--==B.R.I.C.K.S==--")

# Sounds kill of the brick.
def boom_sound():
    pygame.mixer.Channel(2).play(brick_kill_sound)


# Sounds the brick hitting the bottom.
def squish_sound():
    pygame.mixer.Channel(3).play(brick_squish_sound)


# Sounds the rocket firing.
def rocket_sound():
    pygame.mixer.Channel(1).set_volume(0.3)
    pygame.mixer.Channel(1).play(rocket_fire_sound)


# Fades out all channels.
def fadeout_all_sounds():
    pygame.mixer.Channel(0).fadeout(2000)
    pygame.mixer.Channel(1).fadeout(2000)
    pygame.mixer.Channel(2).fadeout(2000)
    pygame.mixer.Channel(3).fadeout(2000)


# Plays background sound (channel 0).
def background_sound(sound):
    pygame.mixer.Channel(0).play(sound, -1)


# Adds, if necessary, a new random brick.
def add_new_bricks(lvl):
    global bricks
    global used_red_bricks, used_white_bricks, used_green_bricks

    # Randomly place bricks, if necessary.
    if len(bricks) < lvl.max_bricks_on_screen:
        brick_x = random.randint(20, 620)

        rnd = random.random()
        factor = random.random()

        if rnd < 0.33:
            if used_green_bricks < lvl.num_green_bricks and factor < lvl.green_brick_factor:
                used_green_bricks += 1
                speed = random.randint(lvl.green_bricks_min_speed, lvl.green_bricks_max_speed)
                bricks.append(Brick(brick_x, 0, speed, 3))
        elif rnd < 0.66:
            if used_white_bricks < lvl.num_white_bricks and factor < lvl.white_brick_factor:
                used_white_bricks += 1
                speed = random.randint(lvl.white_bricks_min_speed, lvl.white_bricks_max_speed)
                bricks.append(Brick(brick_x, 0, speed, 2))
        elif used_red_bricks < lvl.num_red_bricks and factor < lvl.red_brick_factor:
            used_red_bricks += 1
            speed = random.randint(lvl.red_bricks_min_speed, lvl.red_bricks_max_speed)
            bricks.append(Brick(brick_x, 0, speed, 1))


# Waits until either RETURN, ENTER or Joystick A button is pressed.
def wait_start_pressed():
    is_pressed = False

    while not is_pressed:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                end_game()
            elif evt.type == pygame.KEYDOWN and evt.key == K_RETURN:
                is_pressed = True
            elif evt.type == pygame.JOYBUTTONDOWN and round(joystick.get_button(7)) == 1:
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

    screen.fill(SLACK_COLOR)

    # Shortcut function.
    def pri(s, s_x, s_y, color=YELLOW_COLOR, font=title_font):
        screen.blit(font.render(s, 1, color), (s_x, s_y))

    for line in ascii_name:
        pri(line, x, y, mk_random_color())
        y += 15

    pri("--== Copyright 2018-2019 (C) by Vlad Ivanov ==--", 105, 150)
    pri("ver. 2.0.0", 270, 170, font=ver_font)

    x2 = 260
    y2 = 225

    Brick(x2, y2, 0, 1).draw(screen)
    pri("+1 score", x2 + 30, y2)

    y2 += 20

    Brick(x2, y2, 0, 2).draw(screen)
    pri("+9 ammo", x2 + 30, y2)

    y2 += 20

    Brick(x2, y2, 0, 3).draw(screen)
    pri("+2 live", x2 + 30, y2)

    pri("SPACE to shoot | <- -> to move", 175, 330)

    if joystick is not None:
        pri("Supported joystick found", 200, 370)

    pri("Press ENTER to start", 220, 410)

    # Start title background music.
    background_sound(title_bg_sound)

    # Update (refresh) screen.
    pygame.display.update()

    if wait_start_pressed():
        main_game_loop()


# Moved player X coordinate left.
def move_player_left():
    global player_x

    player_x -= 8

    # Roll around the screen.
    if player_x < -20:
        player_x = screen_width


# Moved player X coordinate right.
def move_player_right():
    global player_x

    player_x += 8

    # Roll around the screen.
    if player_x > screen_width:
        player_x = 0


# Draw score, live and ammo.
def draw_header(lvl):
    score_label = header_font.render("score: " + str(score), 1, RED2_COLOR)
    lives_label = header_font.render("lives: " + str(lives), 1, GREEN_COLOR)
    ammo_label = header_font.render("ammo: " + str(ammo), 1, WHITE_COLOR)

    level_label = header_font.render(
        "level: " +
        str(lvl.lvl_num) +
        " (" + str(level_completion) + "%) of " +
        str(len(levels))
        , 1, YELLOW_COLOR)

    screen.blit(score_label, (50, 10))
    screen.blit(lives_label, (190, 10))
    screen.blit(ammo_label, (330, 10))
    screen.blit(level_label, (450, 10))


# Draws all the explosions.
def draw_explosions():
    global explosions

    exp_to_remove = []

    for exp in explosions:
        if exp.is_done():
            exp_to_remove.append(exp)
        else:
            for frag in exp.frags:
                frag.draw(screen)

    explosions[:] = [exp for exp in explosions if exp not in exp_to_remove]


# Draws all the bricks.
def draw_bricks():
    global lives, ammo, explosions, used_bricks

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

    used_bricks += old_cnt - new_cnt

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
    global score, ammo, lives, used_bricks

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
                            ammo += 9
                        elif brick.kind == 3:  # GREEN brick.
                            # Add lives.
                            lives += 2

                        frag_x = brick.x + 7
                        frag_y = brick.y + 5

                        explosions.append(Explosion([AirFragment(frag_x, frag_y) for _ in range(5)]))

    if len(bricks_to_remove) > 0:
        boom_sound()

    used_bricks += len(bricks_to_remove)

    bricks[:] = [brick for brick in bricks if brick not in bricks_to_remove]
    rockets[:] = [rocket for rocket in rockets if rocket not in rockets_to_remove]


# Draws all the rockets in 'rockets' list.
def draw_rockets():
    global rockets

    # Filter out rockets.
    rockets[:] = [rocket for rocket in rockets if rocket.y > 5]

    for rocket in rockets:
        rocket.draw(screen)
        rocket.y -= 6


# Fires the rocket.
def fire_rocket():
    global ammo

    # Add new rocket.
    rockets.append(Rocket(player_x + 7, screen_height - 40))

    # Decrease ammo.
    ammo -= 1

    # BANG!
    rocket_sound()


def screen_fade_out(color=DARK_GREY_COLOR):
    ani = True

    x = screen_width / 2 - 2
    y = screen_height / 2 - 2
    w = 4
    h = 4

    # Slowly growing black rectangle.
    while ani:
        pygame.draw.rect(screen, color, (x, y, w, h))

        w += 30  # Grow faster horizontally since screen isn't perfect square.
        h += 20
        x -= 15  # Grow faster horizontally since screen isn't perfect square.
        y -= 10

        # Quite loop when rectangle covers all screen.
        if w > screen_width and h > screen_height:
            ani = False

        pygame.event.get()
        pygame.display.update()

        clock.tick(fps)


# Animations to switch to a given level.
def switch_to_level(lvl):
    # Fade out sounds.
    fadeout_all_sounds()

    # Fade out the screen.
    screen_fade_out()
    title_x = 300 - (len(lvl.name) / 2) * 17
    # Draw level number.
    screen.fill(DARK_GREY_COLOR)
    screen.blit(level_font.render("--== level " + str(lvl.lvl_num) + " ==--", 1, GREEN_COLOR), (220, 210))
    screen.blit(level_font2.render('"' + lvl.name + '"', 1, GREEN_COLOR), (title_x, 165))

    pygame.display.update()
    pygame.event.get()

    # Sleep for 3 seconds.
    time.sleep(3)


# Draws final score screen and ask for quite or restart.
def you_lost_screen():
    global score

    # Fade out sounds.
    fadeout_all_sounds()

    # Fade out the screen.
    screen_fade_out(SLACK_COLOR)

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

    screen.blit(final_font2.render("Your final score: " + str(score), 1, RED_COLOR), (230, 240))
    screen.blit(final_font1.render("'Q' to Quit | 'R' to Restart", 1, YELLOW_COLOR), (200, 340))

    # Start final background music.
    background_sound(final_bg_sound)

    pygame.display.update()

    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_q:
                return True
            elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_r:
                fadeout_all_sounds()
                draw_title()

                return False


def you_won_screen():
    global score
    # Fade out sounds.
    fadeout_all_sounds()

    # Fade out the screen.
    screen_fade_out(SLACK_COLOR)
    lines = [
        " __ __            _ _ _",
        "|  |  |___ _ _   | | | |___ ___",
        "|_   _| . | | |  | | | | . |   |",
        "  |_| |___|___|  |_____|___|_|_|"
    ]
    x = 180
    y = 50

    screen.fill(SLACK_COLOR)

    for line in lines:
        screen.blit(final_font1.render(line, 1, mk_random_color()), (x, y))
        y += 15

    screen.blit(final_font2.render("Your final score: " + str(score), 1, RED_COLOR), (230, 240))
    screen.blit(final_font1.render("'Q' to Quit | 'R' to Restart", 1, YELLOW_COLOR), (200, 340))

    # Start final background music.
    background_sound(you_won_sound)

    pygame.display.update()

    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_q:
                return True
            elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_r:
                return False


# Draws the player.
def draw_player(lvl):
    pygame.draw.rect(screen, lvl.player_color, (player_x, 450, 20, 20))  # Base.
    pygame.draw.line(screen, lvl.player_color, [player_x + 9, 450], [player_x + 9, 435], 5)  # Turret.


# Resets the game data for the game.
def reset_data():
    global lives, ammo, score, bricks, rockets, explosions
    global used_red_bricks, used_white_bricks, used_green_bricks
    global used_bricks, level_completion

    lives = init_lives
    ammo = init_ammo
    score = 0
    bricks = []
    rockets = []
    explosions = []
    used_bricks = 0
    used_green_bricks = 0
    used_white_bricks = 0
    used_red_bricks = 0
    used_bricks = 0
    level_completion = 0


def is_joy_left():
    return round(joystick.get_axis(0)) == -1


def is_joy_right():
    return round(joystick.get_axis(0)) == 1


def is_joy_fire():
    return round(joystick.get_button(0)) == 1


# Plays given level.
def play_level(lvl):
    global ammo, bricks, rockets, explosions, used_bricks, level_completion
    global used_red_bricks, used_white_bricks, used_green_bricks

    bricks = []
    rockets = []
    explosions = []
    ammo = init_ammo
    used_green_bricks = 0
    used_white_bricks = 0
    used_red_bricks = 0
    used_bricks = 0
    level_completion = 0

    background_sound(lvl.bg_sound)

    intro_ani = True

    x = 0
    y = 0
    w = screen_width
    h = screen_height

    # Intro-animation: shrinking black rectangle.
    while intro_ani:
        # Clear the screen.
        screen.fill(lvl.bg_color)

        # Draw the scene elements.
        for scene_elem in lvl.scene_elements:
            scene_elem.draw(screen)

        draw_header(lvl)

        pygame.draw.rect(screen, DARK_GREY_COLOR, (x, y, w, h))

        w -= 30  # Shrink faster horizontally since screen isn't perfect square.
        h -= 20
        x += 15  # Shrink faster horizontally since screen isn't perfect square.
        y += 10

        # Quite loop when rectangle covers all screen.
        if w <= 0 and h <= 0:
            intro_ani = False

        pygame.event.get()
        pygame.display.update()

        clock.tick(fps)

    left = 0
    right = 0
    game_over = False

    # Main level loop.
    while level_completion < 100 and not game_over:
        if lives <= 0 or ammo <= 0:
            game_over = True

        if not game_over:
            # Clear the screen.
            screen.fill(lvl.bg_color)

            # Draw the scene elements.
            for scene_elem in lvl.scene_elements:
                scene_elem.draw(screen)

            for event in pygame.event.get():
                typ = event.type

                if typ == pygame.QUIT:
                    end_game()
                elif typ == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # Fire new rocket.
                    fire_rocket()
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
                elif typ == pygame.JOYBUTTONDOWN and joystick is not None:
                    if is_joy_fire():
                        fire_rocket()

                elif typ == pygame.JOYAXISMOTION and joystick is not None:
                    if is_joy_left():
                        left = 1
                        right = 0
                    elif is_joy_right():
                        left = 0
                        right = 1
                    else:
                        left = 0
                        right = 0

            if left == 1:
                move_player_left()
            elif right == 1:
                move_player_right()

            # Check bricks and rockets for collision.
            check_bricks_rockets()

            # Randomly place new bricks.
            add_new_bricks(lvl)

            draw_header(lvl)
            draw_player(lvl)
            draw_bricks()
            draw_rockets()
            draw_explosions()

            level_completion = math.floor((used_bricks / lvl.total_bricks) * 100)

            # Update (refresh) screen.
            pygame.display.update()

            # Wait for FPS.
            clock.tick(fps)

    return game_over


def main_game_loop():
    while True:
        player_died = False

        # Play all levels or until the end.
        for lvl in levels:
            switch_to_level(lvl)

            player_died = play_level(lvl)

            if player_died:
                break

        # Fade out all sounds.
        fadeout_all_sounds()

        # Draw final score.
        if player_died:
            end_it = you_lost_screen()
        else:
            end_it = you_won_screen()

        if end_it:
            # End the game.
            end_game()
        else:
            # Clear data.
            reset_data()


draw_title()
main_game_loop()

