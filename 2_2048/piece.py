from config import *

class Piece:
    def __init__(self, value=1) -> None:
        self.value = value
        self.color = self.get_color()


    def get_color(self):
        return COLORS[self.value]