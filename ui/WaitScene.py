import pygame
from .Scene import Scene


class WaitScene(Scene):
    def __init__(self, time=1000, *argv):
        Scene.__init__(self, *argv)
        self.run = 0
        self.time = time

    def _event(self, event):
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                self.the_end()

        if not self.run < self.time:
            self.the_end()

    def _update(self, dt):
        self.run += dt
