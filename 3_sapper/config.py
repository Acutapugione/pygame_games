import sys


class Config:
    SQ_AMOUNT = 20

    WIDTH, HEIGHT = (800 // SQ_AMOUNT) * SQ_AMOUNT, (800 // SQ_AMOUNT) * SQ_AMOUNT
    SQ_SIZE = WIDTH // SQ_AMOUNT
    BOMBS_AMOUNT = SQ_AMOUNT**2 // 10

    BG_COLOR = (107, 101, 100)  # gray
    SQUARE_COLOR = (179, 176, 173)  # light gray
    SQUARE_COLOR_VISIBLE = (125, 122, 120)  # dark gray (border)
    BOMB_COLOR = (184, 38, 9)  # red
    FLAG_COLOR = (242, 122, 27)  # orange

    FONT_SIZE = SQ_SIZE
    FONT_FAMILY = "Comic Sans MS"


# sys.setrecursionlimit(999999999)
