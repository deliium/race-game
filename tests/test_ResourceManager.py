import inspect
import os
import sys

import pygame

from engine.ResourceManager import ResourceManager

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


manager = ResourceManager()


def test_answer():
    pygame.init()
    pygame.display.set_mode((800, 600))
    assert manager.get_image("icon.png") is not None
