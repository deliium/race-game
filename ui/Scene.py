from engine.const import *


class Scene(object):
    def __init__(self, next_scene=None):
        """
        Base class for any scenes
        :param next_scene: scene be chosen when current scene is ended
        """
        self.display = None
        self.manager = None
        self.__end = None
        self.__next_scene = next_scene

    def loop(self, dt):
        """
        Loop scene routine
        :param dt: time interval pass from previous call
        :return: None
        """
        self.__event(pygame.event)
        self._update(dt)
        self._draw(dt)

    def start(self, display, manager):
        """
        Start scene routine
        :param display: game window
        :param manager: use for load resources
        :return:
        """
        self.display = display
        self.manager = manager
        self._start()
        self.__end = False

    def _start(self):
        """
        <!> must override in descendants
        Init and start new Scene
        :return: None
        """
        pass

    def __event(self, event):
        """
        Make some event handle
        :param event: any occurred event
        :return: None
        """
        if len(event.get(pygame.QUIT)) > 0:
            self.__end = True
            self.set_next_scene(None)
            return

        self._event(event)

        for e in event.get(END_SCENE):
            if e.type == END_SCENE:
                self.__end = True

    def _draw(self, dt):
        """
        <!> must override in descendants
        Redraw game by current status
        :param dt: time interval pass from previous call
        :return: None
        """
        pass

    def _event(self, event):
        """
        <!> must override in descendants
        Make event handle
        :param event: any occurred event
        :return: None
        """
        pass

    def _update(self, dt):
        """
        <!> must override in descendants
        Update Scene state
        :param dt: time interval pass from previous call
        :return: None
        """
        pass

    def next(self):
        """
        Getter for next scene
        :return: Next scene
        """
        return self.__next_scene

    def is_end(self):
        """
        Getter for current scene status
        :return: is current scene ended
        """
        return self.__end

    def the_end(self):
        """
        Do some stuff to make scene be ended
        :return: None
        """
        pygame.event.post(pygame.event.Event(END_SCENE))

    def set_next_scene(self, scene):
        """
        Set next scene to current scene
        :param scene: next scene
        :return: None
        """
        self.__next_scene = scene
