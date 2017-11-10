#!/usr/bin/env python3

from ui.MenuScene import MenuScene
from ui.LogoScene import ShowLogoScene, HideLogoScene
from ui.WaitScene import WaitScene
from engine.Game import Game
from engine.const import *

if __name__ == '__main__':
    scene = ShowLogoScene(WaitScene(500, HideLogoScene(WaitScene(400, MenuScene()))))
    game = Game(800, 600, scene)
    game.set_caption(GAME_TITLE, "icon.png")

    print(GAME_TITLE)
    print(GAME_ABOUT)
    print(GAME_HOTKEYS)
    
    game.main_loop()
