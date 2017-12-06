#!/usr/bin/env python3

from engine.Game import Game
from engine.const import *

if __name__ == '__main__':
    game = Game(800, 600)
    game.set_caption(GAME_TITLE, "icon.png")

    print(GAME_TITLE)
    print(GAME_ABOUT)
    print(GAME_HOTKEYS)
    
    game.main_loop()