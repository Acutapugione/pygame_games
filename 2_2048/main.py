import pygame
import sys

from config import *
from game import Game
from board import Board

class Main:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('2048 game')

        self.game = Game()

    def mainloop(self):
        screen = self.screen
        game = self.game
        board = self.game.board
        

        while True:
            screen.fill(BG_COLOR, ((0, 0), (WIDTH, HEIGHT)))
            game.show_board(screen)
            game.show_numbers(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        board.move((0, -1))
                    elif event.key == pygame.K_a:
                        board.move((-1, 0))
                    elif event.key == pygame.K_s:
                        board.move((0, 1))
                    elif event.key == pygame.K_d:
                        board.move((1, 0))
                    
                    
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    

            pygame.display.update()

if __name__ == '__main__':
    m = Main()
    m.mainloop()