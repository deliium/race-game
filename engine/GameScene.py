from pygame import Rect
import numpy as np
import threading
import time

from .Player import Player
from .Scene import Scene
from .ResourceManager import ResourceManager
from .const import *


class GameScene(Scene):
    """ Store game field and draw tiles """
    def _start(self):
        self.tileset = ResourceManager().get_image("tileset.bmp")

        self.tiles_x, self.tiles_y = TILE_X_COUNT, TILE_Y_COUNT
        self.tiles = np.zeros((self.tiles_x, self.tiles_y), dtype=int)
        self.player = Player(self)

        self.step = 0
        self.sleep_time = .3
        t = threading.Thread(target=self.update_step)
        t.start()

    def update_step(self):
        while not self.is_end():
            self.step += 1
            if self.step >= BORDER_HEIGHT+1:
                self.step = 0
            self.make_level()
            self.player.put_to_field()
            time.sleep(self.sleep_time)

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
        self.draw_border_line(0)
        self.draw_border_line(TILE_X_COUNT-1)

    def draw_border_line(self, x):
        for y in range(self.tiles_y):
            if (y % (BORDER_HEIGHT+1)) - self.step == 0:
                self.tiles[x, y] = TILE_ID_GROUND
            else:
                self.tiles[x, y] = TILE_ID_WALL

    def _draw(self, dt):
        self.display.fill(BACKGROUND_COLOR)
        for x in range(self.tiles_x):
            for y in range(self.tiles_y):
                # Draw tile in (x,y)
                # get rect() area; select tile from tileset
                dest = Rect(x * TILE_WIDTH, y * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
                src = Rect(self.tiles[x, y] * TILE_WIDTH, 0, TILE_WIDTH, TILE_HEIGHT)

                self.display.blit(self.tileset, dest, src)