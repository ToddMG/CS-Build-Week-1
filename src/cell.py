class Cell:
    def __init__(self, alive=False):
        # self._x = x
        # self._y = y
        self._alive = alive
        self._next = None

    def is_alive(self):
        if self._alive:
            return True
        return False

    def set_alive(self):
        self._alive = True

    def set_dead(self):
        self._alive = False

    # def neighbors(self):
    #     yield self._x-1, self._y+1
    #     yield self._x, self._y+1
    #     yield self._x+1, self._y+1
    #     yield self._x-1, self._y
    #     yield self._x+1, self._y
    #     yield self._x-1, self._y-1
    #     yield self._x, self._y-1
    #     yield self._x+1, self._y-1