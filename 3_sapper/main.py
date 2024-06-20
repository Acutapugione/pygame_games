import time
import pygame as pg
import sys 

from config import *
from game import Game

class Main:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Sapper Game')

        self.game = Game()

    def main(self):
        screen = self.screen
        game = self.game

        while True:
            screen.fill(BG_COLOR, ((0, 0), (WIDTH, HEIGHT)))

            game.show_board(screen)
            game.board.place_flag(screen)
            
            if game.is_gameover:
                if not game.board.timer:
                    game.board.timer = time.time()
                    
                game.board.draw_bombs(screen)
                game.board.gameover_text(screen)
            elif game.is_won:
                game.board.win_text(screen)

            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    pg.quit()
                    sys.exit()

                elif (event.type == pg.KEYDOWN):
                    if (event.key == pg.K_ESCAPE):
                        pg.quit()
                        sys.exit()
                    
                    elif (event.key == pg.K_r):
                        game.restart_game()
                
                elif (event.type == pg.MOUSEBUTTONUP):
                    if game.is_gameover or game.is_won:
                        continue

                    x,y = event.pos
                    col = x // SQ_SIZE
                    row = y // SQ_SIZE
                    
                    square = game.board.squares[row][col]

                    if event.button == 1:
                        if square.with_flag:
                            continue
                        if square.is_bomb:
                            game.is_gameover = True
                            break
                        if not square.count and not square.is_visible:
                            game.board.open_few(row, col)

                        square.is_visible = True

                        if game.check_win():
                            game.is_won = True
                    
                    elif event.button == 3:
                        if not square.is_visible:
                            square.with_flag = not square.with_flag

            pg.display.update()

if __name__ == "__main__":
    m = Main()
    m.main()