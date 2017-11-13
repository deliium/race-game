def check_move(fn):
    """
    use for check Player move
    :param fn: move function
    :return: decorated move function
    """
    def wrapped(self):
        """
        detach and attach player when make player move
        :param self: player class
        :return: None
        """
        if self.direction is not None:
            self.detach()
            fn(self)
            self.attach()
    return wrapped
