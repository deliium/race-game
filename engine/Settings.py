import shelve
from engine.const import *


class Settings(object):
    @staticmethod
    def save(settings):
        d = shelve.open(SETTINGS_FILE)
        for key in settings:
            d[key] = settings[key]
        d.close()

    @staticmethod
    def load():
        result = {}
        d = shelve.open(SETTINGS_FILE)
        try:
            result['full_screen'] = d['full_screen']
        except KeyError:
            result['full_screen'] = False

        try:
            result['full_screen_width'] = d['full_screen_width']
            result['full_screen_height'] = d['full_screen_height']
        except KeyError:
            info = pygame.display.Info()
            result['full_screen_width'] = info.current_w
            result['full_screen_height'] = info.current_h

        d.close()
        return result
