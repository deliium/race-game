import os

import pygame


class ResourceManager:
    def __init__(self,
                 data_dir='data',
                 image_dir='image',
                 sound_dir='sound',
                 music_dir='music'):
        """
        Makes resource access
        :param data_dir: place, where all the data stored
        :param image_dir: place, where all the images stored
        :param sound_dir: place, where all the sounds stored
        :param music_dir: place, where all the music stored
        """
        # Каталог ресурсов
        self.data_dir = data_dir
        # Изображения
        self.image_dir = image_dir
        # Звуки
        self.sound_dir = sound_dir
        # Музыка
        self.music_dir = music_dir

    def get_image(self, name):
        """
        Load image by name
        :param name: Image name
        :return: Image in pygame format
        """
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

    def get_sound(self, name):
        """
        Load sound by name
        :param name: Sound file name
        :return: Sound in pygame format
        """
        fullname = os.path.join(self.data_dir,
                                os.path.join(self.sound_dir, name))

        try:
            sound = pygame.mixer.Sound(fullname)
        except pygame.error:
            print('Error while loading sound {0}'.format(name))
            raise SystemExit(1)

        return sound

    def get_music(self, name):
        """
        Load music by name
        :param name: Music file name
        :return: Music in pygame format
        """
        fullname = os.path.join(self.data_dir,
                                os.path.join(self.music_dir, name))

        try:
            music = pygame.mixer.Sound(fullname)
        except pygame.error:
            print('Error while loading sound {0}'.format(name))
            raise SystemExit(1)

        return music
