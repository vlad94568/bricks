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


# Sound mixer channels:
# 0 - background (title and main game)
# 1 - rocket fire
# 2 - brick air-kill (killed by rocket)
# 3 - brick ground-kill (reached the bottom)
class SoundMixer:
    def __init__(self):
        self.rocket_fire_sound = pygame.mixer.Sound("sounds/rocket_fired.ogg")
        self.brick_kill_sound = pygame.mixer.Sound("sounds/brick_kill.ogg")
        self.brick_squish_sound = pygame.mixer.Sound("sounds/brick_squished.ogg")

    # Sounds kill of the brick.
    def boom_sound(self):
        pygame.mixer.Channel(2).play(self.brick_kill_sound)

    # Sounds the brick hitting the bottom.
    def squish_sound(self):
        pygame.mixer.Channel(3).play(self.brick_squish_sound)

    # Sounds the rocket firing.
    def rocket_sound(self):
        pygame.mixer.Channel(1).set_volume(0.3)
        pygame.mixer.Channel(1).play(self.rocket_fire_sound)

    # Fades out all channels.
    @staticmethod
    def fadeout_all():
        pygame.mixer.Channel(0).fadeout(2000)
        pygame.mixer.Channel(1).fadeout(2000)
        pygame.mixer.Channel(2).fadeout(2000)
        pygame.mixer.Channel(3).fadeout(2000)

    # Stops all sounds.
    @staticmethod
    def stop_all():
        pygame.mixer.stop()

    # Plays background sound (channel 0).
    @staticmethod
    def background_sound(sound):
        pygame.mixer.Channel(0).play(sound, -1)