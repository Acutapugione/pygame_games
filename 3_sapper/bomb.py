from position import Position
import random
from config import Config
import numpy
import time

from square import Square


class Bomb: ...


class BombGenerator:
    def __init__(
        self,
        mss_size: tuple[
            int,
            int,
        ],
        bombs_count: int = Config.BOMBS_AMOUNT,
        bomb_chance: float | int = Config.BOMBS_CHANCE,
    ) -> None:
        self.rows, self.cols = mss_size
        self.bombs_count = bombs_count
        self.bomb_chance = bomb_chance
        self.bombs = []

    def generate(self):
        rng = numpy.random.RandomState([int(time.time())] * 55)
        array = numpy.zeros(
            (self.rows, self.cols),
            dtype=Square,
        )
        coords = []
        while len(coords) < self.bombs_count:
            row = rng.randint(0, self.rows)
            col = rng.randint(0, self.cols)
            if (row, col) not in coords:
                coords.append((row, col))
        for row, col in coords:
            array[row, col] = Square(row=row, col=col, count=0, is_bomb=True)
        return array
