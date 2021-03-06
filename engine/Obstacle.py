import random
from .const import *


class Obstacle(object):
    def __init__(self, track):
        """
        Make enemy to kill player
        :param track: place to put enemy
        """
        self.track = track
        self.wait = OBSTACLE_WAIT_FOR_NEXT

    def attach(self):
        """
        Put enemy at any coords
        :return:
        """
        for pos in OBSTACLE_POSITIONS[random.randint(0, len(OBSTACLE_POSITIONS) - 1)]:
            obstacle_type = random.randint(OBSTACLE_RANDOM_LIMITS[0], OBSTACLE_RANDOM_LIMITS[1])
            if BONUS_LIFE_LIMITS[0] < obstacle_type < BONUS_LIFE_LIMITS[1]:
                obstacle_coords = BONUS_LIFE_COORDS
                obstacle_tile = TILE_ID_BONUS_LIFE
            elif BONUS_SPEED_LIMITS[0] < obstacle_type < BONUS_SPEED_LIMITS[1]:
                obstacle_coords = BONUS_SPEED_COORDS
                obstacle_tile = TILE_ID_BONUS_SPEED
            elif BONUS_INVULNERABILITY_LIMITS[0] < obstacle_type < BONUS_INVULNERABILITY_LIMITS[1]:
                obstacle_coords = BONUS_INVULNERABILITY_COORDS
                obstacle_tile = TILE_ID_BONUS_INVULNERABILITY
            else:
                obstacle_coords = ENEMY_COORDS
                obstacle_tile = TILE_ID_ENEMY

            coords = [[coord[0] + CAR_WIDTH*pos, coord[1]] for coord in obstacle_coords]

            for coord in coords:
                if 0 <= coord[0] < self.track.tiles_x and 0 <= coord[1] < self.track.tiles_y:
                    self.track.tiles[coord[0]][coord[1]] = obstacle_tile
