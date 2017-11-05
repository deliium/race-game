from engine.Menu import Menu
from engine.const import *
from .Scene import Scene
from .GameScene import GameScene


class MenuScene(Scene):
    def start_game(self):
        self.scene.set_next_scene(self)
        self.set_next_scene(self.scene)
        self.the_end()

    def show_options(self):
        print("show-options")

    def show_score(self):
        print("show-score")

    def stop_game(self):
        self.set_next_scene(None)
        self.the_end()

    def _start(self):
        self.scene = GameScene()
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
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.menu.down()
                elif e.key == pygame.K_UP:
                    self.menu.up()
                elif e.key == pygame.K_RETURN:
                    self.menu.call()

    def _draw(self, dt):
        self.display.fill(BACKGROUND_COLOR)
        self.menu.draw(self.display)
