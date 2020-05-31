import sys, pygame
from board import Board

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
WHITE = 255, 255, 255
BLACK = 0, 0, 0
OSCILATOR = {(1,1),(1,2),(1,3)}
GLIDER = {(1,0),(2,1),(0,2),(1,2),(2,2)}
LINE_POINTS = [[(0, 0), (0, 800)], [(32, 0), (32, 800)], [(64, 0), (64, 800)], [(96, 0), (96, 800)],
               [(128, 0), (128, 800)], [(160, 0), (160, 800)], [(192, 0), (192, 800)], [(224, 0), (224, 800)],
               [(256, 0), (256, 800)], [(288, 0), (288, 800)], [(320, 0), (320, 800)], [(352, 0), (352, 800)],
               [(384, 0), (384, 800)], [(416, 0), (416, 800)], [(448, 0), (448, 800)], [(480, 0), (480, 800)],
               [(512, 0), (512, 800)], [(544, 0), (544, 800)], [(576, 0), (576, 800)], [(608, 0), (608, 800)],
               [(640, 0), (640, 800)], [(672, 0), (672, 800)], [(704, 0), (704, 800)], [(736, 0), (736, 800)],
               [(768, 0), (768, 800)], [(0, 0), (800, 0)], [(0, 32), (800, 32)], [(0, 64), (800, 64)],
               [(0, 96), (800, 96)], [(0, 128), (800, 128)], [(0, 160), (800, 160)], [(0, 192), (800, 192)],
               [(0, 224), (800, 224)], [(0, 256), (800, 256)], [(0, 288), (800, 288)], [(0, 320), (800, 320)],
               [(0, 352), (800, 352)], [(0, 384), (800, 384)], [(0, 416), (800, 416)], [(0, 448), (800, 448)],
               [(0, 480), (800, 480)], [(0, 512), (800, 512)], [(0, 544), (800, 544)], [(0, 576), (800, 576)],
               [(0, 608), (800, 608)], [(0, 640), (800, 640)], [(0, 672), (800, 672)], [(0, 704), (800, 704)],
               [(0, 736), (800, 736)], [(0, 768), (800, 768)]]

class GameOfLife:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clear_screen()
        self.game_board = Board()
        self.configure_grid()
        self.paused = False
        pygame.display.flip()


    def get_board_cells(self):
        return self.game_board.get_live_cells()

    def clear_screen(self):
        self.screen.fill(WHITE)


    def init_grids(self):
        pass


    def configure_grid(self):
        self.game_board.configure_board(GLIDER)


    def advance_board(self):
        self.game_board.advance()


    def draw_lines(self):
        for line in LINE_POINTS:
            pygame.draw.lines(self.screen, BLACK, True, line)


    def draw_grid(self):
        block_size = 32

        self.screen.fill(WHITE)
        self.draw_lines()

        self.advance_board()
        #   print(self.get_board_cells())

        for (x,y) in self.get_board_cells():
            live_cell = pygame.Rect(x*block_size, y*block_size,
                               block_size, block_size)
            pygame.draw.rect(self.screen, BLACK, live_cell, 0)

        pygame.display.flip()
        # pygame.display.flip()

    def pause_game(self):
        self.paused = True


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('click!')
            # if event is click on pause, then toggle game pause
            # if event is click on start, then toggle game start
            # if event is click on randomize, then randomize board
            # if event is click on grid, then
        pass

    def run(self):
        while True:

                self.handle_events()
                self.draw_grid()
                #pygame.time.wait(300)


if __name__ == '__main__':

    game = GameOfLife()
    game.run()