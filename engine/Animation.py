class Animation(object):
    def __init__(self, sprite, frame_width, frame_height, frame_speed):
        """
        Makes transparent animation
        :param time: delay while animation works
        :param show: is animation will be shows
        """
        self.sprite = sprite
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame_speed = frame_speed
        self.frame_end = int(self.sprite.get_size()[0] / frame_width)
        self.counter = 0
        self.frame_current = 0
        self.run = False

    def update(self, dt):
        """
        Update animation by time
        :param dt: time interval pass from previous call
        :return: None
        """
        if self.run:
            if self.counter == self.frame_speed - 1:
                self.frame_current = (self.frame_current + 1) % self.frame_end
            self.counter = (self.counter + 1) % self.frame_speed

    def start(self):
        """
        Start animation from beginning
        :return: None
        """
        self.counter = 0
        self.frame_current = 0
        self.run = True

    def is_start(self):
        """
        Tell, is animation starting
        :return: Boolean
        """
        return self.run

    def stop(self):
        """
        Stop animation works
        :return: None
        """
        self.run = False

    def get_coords(self):
        """
        Check is animation ending and return coords of the next sprite part
        :return: coords to draw sprite part
        """
        if self.frame_current == self.frame_end - 1:
            self.stop()
        return 0 + self.frame_width*self.frame_current, 0, self.frame_width, self.frame_height
