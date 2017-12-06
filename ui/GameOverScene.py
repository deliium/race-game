from .Scene import Scene
from engine.const import *


class GameOverScene(Scene):
    def _start(self):
        """
        Init and start new Menu scene
        :return: None
        """
        self.font = pygame.font.SysFont("Monospace", 40, bold=False, italic=False)

    def _event(self, event):
        """
        Make event handle
        :param event: any occurred event
        :return: None
        """
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    self.set_next_scene("menu")
                    self.the_end()

    def _draw(self, dt):
        """
        Draw current scene state
        :param dt: time interval pass from previous call
        :return: None
        """
        self.display.blit(self.font.render("Игра закончена", True, (0, 0, 0)), (400, 300))

