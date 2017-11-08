from pygame.locals import USEREVENT
import pygame

TILE_WIDTH = 24
TILE_HEIGHT = 24

TILE_X_COUNT = 11
TILE_Y_COUNT = 20

TILE_ID_PLAYER = 1
TILE_ID_ENEMY = 1
TILE_ID_WALL = 1
TILE_ID_GROUND = 0

TRACK_MOVE_SLEEP_TIME = .3
PLAYER_MOVE_SLEEP_TIME = .1

BORDER_HEIGHT = 2

END_SCENE = USEREVENT + 1

BACKGROUND_COLOR = pygame.Color("#849173")

PLAYER_COORDS = [[5, 16], [4, 17], [5, 17], [6, 17], [5, 18], [4, 19], [6, 19]]
ENEMY_COORS = [[2, 0], [1, 1], [2, 1], [3, 1], [2, 2], [1, 3], [3, 3]]
CAR_WIDTH = 3

PLAYER_LIVES_COUNT = 5

GAME_TITLE = "Race game"
GAME_ABOUT = """ About game >>= simple race game from tetris """
GAME_HOTKEYS = """
== Keyboards ==
ESC = exit
Arrow left = move left
Arrow right = move right
"""

