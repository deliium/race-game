from .const import *
from .decorators import check_move


class Player(object):
    def __init__(self, track):
        self.track = track
        self.coords = PLAYER_COORDS
        self.direction = None

    def attach(self):
        for i in range(len(self.coords)):
            if self.track.tiles[self.coords[i][0]][self.coords[i][1]] == TILE_ID_GROUND:
                self.track.tiles[self.coords[i][0]][self.coords[i][1]] = TILE_ID_PLAYER
            else:
                print("GAME OVER")

    def detach(self):
        for i in range(len(self.coords)):
            self.track.tiles[self.coords[i][0]][self.coords[i][1]] = TILE_ID_GROUND

    @check_move
    def move(self):
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
