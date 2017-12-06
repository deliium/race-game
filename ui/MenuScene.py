from engine.Menu import Menu
from engine.const import *
from .Scene import Scene


class MenuScene(Scene):
    def start_game(self):
        """
        Handle start game button in menu
        :return: None
        """
        self.set_next_scene("game")
        self.the_end()

    def show_options(self):
        """
        Handle show option button in menu
        :return: None
        """
        print("show-options")

    def show_score(self):
        """
        Handle show score button in menu
        :return: None
        """
        print("show-score")

    def stop_game(self):
        """
        Handle stop game button in menu
        :return: None
        """
        self.set_next_scene(None)
        self.the_end()

    def _start(self):
        """
        Init and start new Menu scene
        :return: None
        """
        self.menu = Menu((330, 300))
        self.menuItems = (("Начать игру", self.start_game),
                          ("Настройки", self.show_options),
                          ("Счёт", self.show_score),
                          ("Выйти", self.stop_game))

        font = pygame.font.SysFont("Monospace", 40, bold=False, italic=False)
        font_bold = pygame.font.SysFont("Monospace", 40, bold=True, italic=False)
        for item in self.menuItems:
            self.menu.add_menu_item(font.render(item[0], True, (0, 0, 0)),
                                    font_bold.render(item[0], True, (0, 0, 0)),
                                    item[1])

    def _event(self, event):
        """
        Make event handle
        :param event: any occurred event
        :return: None
        """
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.menu.down()
                elif e.key == pygame.K_UP:
                    self.menu.up()
                elif e.key == pygame.K_RETURN:
                    self.menu.call()

    def _draw(self, dt):
        """
        Redraw menu by current status
        :param dt: time interval pass from previous call
        :return: None
        """
        self.display.fill(BACKGROUND_COLOR)
        self.menu.draw(self.display)


class PauseScene(MenuScene):
    def continue_game(self):
        """
        Handle start game button in menu
        :return: None
        """
        self.set_next_scene("game")
        self.the_end()

    def _start(self):
        """
        Init and start new Menu scene
        :return: None
        """
        self.menu = Menu((330, 300))
        self.menuItems = (("Продолжить игру", self.continue_game),
                          ("Настройки", super().show_options),
                          ("Счёт", super().show_score),
                          ("Выйти", super().stop_game))

        font = pygame.font.SysFont("Monospace", 40, bold=False, italic=False)
        font_bold = pygame.font.SysFont("Monospace", 40, bold=True, italic=False)
        for item in self.menuItems:
            self.menu.add_menu_item(font.render(item[0], True, (0, 0, 0)),
                                    font_bold.render(item[0], True, (0, 0, 0)),
                                    item[1])
