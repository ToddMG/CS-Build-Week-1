import sys, pygame

BOARD_SIZE = WIDTH, HEIGHT = 320, 240
DEAD_COLOR = 255, 255, 255
ALIVE_COLOR = 0, 0, 0

class GameOfLife:

    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode(BOARD_SIZE)

    def run(self):

        pygame.draw.rect()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.screen.fill(DEAD_COLOR)

            #screen.blit(ball, ballrect)
            pygame.display.flip()

if __name__ == '__main__':

    game = GameOfLife()
    game.run()