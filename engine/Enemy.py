from .const import *


class Enemy(object):
    def __init__(self, track):
        """
        Make enemy to kill player
        :param track: place to put enemy
        """
        self.track = track
        self.wait = ENEMY_WAIT_FOR_NEXT

    def attach(self, enemy_poses):
        """
        Put player at any coords
        :param enemy_poses: enemy position
        :return:
        """
        for enemy_pos in enemy_poses:
            coords = [[coord[0] + CAR_WIDTH*enemy_pos, coord[1]] for coord in ENEMY_COORS]

            for coord in coords:
                if 0 <= coord[0] < self.track.tiles_x and 0 <= coord[1] < self.track.tiles_y:
                    self.track.tiles[coord[0]][coord[1]] = TILE_ID_ENEMY
