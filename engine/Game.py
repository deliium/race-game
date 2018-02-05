from ui.GameOverScene import GameOverScene
from ui.GameScene import GameScene
from ui.LogoScene import LogoScene
from ui.MenuScene import MenuScene, PauseScene
from ui.ScoreScene import ScoreScene
from ui.SettingsScene import SettingsScene

from .const import *
from .ResourceManager import ResourceManager
from .Settings import Settings


class Game(object):
    def __init__(self):
        """
        Game main class. Game loop starts here
        """
        pygame.init()

        self.settings = Settings()

        self.scenes = {"menu": MenuScene(),
                       "settings": SettingsScene(),
                       "score": ScoreScene(),
                       "game": GameScene(),
                       "pause": PauseScene(),
                       "game_over": GameOverScene(),
                       "logo": LogoScene()}
        self.scene_name = "logo"  # start scene
        self.previous_scene_name = None
        self.scene = self.scenes[self.scene_name]

        self.__manager = ResourceManager()
        self.__display = self.settings.get_display()
        self.__display.fill(BACKGROUND_COLOR)
        pygame.display.flip()

    def flip_scene(self):
        """
        Switch to the next scene
        :return: None
        """
        self.previous_scene_name = self.scene_name
        self.scene_name = self.scene.next()
        self.scene = self.scenes[self.scene_name] if self.scene_name is not None else None

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
            if self.previous_scene_name == "pause" and self.scene_name == "game":
                self.scene.wake()
                self.scene.make_threads()
            else:
                self.scene.start(self.__display, self.__manager)

            while not self.scene.is_end():
                # say to scene how much time has passed
                self.scene.loop(dt)

                pygame.display.flip()

                dt = clock.tick(self.settings.get_fps())

            self.flip_scene()

        pygame.quit()
