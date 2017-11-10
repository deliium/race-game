import pygame
from engine import const
from .Scene import Scene
from .MenuScene import MenuScene
from engine.SpriteAnimation import SpriteAnimation


class ShowLogoScene(Scene):
    def _start(self):
        self.sprite = self.manager.get_image('logo.png')
        self.logo = SpriteAnimation(3000)
        self.logo.start()

    def _event(self, event):
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                self.the_end()
                self.set_next_scene(MenuScene())

        if not self.logo.is_start():
            self.the_end()

    def _update(self, dt):
        self.logo.update(dt)

    def get_center(self, surface, sprite):
        """ Return drawing start point for sprite to set him on surface center """
        return ((surface.w - sprite.w) / 2,
                (surface.h - sprite.h) / 2)

    def _draw(self, dt):
        self.display.fill(const.BACKGROUND_COLOR)
        # Draw logo with sprite animation
        self.display.blit(self.logo.get_sprite(self.sprite),
                          self.get_center(self.display.get_rect(),
                          self.sprite.get_rect()))


class HideLogoScene(ShowLogoScene):
    def _start(self):
        ShowLogoScene._start(self)

        self.logo.toggle()
        self.logo.set_time(1000)
