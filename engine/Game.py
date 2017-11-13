from .ResourceManager import ResourceManager
from .const import *


class Game(object):
    def __init__(self,
                 width=800,
                 height=600,
                 scene=None,
                 color=BACKGROUND_COLOR,
                 fps=40,
                 manager=ResourceManager()):
        """
        Game main class. Game loop starts here
        :param width: window width
        :param height: window height
        :param scene: main scene to start game
        :param color: use for background
        :param fps: use for snap game loop for time
        :param manager: use for load resources
        """
        pygame.init()

        self.__display = None
        self.set_display(width, height)

        self.fps = fps
        self.scene = scene
        self.__manager = manager

        self.__display.fill(color)
        pygame.display.flip()

    def set_display(self, width, height):
        """
        Set initial size to game window
        :param width: window width
        :param height: window height
        :return: None
        """
        self.__display = pygame.display.set_mode((width, height))

    def set_caption(self, title=None, icon=None):
        """
        Set caption to game window
        :param title: caption text
        :param icon: window icon
        :return: None
        """
        pygame.display.set_caption(title if title is not None else "Game")

        if icon is not None:
            pygame.display.set_icon(self.__manager.get_image(icon))

    def main_loop(self):
        """
        Game loop, all actions start here
        :return: None
        """
        while self.scene is not None:
            clock = pygame.time.Clock()
            dt = 0

            # init scene, set canvas and resource manager
            self.scene.start(self.__display, self.__manager)

            while not self.scene.is_end():
                # say to scene how much time has passed
                self.scene.loop(dt)

                pygame.display.flip()

                dt = clock.tick(self.fps)

            self.scene = self.scene.next()

        pygame.quit()
