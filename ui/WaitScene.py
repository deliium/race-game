import pygame
from .Scene import Scene


class WaitScene(Scene):
    def __init__(self, time=1000, *argv):
        """
        Init and start new wait scene
        :param time: live time for this scene
        :param argv: all args for base Scene class
        """
        Scene.__init__(self, *argv)
        self.run = 0
        self.time = time

    def _event(self, event):
        """
        Make event handle
        :param event: any occurred event
        :return: None
        """
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                self.the_end()

        if not self.run < self.time:
            self.the_end()

    def _update(self, dt):
        """
        Update Scene state
        :param dt: time interval pass from previous call
        :return: None
        """
        self.run += dt
