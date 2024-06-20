
class Square:
    def __init__(self, row=0, col=0, piece=None) -> None:
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self) -> bool:
        return self.piece != None
    