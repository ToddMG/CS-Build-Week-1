import sys, pygame, os
from board import Board


clock = pygame.time.Clock()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
WHITE = 255, 255, 255
BLACK = 0, 0, 0

START_IMG = pygame.image.load(os.path.join(os.path.dirname(__file__), '../img/button_start.jpg' ))
STOP_IMG = pygame.image.load(os.path.join(os.path.dirname(__file__), '../img/button_stop.jpg' ))
CLEAR_IMG = pygame.image.load(os.path.join(os.path.dirname(__file__), '../img/button_clear.jpg' ))
START_XY = (168,736)
STOP_XY = (368,736)
CLEAR_XY = (568,736)
BUTTON_WH = (100,50)

OSCILATOR = {(1,1),(1,2),(1,3)}

GLIDER = {(1,0),(2,1),(0,2),(1,2),(2,2)}

PULSAR = {(8,5),(9,5),(10,5),(14,5),(15,5),(16,5),
          (6,7),(11,7),(13,7),(18,7),
          (6,8),(11,8),(13,8),(18,8),
          (6,9),(11,9),(13,9),(18,9),
          (8,10),(9,10),(10,10),(14,10),(15,10),(16,10),
          (8,12),(9,12),(10,12),(14,12),(15,12),(16,12),
          (6, 13), (11, 13), (13, 13), (18, 13),
          (6, 14), (11, 14), (13, 14), (18, 14),
          (6, 15), (11, 15), (13, 15), (18, 15),
          (8,17),(9,17),(10,17),(14,17),(15,17),(16,17)}

HALF = {(8,5),(9,5),(10,5),(14,5),(15,5),(16,5),
          (6,7),(11,7),(13,7),(18,7),
          (6,8),(11,8),(13,8),(18,8),
          (6,9),(11,9),(13,9),(18,9)}

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
        self.game_board = Board()
        self.configure_grid()
        self.paused = False
        self.time = 0
        pygame.display.flip()


    def get_board_cells(self):
        return self.game_board.get_live_cells()


    def clear_screen(self):
        self.game_board.configure_board(None)
        self.draw_grid()


    def configure_grid(self, config=OSCILATOR):
        self.game_board.configure_board(config)


    def advance_board(self):
        self.game_board.advance()


    def draw_lines(self):
        for line in LINE_POINTS:
            pygame.draw.lines(self.screen, BLACK, True, line)


    def draw_buttons(self):
        self.screen.blit(START_IMG, ((WINDOW_WIDTH * 0.21), (WINDOW_HEIGHT * 0.92))) #168 & 736
        self.screen.blit(STOP_IMG, ((WINDOW_WIDTH * 0.46), (WINDOW_HEIGHT * 0.92))) #368 & 736
        self.screen.blit(CLEAR_IMG, ((WINDOW_WIDTH * 0.71), (WINDOW_HEIGHT * 0.92))) #568 & 736


    def button_watch(self):
        mouse_pos = pygame.mouse.get_pos()

        if START_XY[0]+BUTTON_WH[0] > mouse_pos[0] > START_XY[0] and START_XY[1]+BUTTON_WH[1] > mouse_pos[1] > START_XY[1]:
            self.resume_game()

        elif STOP_XY[0] + BUTTON_WH[0] > mouse_pos[0] > STOP_XY[0] and STOP_XY[1] + BUTTON_WH[1] > mouse_pos[1] > STOP_XY[1]:
            self.pause_game()

        elif CLEAR_XY[0] + BUTTON_WH[0] > mouse_pos[0] > CLEAR_XY[0] and CLEAR_XY[1] + BUTTON_WH[1] > mouse_pos[1] > CLEAR_XY[1]:
            if self.paused:
                self.clear_screen()

        else:
            cell_x = mouse_pos[0] // 32
            cell_y = mouse_pos[1] // 32
            self.configure_grid({(cell_x,cell_y)})


    def draw_grid(self):
        block_size = 32

        self.screen.fill(WHITE)
        self.draw_lines()

        for (x,y) in self.get_board_cells():
            live_cell = pygame.Rect(x*block_size, y*block_size,
                               block_size, block_size)
            pygame.draw.rect(self.screen, BLACK, live_cell, 0)

        pygame.display.update()


    def pause_game(self):
        self.paused = True

    def resume_game(self):
        self.paused = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.button_watch()


    def run(self):
        while True:
            while not self.paused: # Not Paused
                self.handle_events()
                if pygame.time.get_ticks() - self.time > 350:
                    # been 2 seconds
                      # reset the timer
                    self.time = pygame.time.get_ticks()
                    self.advance_board()
                    self.draw_grid()
                    self.draw_buttons()

                pygame.display.flip()
                clock.tick(60)

            while self.paused: # Paused
                self.handle_events()
                self.draw_grid()
                self.draw_buttons()
                pygame.display.flip()
                clock.tick(5)





if __name__ == '__main__':

    game = GameOfLife()
    game.run()