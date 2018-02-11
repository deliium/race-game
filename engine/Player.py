from copy import deepcopy

from .const import *
from .decorators import check_move


class Player(object):
    def __init__(self, track):
        """
        Make player for game
        :param track: place to put player
        """
        self.track = track
        self.coords = deepcopy(PLAYER_COORDS)
        self.direction = None
        self.score = 0
        self.lives_count = PLAYER_LIVES_COUNT
        self.invulnerability_time = INVULNERABILITY_TIME
        self.is_invulnerability = False
        self.is_dead = False

    def attach(self):
        """
        Insert player on track
        :return: None
        """
        for i in range(len(self.coords)):
            if self.track.tiles[self.coords[i][0]][self.coords[i][1]] == TILE_ID_GROUND:
                self.track.tiles[self.coords[i][0]][self.coords[i][1]] = TILE_ID_PLAYER
            elif self.track.tiles[self.coords[i][0]][self.coords[i][1]] == TILE_ID_BONUS_LIFE:
                self.lives_count += 1
            elif self.track.tiles[self.coords[i][0]][self.coords[i][1]] == TILE_ID_BONUS_SPEED:
                self.track.speed += 1
            elif self.track.tiles[self.coords[i][0]][self.coords[i][1]] == TILE_ID_BONUS_INVULNERABILITY:
                self.is_invulnerability = True
            elif self.track.tiles[self.coords[i][0]][self.coords[i][1]] == TILE_ID_ENEMY:
                if self.is_invulnerability:
                    if self.invulnerability_time == 0:
                        self.invulnerability_time = INVULNERABILITY_TIME
                        return
                    self.invulnerability_time -= 1
                else:
                    self.lives_count -= 1
                    if self.lives_count == 0:
                        self.is_dead = True

    def detach(self):
        """
        Remove player from track
        :return: None
        """
        for i in range(len(self.coords)):
            self.track.tiles[self.coords[i][0]][self.coords[i][1]] = TILE_ID_GROUND

    def get_center(self, tile_size):
        x = self.coords[PLAYER_CENTER][0] * (tile_size - 1) + int(tile_size/2)
        y = self.coords[PLAYER_CENTER][1] * (tile_size - 1) + int(tile_size/2)
        return x, y

    @check_move
    def move(self):
        """
        Make player move
        :return: None
        """
        if self.direction == "left":
            is_move = True
            for coord in self.coords:
                if coord[0] <= 1:
                    is_move = False
            if is_move:
                for i in range(len(self.coords)):
                    self.coords[i][0] -= 1
        elif self.direction == "right":
            is_move = True
            for coord in self.coords:
                if coord[0] >= TILE_X_COUNT-2:
                    is_move = False
            if is_move:
                for i in range(len(self.coords)):
                    self.coords[i][0] += 1
