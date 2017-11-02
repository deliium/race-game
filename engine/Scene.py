from .const import *

"""
_foo() -> must override in descendants
"""

class Scene(object):
    def __init__(self, next_scene=None):
        self.display = None
        self.manager = None
        self.__end = None
        self.__next_scene = next_scene

    def loop(self, dt):
        self.__event(pygame.event)
        self._update(dt)
        self._draw(dt)

    def start(self, display, manager):
        self.display = display
        self.manager = manager
        self._start()
        self.__end = False

    def _start(self):
        pass

    def __event(self, event):
        if len(event.get(pygame.QUIT)) > 0:
            self.__end = True
            self.set_next_scene(None)
            return

        self._event(event)

        for e in event.get(END_SCENE):
            if e.type == END_SCENE:
                self.__end = True

    def _draw(self, dt):
        pass

    def _event(self, event):
        pass

    def _update(self, dt):
        pass

    def next(self):
        return self.__next_scene

    def is_end(self):
        return self.__end

    def the_end(self):
        pygame.event.post(pygame.event.Event(END_SCENE))

    def set_next_scene(self, scene):
        self.__next_scene = scene
