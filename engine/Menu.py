class Menu:
    def __init__(self, position=(0, 0)):
        self.index = 0
        self.x = position[0]
        self.y = position[1]
        self.menu = list()

    def down(self):
        self.index += 1
        if self.index >= len(self.menu):
            self.index = 0

    def up(self):
        self.index -= 1
        if self.index < 0:
            self.index = len(self.menu) - 1

    def add_menu_item(self, no_select, select, func):
        self.menu.append({'no select': no_select,
                          'select': select,
                          'func': func})

    def call(self):
        self.menu[self.index]['func']()

    def draw(self, display):
        index = 0
        x = self.x
        y = self.y
        for item in self.menu:
            if self.index == index:
                display.blit(item['select'], (x, y))
                y += item['select'].get_rect().h
            else:
                display.blit(item['no select'], (x, y))
                y += item['no select'].get_rect().h
            index += 1
