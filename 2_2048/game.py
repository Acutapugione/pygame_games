import pygame

from config import *
from board import Board

class Game:
    def __init__(self) -> None:
        self.board = Board()
        

    def show_board(self, screen) -> None:

        for row in range(ROWS):
            for col in range(COLS):
                rect = (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, SQUARE_COLOR, rect, width=GAP)

    def show_numbers(self, screen) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    square = self.board.squares[row][col]

                    rect = (square.col * SQUARE_SIZE + GAP, square.row * SQUARE_SIZE + GAP, SQUARE_SIZE - (GAP*2), SQUARE_SIZE - (GAP*2))
                    pygame.draw.rect(screen, square.piece.color, rect)
