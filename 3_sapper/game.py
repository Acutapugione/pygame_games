import time
import pygame as pg

from config import *
from board import Board


class Game:
    
    def __init__(self) -> None:
        self.board = Board()
        self.FONT = pg.font.SysFont(FONT_FAMILY, FONT_SIZE)
        self.is_gameover = False
        self.is_won = False

    def show_board(self, surface):
        for row in range(SQ_AMOUNT):
            for col in range(SQ_AMOUNT):
                rect = (col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE)
                
                square = self.board.squares[row][col]

                if self.is_gameover and square.is_bomb:
                    square.is_visible = True

                if square.is_visible and square.is_bomb:
                    pg.draw.rect(surface, MINE_COLOR, rect)
                elif square.is_visible:
                    pg.draw.rect(surface, SQUARE_COLOR, rect)

                color = SQUARE_COLOR_VISIBLE if square.is_visible else SQUARE_COLOR
                pg.draw.rect(surface, color, rect, width=1)

                if square.count and square.is_visible:
                    text_surface = self.FONT.render(str(square.count), False, (0, 0, 0))
                    text_rect = (
                        ( col * SQ_SIZE + ( SQ_SIZE // 2 ) - ( text_surface.get_width() // 2 ) ), # x = center - half of text width
                        ( row * SQ_SIZE + ( SQ_SIZE // 2 ) - ( text_surface.get_height() // 2 ) ) # y = center - half of text height
                    )
                    surface.blit(text_surface, text_rect)

    def check_win(self):
        for row in self.board.squares:
            for square in row:
                if square.is_bomb:
                    continue
                
                if not square.is_visible:
                    return False
                    
        return True

    def restart_game(self):
        self.__init__()
