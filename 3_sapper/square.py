class Square:
    def __init__(self, row=0, col=0, count=0, is_bomb=False) -> None:
        self.row = row
        self.col = col
        self.count = count
        self.is_bomb = is_bomb
        self.is_visible = False
        self.with_flag = False
    