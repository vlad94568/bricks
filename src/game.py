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

import pygame

from src.scene.rocket import *


# Global game data holder.
class Game:
    def __init__(self,
                 init_lives,
                 init_ammo,
                 title_sound,
                 end_sound,
                 levels,
                 mixer
                 ):
        self.mixer = mixer
        self.score = 0
        self.ammo = init_ammo
        self.lives = init_lives
        self.is_joystick_found = self.detect_joystick()  # Auto-detect joystick at the start.
        self.title_sound = title_sound
        self.end_sound = end_sound
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.levels = levels
        self.lvl_idx = 0
        self.fps = 30
        self.player_x = screen_width / 2 - 10

    # Fires the rocket.
    def fire_rocket(self, lvl):
        # Add new rocket.
        lvl.add_rocket(Rocket(self.player_x + 7, screen_height - 40))

        # Decrease ammo.
        self.ammo -= 1

        # BANG!
        self.mixer.rocket_sound()

    # Clears & resets all internal game data.
    def reset_data(self):
        ()  # TODO

    # Moved player X coordinate left.
    def move_player_left(self):
        self.player_x -= 8

        # Roll around the screen.
        if self.player_x < -20:
            self.player_x = screen_width

    # Moved player X coordinate right.
    def move_player_right(self):
        self.player_x += 8

        # Roll around the screen.
        if self.player_x > screen_width:
            self.player_x = 0

    # Ticks FPS clock.
    def tick_clock(self):
        self.clock.tick(self.fps)

    # Draws the player.
    def draw_player(self, lvl):
        pygame.draw.rect(self.screen, lvl.player_color, (self.player_x, 450, 20, 20), 5)  # Base.
        pygame.draw.line(self.screen, lvl.player_color, [self.player_x + 9, 450], [self.player_x + 9, 435], 5)  # Turret.

    # Detects if supported joystick is found.
    @staticmethod
    def detect_joystick():
        is_joystick_found = False

        joystick_count = pygame.joystick.get_count()

        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            # Get the name from the OS for the controller/joystick
            name = joystick.get_name()

            if name.startswith("USB,2-axis 8-button gamepad"):
                is_joystick_found = True

        return is_joystick_found

