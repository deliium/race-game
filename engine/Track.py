from engine.const import *


class Track(object):
    def __init__(self):
        """
        Track, where Player meets Enemies
        """
        self.tiles_x, self.tiles_y = TILE_X_COUNT, TILE_Y_COUNT
        self.tiles = [[0 for _ in range(self.tiles_y)] for _ in range(self.tiles_x)]

        self.step = 0
        self.speed = 1
        self.level = 1
        self.clear()

    def clear(self):
        """
        Make track clean with ground tiles
        :return: None
        """
        for x in range(self.tiles_x):
            for y in range(self.tiles_y):
                self.tiles[x][y] = TILE_ID_GROUND

    def border_line(self, x):
        """
        Make border line for track
        :param x: border position
        :return: None
        """
        for y in range(self.tiles_y):
            self.tiles[x][y] = TILE_ID_GROUND if (y % (BORDER_HEIGHT+1)) - self.step == 0 else TILE_ID_WALL

    def move(self):
        """
        Make track move for next step
        :return: None
        """
        self.step = 0 if self.step >= BORDER_HEIGHT else self.step + 1

        for x in range(1, self.tiles_x-1):
            self.tiles[x].insert(0, 0)
            self.tiles[x] = self.tiles[x][:-1]

        self.border_line(0)
        self.border_line(TILE_X_COUNT - 1)

    def get_speed(self):
        return 1 if self.speed < 1 else self.speed
