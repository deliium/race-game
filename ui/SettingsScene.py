import shelve
from engine.const import *
from .Scene import Scene
from .CheckBox import CheckBox
from .Label import Label


class SettingsScene(Scene):
    def _start(self):
        """
        Init and start new Scene
        :return: None
        """
        self.header_label = Label(self.display, 150, 30, "Настройки", 72)
        self.full_screen_label = Label(self.display, 50, 100, "Полный экран", 48)
        self.full_screen_checkbox = CheckBox(self.display, 500, 100, 32)
        self._load()

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
                    self._save()
                    self.set_next_scene("menu")
                    self.the_end()
            self.full_screen_checkbox.update(e)

    def _save(self):
        d = shelve.open('settings.txt')
        d['full_screen'] = self.full_screen_checkbox.is_checked()
        d.close()

    def _load(self):
        d = shelve.open("settings.txt")
        try:
            self.full_screen_checkbox.checked = d['full_screen']
        except KeyError:
            d['full_screen'] = self.full_screen_checkbox.is_checked()
        d.close()
