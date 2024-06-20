from random import randint


from config import *
from square import Square
from piece import Piece


class Board:
    def __init__(self) -> None:
        self.squares = [[0, 0, 0, 0] for x in range(ROWS)]
        self.create_board()

    def create_board(self) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square()

        random_row = randint(0, ROWS-1)
        random_col = randint(0, COLS-1)
        self.squares[random_row][random_col] = Square(
            random_row, random_col, Piece())

    def create_random_piece(self):
        while True:
            random_row = randint(0, ROWS-1)
            random_col = randint(0, COLS-1)
            print(random_row, random_col)
            if self.squares[random_row][random_col].has_piece():
                continue
            else:
                self.squares[random_row][random_col] = Square(
                    random_row, random_col, Piece(2))
                break

    def move(self, k: tuple) -> None:
        self.create_random_piece()
        x, y = k
        if x:
            for row in range(ROWS):
                for col in range(COLS):
                    if self.squares[row][col].has_piece():
                        piece = self.squares[row][col]

                        while True:
                            # check if piece moved to the end
                            if x == 1:
                                if piece.col == COLS-1:
                                    break
                            elif x == -1:
                                if piece.col == 0:
                                    break
                            # check if piece there is another piece in range of movement
                            if self.squares[piece.row][piece.col+x].has_piece():
                                break

                            piece.col += x
        elif y:
            for row in range(ROWS):
                for col in range(COLS):
                    if self.squares[row][col].has_piece():
                        piece = self.squares[row][col]

                        while True:
                            # check if piece moved to the end
                            if y == 1:
                                if piece.row == ROWS-1:
                                    break
                            elif y == -1:
                                if piece.row == 0:
                                    break
                            # check if piece there is another piece in range of movement
                            if self.squares[piece.row+y][piece.col].has_piece():
                                break

                            piece.row += y
