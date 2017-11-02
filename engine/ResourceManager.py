import os
import pygame


class ResourceManager:
    def __init__(self,
                 data_dir='data',
                 image_dir='image',
                 sound_dir='sound',
                 music_dir='music'):
        # Каталог ресурсов
        self.data_dir = data_dir
        # Изображения
        self.image_dir = image_dir
        # Звуки
        self.sound_dir = sound_dir
        # Музыка
        self.music_dir = music_dir

    def get_image(self, name):
        """ load image by name """
        fullname = os.path.join(self.data_dir,
                                os.path.join(self.image_dir, name))

        try:
            image = pygame.image.load(fullname)
        except pygame.error:
            print('Error while loading image {0}'.format(name))
            raise SystemExit(1)
        else:
            # use image with alpha channel
            image = image.convert_alpha()

        return image
