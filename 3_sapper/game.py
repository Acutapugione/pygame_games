import time
import pygame as pg

from config import *
from board import Board
from pygame.font import Font


class Game:

    def __init__(
        self,
        board: Board,
        font: Font,
    ) -> None:
        self.board = board
        self.font = font
        self.is_gameover = False
        self.is_won = False

    def show_board(self, surface):
        self.board.show(
            surface,
            square_size=Config.SQ_SIZE,
            square_color=Config.SQUARE_COLOR,
            square_visible_color=Config.SQUARE_COLOR_VISIBLE,
        )

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
