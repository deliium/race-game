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

        self.track_step = 0
        self.track_sleep_time = .3
        threading.Thread(target=self.update_track).start()

        self.move_sleep_time = .1
        threading.Thread(target=self.update_move).start()

    def update_track(self):
        while not self.is_end():
            self.track_step = 0 if self.track_step >= BORDER_HEIGHT else self.track_step + 1
            self.make_level()
            time.sleep(self.track_sleep_time)

    def update_move(self):
        while not self.is_end():
            self.player.move()
            time.sleep(self.move_sleep_time)

    def _event(self, event):
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    self.the_end()
                elif e.key == pygame.K_LEFT:
                    self.player.direction = "left"
                    self.player.move()
                elif e.key == pygame.K_RIGHT:
                    self.player.direction = "right"
                    self.player.move()
            elif e.type == pygame.KEYUP:
                self.player.direction = None

    def make_level(self):
        for x in range(self.tiles_x):
            for y in range(self.tiles_y):
                self.tiles[x, y] = TILE_ID_GROUND
        self.player.put_to_field()
        self.draw_border_line(0)
        self.draw_border_line(TILE_X_COUNT-1)

    def draw_border_line(self, x):
        for y in range(self.tiles_y):
            self.tiles[x, y] = TILE_ID_GROUND if (y % (BORDER_HEIGHT+1)) - self.track_step == 0 else TILE_ID_WALL

    def _draw(self, dt):
        self.display.fill(BACKGROUND_COLOR)
        for x in range(self.tiles_x):
            for y in range(self.tiles_y):
                # Draw tile in (x,y)
                # get rect() area; select tile from tileset
                dest = Rect(x * TILE_WIDTH, y * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
                src = Rect(self.tiles[x, y] * TILE_WIDTH, 0, TILE_WIDTH, TILE_HEIGHT)

                self.display.blit(self.tileset, dest, src)