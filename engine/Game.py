from ui.LogoScene import LogoScene
from ui.MenuScene import MenuScene, PauseScene
from ui.SettingsScene import SettingsScene
from ui.ScoreScene import ScoreScene
from ui.GameScene import GameScene
from ui.GameOverScene import GameOverScene
from .Settings import Settings
from .ResourceManager import ResourceManager
from .const import *


class Game(object):
    def __init__(self,
                 width=DEFAULT_WIDTH,
                 height=DEFAULT_HEIGHT,
                 color=BACKGROUND_COLOR,
                 fps=40,
                 manager=ResourceManager()):
        """
        Game main class. Game loop starts here
        :param width: window width
        :param height: window height
        :param color: use for background
        :param fps: use for snap game loop for time
        :param manager: use for load resources
        """
        pygame.init()

        self.settings = Settings()
        self.settings.load()

        self.__display = None
        self.set_display(width, height)

        self.fps = fps
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
        self.__manager = manager

        self.__display.fill(color)
        pygame.display.flip()

    def flip_scene(self):
        """
        Switch to the next scene
        :return: None
        """
        self.previous_scene_name = self.scene_name
        self.scene_name = self.scene.next()
        self.scene = self.scenes[self.scene_name] if self.scene_name is not None else None

    def set_display(self, width, height):
        """Set initial size to game window
        :param width: window width
        :param height: window height
        :return: None
        """
        if self.settings['full_screen']:
            width = self.settings['full_screen_width']
            height = self.settings['full_screen_height']
            self.__display = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        else:
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
            if self.previous_scene_name == "pause" and self.scene_name == "game":
                self.scene.wake()
                self.scene.make_threads()
            else:
                self.scene.start(self.__display, self.__manager)

            while not self.scene.is_end():
                # say to scene how much time has passed
                self.scene.loop(dt)

                pygame.display.flip()

                dt = clock.tick(self.fps)

            self.flip_scene()

        pygame.quit()
