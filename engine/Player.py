from .ResourceManager import ResourceManager
from .const import *


class Player(object):
    def __init__(self, field):
        manager = ResourceManager()
        self.tileset = manager.get_image("tileset.bmp")

        self.field = field
        self.player = PLAYER_COORDS

        self.direction = None

    def put_to_field(self):
        for i in range(len(self.player)):
            if 0 < self.player[i][0] < self.field.tiles_x and 0 < self.player[i][1] < self.field.tiles_y:
                self.field.tiles[self.player[i][0], self.player[i][1]] = TILE_ID_PLAYER
            else:
                # TODO collision reaction
                pass

    def remove_from_field(self):
        for i in range(len(self.player)):
            self.field.tiles[self.player[i][0], self.player[i][1]] = TILE_ID_GROUND
    
    def move(self, direction):
        self.direction = direction

        self.remove_from_field()

        # TODO move player

        self.put_to_field()
