import pygame


class CheckBox(object):
    def __init__(self, display, x, y, size, color=(230, 230, 230), check_color=(0, 0, 0), outline_color=(0, 0, 0)):
        self.display = display

        self.x = x
        self.y = y
        self.size = size
        self.check_size = int(size/3)
        self.outline_size = 1
        self.item = pygame.Rect(self.x, self.y, self.size, self.size)
        self.outline = self.item.copy()

        self.color = color
        self.check_color = check_color
        self.outline_color = outline_color

        self.checked = False

    def _set_checked(self, event):
        x, y = event.pos
        left, right, top, bottom = self.x, self.x + self.size, self.y, self.y + self.size
        if left <= x <= right and top <= y <= bottom:
            self.checked = not self.checked

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self._set_checked(event)

    def is_checked(self):
        return self.checked

    def render(self):
        pygame.draw.rect(self.display, self.color, self.item)
        pygame.draw.rect(self.display, self.outline_color, self.outline, self.outline_size)
        if self.checked:
            circle_position = self.x + int(self.size/2), self.y + int(self.size/2)
            pygame.draw.circle(self.display, self.check_color, circle_position, self.check_size)
