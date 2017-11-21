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
        """
        Init and start new game scene
        :return: None
        """
        self.tileset = self.manager.get_image("tileset.bmp")

        self.track = Track()
        self.enemy = Enemy(self.track)
        self.enemy.attach((0, 2))
        self.player = Player(self.track)
        self.player.attach()
        self.font = pygame.font.SysFont("Monospace", 40, bold=False, italic=False)

        threading.Thread(target=self.update_track).start()
        threading.Thread(target=self.update_move).start()

    def update_track(self):
        """
        Updating track for next game state
        :return: None
        """
        while not self.is_end():
            if self.player.is_dead:
                # TODO need to stop game now
                print("GAME OVER")
            self.player.detach()
            self.track.move()
            self.player.attach()
            self.player.score += 1
            if self.player.score % 50 == 0:
                self.track.speed += 1
            time.sleep(TRACK_MOVE_SLEEP_TIME)

    def update_move(self):
        """
        Update player move, handles player position on track
        :return: None
        """
        while not self.is_end():
            self.player.move()
            time.sleep(PLAYER_MOVE_SLEEP_TIME)

    def _event(self, event):
        """
        Make event handle
        :param event: any occurred event
        :return: None
        """
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_n:
                    self.enemy.attach((0, 2))
                elif e.key == pygame.K_p:
                    self.set_next_scene(WaitScene())
                elif e.key == pygame.K_ESCAPE:
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
        """
        Redraw game by current status
        :param dt: time interval pass from previous call
        :return: None
        """
        windows_width, windows_height = pygame.display.get_surface().get_size()
        window_half_width = windows_width / 2
        tile_size = self.calculate_tile_size(windows_height, window_half_width)

        self.display.fill(BACKGROUND_COLOR)
        self.draw_field(tile_size)
        self.draw_score(window_half_width, tile_size)

    def calculate_tile_size(self, field_height, field_width):
        tile_calculated_height = field_height / self.track.tiles_y
        tile_calculated_width = field_width / self.track.tiles_x
        tile_size = tile_calculated_width if tile_calculated_height > tile_calculated_width else tile_calculated_height
        return tile_size

    def draw_field(self, tile_size):
        margin = 1
        scaled_tile = pygame.transform.scale(self.tileset, (int((tile_size - margin) * 2), int(tile_size - margin)))

        for x in range(self.track.tiles_x):
            for y in range(self.track.tiles_y):
                # Draw tile in (x,y)
                # get rect() area; select tile from tileset
                destination = Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                src = Rect(self.track.tiles[x][y] * tile_size, 0, tile_size - margin, tile_size - margin)
                self.display.blit(scaled_tile, destination, src)

    def draw_score(self, window_half_width, tile_size):
        self.display.blit(self.font.render("Счёт: " + str(self.player.score), True, (0, 0, 0)),
                          (window_half_width + tile_size, tile_size))
        self.display.blit(self.font.render("Скорость: " + str(self.track.speed), True, (0, 0, 0)),
                          (window_half_width + tile_size, tile_size * 2))
        self.display.blit(self.font.render("Жизней: " + str(self.player.lives_count), True, (0, 0, 0)),
                          (window_half_width + tile_size, tile_size * 3))