import pygame


class SpriteAnimation(object):
    def __init__(self, time=2000, show=True):
        """
        Makes transparent animation
        :param time: delay while animation works
        :param show: is animation will be shows
        """
        self.show = show
        self.set_time(time)
        self.run = False

    def update(self, dt):
        """
        Update animation by time
        :param dt: time interval pass from previous call
        :return: None
        """
        if self.run:
            self.add += float(dt) * self.time
            if int(self.add) > 0:
                self.count += int(self.add)
                self.add = self.add - int(self.add)
                if self.count > 255:
                    self.count = 255
                    self.run = False

    def start(self):
        """
        Start animation from beginning
        :return: None
        """
        self.count = 0
        self.add = float(0)
        self.run = True

    def is_start(self):
        """
        Tell, is animation starting
        :return: Boolean
        """
        return self.run

    def stop(self):
        """
        Stop animation works
        :return: None
        """
        self.run = False

    def set_time(self, time=2000):
        """
        Set animation time duration
        :param time: time, during which animation will be works
        :return: None
        """
        self.time = float(255) / float(time)

    def get_sprite(self, sprite):
        """
        Return animation sprite for next drawing
        :param sprite: sprite for changing in next state
        :return: sprite in new state
        """
        sprite_copy = sprite.copy()
        if self.show:
            sprite_copy.fill((0, 0, 0, 255 - self.count), None, pygame.BLEND_RGBA_SUB)
        else:
            sprite_copy.fill((0, 0, 0, self.count), None, pygame.BLEND_RGBA_SUB)

        return sprite_copy

    def toggle(self):
        """
        Toggle animation show state
        :return: None
        """
        self.show = not self.show
