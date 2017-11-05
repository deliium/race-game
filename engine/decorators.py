def check_move(fn):
    def wrapped(self):
        if self.direction is not None:
            self.detach()
            fn(self)
            self.attach()
    return wrapped
