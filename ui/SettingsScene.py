from engine.const import *
from engine.Settings import Settings
from .Scene import Scene
from .CheckBox import CheckBox
from .Label import Label


class SettingsScene(Scene):
    def _start(self):
        """
        Init and start new Scene
        :return: None
        """
        self.settings = Settings()
        self.settings.load()

        self.header_label = Label(self.display, 150, 30, "Настройки", 72)
        self.full_screen_label = Label(self.display, 50, 100, "Полный экран", 48)
        self.full_screen_checkbox = CheckBox(self.display, 500, 100, 32)
        self.full_screen_checkbox.checked = self.settings['full_screen']

    def _draw(self, dt):
        """
        Redraw game by current status
        :param dt: time interval pass from previous call
        :return: None
        """
        self.display.fill(BACKGROUND_COLOR)
        self.header_label.render()
        self.full_screen_label.render()
        self.full_screen_checkbox.render()

    def _event(self, event):
        """
        Make event handle
        :param event: any occurred event
        :return: None
        """
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    self.settings['full_screen'] = self.full_screen_checkbox.is_checked()
                    if self.settings['full_screen']:
                        width = self.settings['full_screen_width']
                        height = self.settings['full_screen_height']
                        pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                    else:
                        pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT))
                    self.settings.save()
                    self.set_next_scene("menu")
                    self.the_end()
            self.full_screen_checkbox.update(e)
