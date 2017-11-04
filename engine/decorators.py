def check_move(fn):
    def wrapped(self):
        if self.direction is not None:
            self.remove_from_field()
            fn(self)
            self.put_to_field()
    return wrapped
