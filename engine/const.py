from pygame.locals import USEREVENT
import pygame

TILE_WIDTH = 24
TILE_HEIGHT = 24

TILE_X_COUNT = 11
TILE_Y_COUNT = 20

TILE_ID_PLAYER = 1
TILE_ID_WALL = 1
TILE_ID_GROUND = 0

END_SCENE = USEREVENT + 1

BACKGROUND_COLOR = pygame.Color("#849173")

PLAYER_COORDS = [[5, 16], [4, 17], [5, 17], [6, 17], [5, 18], [4, 19], [6, 19]]

GAME_TITLE = "Race game"
GAME_ABOUT = """ About game >>= simple race game from tetris """
GAME_HOTKEYS = """
== Keyboards ==
ESC = exit
Arrow left = move left
Arrow right = move right
"""

