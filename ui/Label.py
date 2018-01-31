import pygame


class Label(object):
    def __init__(self, display, x, y, text="", size=22, color=(0, 0, 0)):
        self.display = display
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.color = color
        self.font = pygame.font.Font(None, self.size)

    def render(self):
        text_surface = self.font.render(self.text, True, self.color)
        #w, h = self.font.size(self.text)
        #font_position = self.x + int(w/2), self.y - int(h/2)
        self.display.blit(text_surface, (self.x, self.y))
