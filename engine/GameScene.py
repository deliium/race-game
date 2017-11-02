from pygame import Rect
import numpy as np

from .Player import Player
from .Scene import Scene
from .ResourceManager import ResourceManager
from .const import *


class GameScene(Scene):
    """ Store game field and draw tiles """
    
    def _start(self):
        manager = ResourceManager()
        self.tileset = manager.get_image("tileset.bmp")

        self.tiles_x, self.tiles_y = TILE_X_COUNT, TILE_Y_COUNT

        self.tiles = np.zeros((self.tiles_x, self.tiles_y), dtype=int)
        self.make_level()

        self.player = Player(self)
        self.player.put_to_field()

    def _event(self, event):
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    self.the_end()
                elif e.key == pygame.K_LEFT:
                    self.player.move("left")
                elif e.key == pygame.K_RIGHT:
                    self.player.move("right")

    def make_level(self):
        for x in range(self.tiles_x):
            for y in range(self.tiles_y):
                self.tiles[x, y] = TILE_ID_GROUND

    def _draw(self, dt):
        self.display.fill(BACKGROUND_COLOR)
        for x in range(self.tiles_x):
            for y in range(self.tiles_y):
                # Draw tile in (x,y)
                # get rect() area; select tile from tileset
                dest = Rect(x * TILE_WIDTH, y * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
                src = Rect(self.tiles[x, y] * TILE_WIDTH, 0, TILE_WIDTH, TILE_HEIGHT)

                self.display.blit(self.tileset, dest, src)

