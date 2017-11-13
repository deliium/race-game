class Menu:
    def __init__(self, position=(0, 0)):
        """
        Make all menu mechanics
        :param position: start position for drawing
        """
        self.index = 0
        self.x = position[0]
        self.y = position[1]
        self.menu = list()

    def down(self):
        """
        Move menu pointer down
        :return: None
        """
        self.index += 1
        if self.index >= len(self.menu):
            self.index = 0

    def up(self):
        """
        Move menu pointer up
        :return: None
        """
        self.index -= 1
        if self.index < 0:
            self.index = len(self.menu) - 1

    def add_menu_item(self, no_select, select, func):
        """
        Insert new menu item
        :param no_select: function invoked when a menu item isn't selected
        :param select: function invoked when menu item is selected
        :param func: function invoked when menu item is clicked
        :return: None
        """
        self.menu.append({'no select': no_select,
                          'select': select,
                          'func': func})

    def call(self):
        """
        Invoke function from menu item
        :return: None
        """
        self.menu[self.index]['func']()

    def draw(self, display):
        """
        Draw menu on display
        :param display: place to put menu items
        :return: None
        """
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
