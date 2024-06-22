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

    def gameover_text(self, surface):
        ctime = time.time()

        text_surface = self.font.render("Game over!", False, (255, 255, 255), "red")

        if ctime - self.board.timer > 2:
            text_surface = self.font.render(
                'Press "R" to play again', False, (255, 255, 255), "red"
            )

        surface.blit(
            text_surface,
            (
                (Config.WIDTH // 2) - (text_surface.get_width() // 2),
                (Config.HEIGHT // 2) - (text_surface.get_height() // 2),
            ),
        )

    def win_text(self, surface):
        text_surface = self.font.render("You won!", False, (255, 255, 255), "green")
        surface.blit(
            text_surface,
            (
                (Config.WIDTH // 2) - (text_surface.get_width() // 2),
                (Config.HEIGHT // 2) - (text_surface.get_height() // 2),
            ),
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
