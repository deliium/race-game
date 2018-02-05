from pygame import Rect
import threading
import time
import random

from engine.Track import Track
from engine.Enemy import Enemy
from engine.Player import Player
from engine.Animation import Animation
from engine.Settings import Settings
from engine.const import *
from .ScoreScene import ScoreScene
from .Scene import Scene


class GameScene(Scene):
    def _start(self):
        """
        Init and start new game scene
        :return: None
        """
        self.tileset = self.manager.get_image("tileset.bmp")
        self.main_theme_music = self.manager.get_music("main-theme.ogg")
        self.explosion_sound = self.manager.get_sound("boom.ogg")

        self.track = Track()
        self.enemy = Enemy(self.track)
        self.player = Player(self.track)
        self.player.attach()
        self.explosion_sprite_size = 192
        self.explosion_speed = 4
        self.explosion = Animation(self.manager.get_image("explosion.png"),
                                   self.explosion_sprite_size,
                                   self.explosion_sprite_size,
                                   self.explosion_speed)
        self.is_explosion_started = False
        self.settings = Settings()
        self.font = pygame.font.SysFont("Monospace", 40, bold=False, italic=False)
        self.make_threads()

    def make_threads(self):
        """
        Start threads to change game state
        :return: None
        """
        threading.Thread(target=self.update_track).start()
        threading.Thread(target=self.update_move).start()
        if self.settings['music']:
            self.main_theme_music.play()

    def update_track(self):
        """
        Updating track for next game state
        :return: None
        """
        while not self.is_end():
            if not self.enemy.wait:
                self.enemy.attach(ENEMY_POSITIONS[random.randint(0, len(ENEMY_POSITIONS)-1)])
            self.enemy.wait = ENEMY_WAIT_FOR_NEXT if not self.enemy.wait else self.enemy.wait - 1

            if self.player.is_dead:
                ScoreScene.save(self.player.score)
                self.is_explosion_started = True
                self.player.detach()
                self.explosion.start()
                if self.settings['music']:
                    self.explosion_sound.play()
                break
            self.player.detach()
            self.track.move()
            self.player.attach()
            self.player.score += 1
            if self.player.score % (SPEED_INCREASE_SCORE * self.track.level) == 0:
                self.track.speed += 1
            if self.player.score % (LEVEL_INCREASE_SCORE * self.track.level) == 0:
                self.track.level += 1
                self.player.lives_count = int(self.player.lives_count * 1.7)
                self.track.speed = self.track.level

            track_sleep_time = TRACK_MOVE_SLEEP_TIME / self.track.get_speed()
            time.sleep(track_sleep_time)

    def update_move(self):
        """
        Update player move, handles player position on track
        :return: None
        """
        while not self.is_end():
            if self.player.is_dead:
                break
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
                if e.key == pygame.K_p:
                    self.set_next_scene("pause")
                    self.the_end()
                elif e.key == pygame.K_ESCAPE:
                    ScoreScene.save(self.player.score)
                    self.set_next_scene("menu")
                    self.the_end()
                elif e.key == pygame.K_LEFT:
                    self.player.direction = "left"
                    self.player.move()
                elif e.key == pygame.K_RIGHT:
                    self.player.direction = "right"
                    self.player.move()
                elif e.key == pygame.K_UP:
                    self.track.speed += 1
                elif e.key == pygame.K_DOWN:
                    self.track.speed -= 1
            elif e.type == pygame.KEYUP:
                self.player.direction = None

    def _update(self, dt):
        """
        Update scene by time
        :param dt: time interval pass from previous call
        :return: None
        """
        if self.is_explosion_started:
            self.explosion.update(dt)
            if not self.explosion.is_start() and self.player.is_dead:
                self.set_next_scene("game_over")
                self.the_end()

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
        if self.explosion.is_start():
            player_center = [x - int(self.explosion_sprite_size / 2) for x in self.player.get_center(tile_size)]
            self.display.blit(self.explosion.sprite, player_center, self.explosion.get_coords())

    def the_end(self):
        self.main_theme_music.stop()
        super().the_end()

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
        self.display.blit(self.font.render("Уровень: " + str(self.track.level), True, (0, 0, 0)),
                          (window_half_width + tile_size, tile_size * 4))
