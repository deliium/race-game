import shelve
from engine.decorators import singleton
from engine.const import *


@singleton
class Settings(object):
    def __init__(self):
        self.items = {}
        self.load()

    def save(self):
        d = shelve.open(SETTINGS_FILE)
        for key in self.items:
            d[key] = self.items[key]
        d.close()

    def load(self):
        d = shelve.open(SETTINGS_FILE)
        try:
            self.items['full_screen'] = d['full_screen']
        except KeyError:
            self.items['full_screen'] = False

        try:
            self.items['music'] = d['music']
        except KeyError:
            self.items['music'] = False

        try:
            self.items['full_screen_width'] = d['full_screen_width']
            self.items['full_screen_height'] = d['full_screen_height']
        except KeyError:
            info = pygame.display.Info()
            self.items['full_screen_width'] = info.current_w
            self.items['full_screen_height'] = info.current_h

        d.close()

    def get_display(self):
        """ get pygame.display with mode settings
        :return: pygame.display
        """
        if self.items['full_screen']:
            width = self.items['full_screen_width']
            height = self.items['full_screen_height']
            return pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        else:
            return pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT))

    def get_fps(self):
        """ get game fps
        :return: fps value
        """
        return DEFAULT_FPS

    def __getitem__(self, key):
        try:
            value = self.items[key]
        except KeyError:
            value = None
        return value

    def __setitem__(self, key, value):
        self.items[key] = value
