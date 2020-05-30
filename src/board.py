import sys

class Board:
    def __init__(self, rows=20, cols=20):
        self._rows = rows
        self._cols = cols
        self._cells = set()
        self._buffer_cells = set()

    def get_live_cells(self):
        return self._cells

    def cell_spawn(self, x, y):
        self._buffer_cells.add((x,y))

    def cell_kill(self, x, y):
        self._buffer_cells.remove((x,y))

    def kill_buffer(self):
        self._buffer_cells = set()

    def cell_is_alive(self, x, y):
        return (x,y) in self._cells

    def generate_buffer(self):
        self.kill_buffer()
        for y in range(self._rows):
            for x in range(self._cols):
                if self.cell_is_alive(x,y):
                    if 1 < self.get_alive_neighbors(x,y) < 4:
                        self.cell_spawn(x, y)
                    else:
                        pass

                else:
                    if self.get_alive_neighbors(x,y) == 3:
                        self.cell_spawn(x, y)


    def advance(self):
        self._cells = self._buffer_cells
        self.generate_buffer()
        self.draw_board()

    def get_alive_neighbors(self, x, y):
        return sum([1 for cell in self.generate_neighbors(x, y) if cell in self._cells])

    def generate_neighbors(self, x, y):
        yield x - 1, y + 1
        yield x, y + 1
        yield x + 1, y + 1
        yield x - 1, y
        yield x + 1, y
        yield x - 1, y - 1
        yield x, y - 1
        yield x + 1, y - 1

    def draw_board(self):
        print('\n'*3)
        for y in range(self._rows):
            print('')
            for x in range(self._cols):
                if (x,y) in self.get_live_cells():
                    sys.stdout.write(' X ')
                else:
                    sys.stdout.write(' - ')



    def configure_board(self, preset_cells):
        for x,y in preset_cells:
            self.cell_spawn(x,y)

if __name__ == '__main__':
    test_board = Board()
    test_cells = {(0,2),(2,1),(2,2),(2,3),(1,3)}
    test_board.configure_board(test_cells)
    i = 0
    while i < 100:
        test_board.advance()
        i += 1
