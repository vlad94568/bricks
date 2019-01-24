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


# Explosion container.
class Explosion:
    def __init__(self, frags):
        self.frags = frags

    def is_done(self):
        return self.frags[0].frame_cnt == 30

    # Draws explosion (i.e. its fragments).
    def draw(self, screen):
        for frag in self.frags:
            frag.draw(screen)
