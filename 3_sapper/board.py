import random
import time
import pygame as pg
from pygame.font import Font, SysFont
from config import *
from square import Square


class Board:

    def __init__(
        self,
        squares_amount: int = SQ_AMOUNT,
        font: Font = SysFont(FONT_FAMILY, size=70),
        bombs_amount: int = BOMBS_AMOUNT,
    ) -> None:
        self.squares = tuple(
            tuple(0 for row in range(squares_amount)) for col in range(squares_amount)
        )
        print(f"{self.squares=}")
        # self.squares = ((0) * squares_amount for x in range(squares_amount))
        self.bombs = set()
        self.font = pg.font.SysFont(FONT_FAMILY, size=70)
        self.timer = 0

        self.generate_bombs()
        self.create_board()

    def create_board(self):
        for row in range(SQ_AMOUNT):
            for col in range(SQ_AMOUNT):
                if not (row, col) in self.bombs:
                    count = self.count_bombs_around(row, col)
                    self.squares[row][col] = Square(row=row, col=col, count=count)

    def generate_bombs(self):
        while len(self.bombs) != BOMBS_AMOUNT:
            bomb_row, bomb_col = random.randint(0, SQ_AMOUNT - 1), random.randint(
                0, SQ_AMOUNT - 1
            )
            self.bombs.add((bomb_row, bomb_col))
            self.squares[bomb_row][bomb_col] = Square(
                row=bomb_row, col=bomb_col, count=0, is_bomb=True
            )

    def count_bombs_around(self, row: int, col: int):
        count = 0
        for c_row in range(
            row if row - 1 < 0 else row - 1, row + 1 if row + 2 > SQ_AMOUNT else row + 2
        ):
            for c_col in range(
                col if col - 1 < 0 else col - 1,
                col + 1 if col + 2 > SQ_AMOUNT else col + 2,
            ):
                if (
                    self.squares[c_row][c_col].__class__ is Square
                    and self.squares[c_row][c_col].is_bomb
                ):
                    count += 1

        return count

    def place_flag(self, surface):
        for row in self.squares:
            for square in row:
                if square.with_flag:
                    rect = (
                        square.col * SQ_SIZE,
                        square.row * SQ_SIZE,
                        SQ_SIZE,
                        SQ_SIZE,
                    )
                    pg.draw.rect(surface, FLAG_COLOR, rect)

    def open_few(self, row: int, col: int):
        for c_row in range(
            row if row - 1 < 0 else row - 1, row + 1 if row + 2 > SQ_AMOUNT else row + 2
        ):
            for c_col in range(
                col if col - 1 < 0 else col - 1,
                col + 1 if col + 2 > SQ_AMOUNT else col + 2,
            ):
                square = self.squares[c_row][c_col]

                if square.is_visible:
                    continue

                square.is_visible = True

                if not square.count:
                    self.open_few(c_row, c_col)

    def draw_bombs(self, surface):
        for row, col in self.bombs:
            rect = (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            pg.draw.rect(surface, BOMB_COLOR, rect)

    def gameover_text(self, surface):
        ctime = time.time()

        text_surface = self.font.render("Game over!", False, (255, 255, 255), "red")

        if ctime - self.timer > 2:
            text_surface = self.font.render(
                'Press "R" to play again', False, (255, 255, 255), "red"
            )

        surface.blit(
            text_surface,
            (
                (WIDTH // 2) - (text_surface.get_width() // 2),
                (HEIGHT // 2) - (text_surface.get_height() // 2),
            ),
        )

    def win_text(self, surface):
        text_surface = self.font.render("You won!", False, (255, 255, 255), "green")
        surface.blit(
            text_surface,
            (
                (WIDTH // 2) - (text_surface.get_width() // 2),
                (HEIGHT // 2) - (text_surface.get_height() // 2),
            ),
        )
