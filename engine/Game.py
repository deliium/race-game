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
        pygame.init()

        self.__display = None
        self.set_display(width, height)

        self.fps = fps
        self.scene = scene
        self.__manager = manager

        self.__display.fill(color)
        pygame.display.flip()

    def set_display(self, width, height):
        self.__display = pygame.display.set_mode((width, height))

    def set_caption(self, title=None, icon=None):
        pygame.display.set_caption(title if title is not None else "Game")

        if icon is not None:
            pygame.display.set_icon(self.__manager.get_image(icon))

    def main_loop(self):
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
