from pprint import pprint
import random
import time
import pygame as pg
from pygame.font import Font, SysFont
from config import Config

# (
#     WIDTH,
#     HEIGHT,
#     SQ_AMOUNT,
#     BOMBS_AMOUNT,
#     FONT_FAMILY,
#     SQ_SIZE,
#     BOMB_COLOR,
#     FLAG_COLOR,
# )
from square import Square
from bomb import BombGenerator


class Board:
    def __init__(
        self,
        font: Font,
        squares_amount: int = Config.SQ_AMOUNT,
        bombs_amount: int = Config.BOMBS_AMOUNT,
    ) -> None:
        self.squares_amount = squares_amount
        self.font = font
        # self.bombs = set()
        self.timer = 0.0
        self.bombs_amount = bombs_amount
        self.bomb_generator = BombGenerator(
            (self.squares_amount, self.squares_amount),
            self.bombs_amount,
        )
        self.bombs = self.bomb_generator.generate()
        pprint(self.bombs)
        self.__squares = self.__generate_squares()
        pprint(self.__squares)

    def show(
        self,
        surface,
        square_size=Config.SQ_SIZE,
        square_color=Config.SQUARE_COLOR,
        square_visible_color=Config.SQUARE_COLOR_VISIBLE,
    ):
        for row, col in zip(range(self.squares_amount), range(self.squares_amount)):
            rect = (col * square_size, row * square_size, square_size, square_size)
            square = self.__squares[row][col]
            color = square_visible_color if square.is_visible else square_color
            pg.draw.rect(surface, color, rect, width=1)
            if square.count and square.is_visible:
                text_surface = self.font.render(str(square.count), False, (0, 0, 0))
                center_multiplier = (  # half of text width
                    square_size + (square_size // 2) - (text_surface.get_width() // 2)
                )
                text_rect = (
                    (col * center_multiplier),  # x = center - half of text width
                    (row * center_multiplier),  # y = center - half of text height
                )
                surface.blit(text_surface, text_rect)

    def __generate_squares(self) -> tuple[tuple[Square, ...], ...]:
        return tuple(
            tuple(
                (Square(row=row, col=col, is_bomb=self.bombs[row, col] != 0))
                for row in range(self.squares_amount)
            )
            for col in range(self.squares_amount)
        )

    # def create_board(self):
    #     for row in range(SQ_AMOUNT):
    #         for col in range(SQ_AMOUNT):
    #             if not (row, col) in self.bombs:
    #                 count = self.count_bombs_around(row, col)
    #                 self.squares[row][col] = Square(row=row, col=col, count=count)

    def generate_bombs(self):
        while len(self.bombs) != self.bombs_amount:
            bomb_row, bomb_col = random.randint(
                0, Config.SQ_AMOUNT - 1
            ), random.randint(0, Config.SQ_AMOUNT - 1)
            self.bombs.add((bomb_row, bomb_col))
            self.squares[bomb_row][bomb_col] = Square(
                row=bomb_row, col=bomb_col, count=0, is_bomb=True
            )

    def count_bombs_around(self, row: int, col: int):
        count = 0
        for c_row in range(
            row if row - 1 < 0 else row - 1,
            row + 1 if row + 2 > self.squares_amount else row + 2,
        ):
            for c_col in range(
                col if col - 1 < 0 else col - 1,
                col + 1 if col + 2 > self.squares_amount else col + 2,
            ):
                if (
                    self.squares[c_row][c_col].__class__ is Square
                    and self.squares[c_row][c_col].is_bomb
                ):
                    count += 1

        return count

    def place_flag(self, surface):
        for row in self.__squares:
            for square in row:
                if square.with_flag:
                    rect = (
                        square.col * Config.SQ_SIZE,
                        square.row * Config.SQ_SIZE,
                        Config.SQ_SIZE,
                        Config.SQ_SIZE,
                    )
                    pg.draw.rect(surface, Config.FLAG_COLOR, rect)

    def open_few(self, row: int, col: int):
        for c_row in range(
            row if row - 1 < 0 else row - 1,
            row + 1 if row + 2 > Config.SQ_AMOUNT else row + 2,
        ):
            for c_col in range(
                col if col - 1 < 0 else col - 1,
                col + 1 if col + 2 > Config.SQ_AMOUNT else col + 2,
            ):
                square = self.squares[c_row][c_col]

                if square.is_visible:
                    continue

                square.is_visible = True

                if not square.count:
                    self.open_few(c_row, c_col)

    def draw_bombs(self, surface):
        for row, col in self.bombs:
            rect = (
                col * Config.SQ_SIZE,
                row * Config.SQ_SIZE,
                Config.SQ_SIZE,
                Config.SQ_SIZE,
            )
            pg.draw.rect(surface, Config.BOMB_COLOR, rect)

    # def gameover_text(self, surface):
    #     ctime = time.time()

    #     text_surface = self.font.render("Game over!", False, (255, 255, 255), "red")

    #     if ctime - self.timer > 2:
    #         text_surface = self.font.render(
    #             'Press "R" to play again', False, (255, 255, 255), "red"
    #         )

    #     surface.blit(
    #         text_surface,
    #         (
    #             (Config.WIDTH // 2) - (text_surface.get_width() // 2),
    #             (Config.HEIGHT // 2) - (text_surface.get_height() // 2),
    #         ),
    #     )

    # def win_text(self, surface):
    #     text_surface = self.font.render("You won!", False, (255, 255, 255), "green")
    #     surface.blit(
    #         text_surface,
    #         (
    #             (Config.WIDTH // 2) - (text_surface.get_width() // 2),
    #             (Config.HEIGHT // 2) - (text_surface.get_height() // 2),
    #         ),
    #     )
