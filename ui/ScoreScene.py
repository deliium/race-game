import shelve

from engine.const import *

from .Label import Label
from .Scene import Scene


class ScoreScene(Scene):
    def _start(self):
        """
        Init and start new Scene
        :return: None
        """
        self.header_label = Label(self.display, 150, 30, "Статистика", 72)
        self.score_label = Label(self.display, 50, 100, "Прошлая игра: ", 72)
        self.score = 0
        self._load()

    def _draw(self, dt):
        """
        Redraw game by current status
        :param dt: time interval pass from previous call
        :return: None
        """
        self.display.fill(BACKGROUND_COLOR)
        self.header_label.render()
        self.score_label.render()

    def _event(self, event):
        """
        Make event handle
        :param event: any occurred event
        :return: None
        """
        for e in event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    self.set_next_scene("menu")
                    self.the_end()

    @staticmethod
    def save(score):
        d = shelve.open(SCORE_FILE)
        d['score'] = score
        d.close()

    def _load(self):
        d = shelve.open(SCORE_FILE)
        try:
            self.score = d['score']
        except KeyError:
            d['score'] = self.score
        d.close()
        self.score_label.text += str(self.score)
