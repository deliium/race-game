from pygame import Rect
import threading
import time

from engine.Track import Track
from engine.Enemy import Enemy
from engine.Player import Player
from engine.const import *
from .Scene import Scene


class GameScene(Scene):
    def _start(self):
        self.tileset = self.manager.get_image("tileset.bmp")

        self.track = Track()
        self.enemy = Enemy(self.track)
        self.enemy.attach((0, 2))
        self.player = Player(self.track)
        self.player.attach()

        threading.Thread(target=self.update_track).start()
        threading.Thread(target=self.update_move).start()

    def update_track(self):
        while not self.is_end():
            self.player.detach()
            self.track.move()
            self.player.attach()
            time.sleep(TRACK_MOVE_SLEEP_TIME)

    def update_move(self):
        while not self.is_end():
            self.player.move()
            time.sleep(PLAYER_MOVE_SLEEP_TIME)

    def _event(self, event):
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_n:
                    self.enemy.attach((0, 2))
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

    def _draw(self, dt):
        self.display.fill(BACKGROUND_COLOR)

        for x in range(self.track.tiles_x):
            for y in range(self.track.tiles_y):
                # Draw tile in (x,y)
                # get rect() area; select tile from tileset
                dest = Rect(x * TILE_WIDTH, y * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
                src = Rect(self.track.tiles[x][y] * TILE_WIDTH, 0, TILE_WIDTH, TILE_HEIGHT)

                self.display.blit(self.tileset, dest, src)
