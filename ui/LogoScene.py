import pygame
from engine import const
from .Scene import Scene
from engine.SpriteAnimation import SpriteAnimation


class LogoScene(Scene):
    def _start(self):
        """
        Init new logo scene
        :return: None
        """
        self.sprite = self.manager.get_image('logo.png')
        self.logo = SpriteAnimation(3000)
        self.logo.start()

    def _event(self, event):
        """
        Handles event
        :param event: any occurred event
        :return: None
        """
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                self.set_next_scene("menu")
                self.the_end()

        if not self.logo.is_start():
            self.set_next_scene("menu")
            self.the_end()

    def _update(self, dt):
        """
        Update scene by time
        :param dt: time interval pass from previous call
        :return: None
        """
        self.logo.update(dt)

    @staticmethod
    def get_center(surface, sprite):
        """
        Return drawing start point for sprite to set him on surface center
        :param surface: drawing place
        :param sprite: sprite, which will be drawing
        :return:
        """
        return ((surface.w - sprite.w) / 2,
                (surface.h - sprite.h) / 2)

    def _draw(self, dt):
        """
        Draw current scene state
        :param dt: time interval pass from previous call
        :return: None
        """
        self.display.fill(const.BACKGROUND_COLOR)
        # Draw logo with sprite animation
        self.display.blit(self.logo.get_sprite(self.sprite),
                          self.get_center(self.display.get_rect(),
                          self.sprite.get_rect()))