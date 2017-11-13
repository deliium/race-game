from .const import *


class Enemy(object):
    def __init__(self, track):
        """
        Make enemy to kill player
        :param track: place to put enemy
        """
        self.track = track

    def attach(self, enemy_poses):
        """
        Put player at any coords
        :param enemy_poses: enemy position
        :return:
        """
        for enemy_pos in enemy_poses:
            coords = [[coord[0] + CAR_WIDTH*enemy_pos, coord[1]] for coord in ENEMY_COORS]

            for i in range(len(coords)):
                if 0 <= coords[i][0] < self.track.tiles_x and 0 <= coords[i][1] < self.track.tiles_y:
                    self.track.tiles[coords[i][0]][coords[i][1]] = TILE_ID_ENEMY
