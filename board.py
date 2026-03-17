import constants as c


class Board:
    def __init__(self):
        self.b = [[0 for _ in range(c.ROWS + 2)] for _ in range(c.COLS + 2)]

        self.b[4][5] = self.b[5][4] = c.BS.get("BLACK")
        self.b[4][4] = self.b[5][5] = c.BS.get("WHITE")

        for i in range(c.ROWS + 2):
            self.b[i][0] = c.BS.get("WALL")
            self.b[0][i] = c.BS.get("WALL")
            self.b[i][c.ROWS + 1] = c.BS.get("WALL")
            self.b[c.COLS + 1][i] = c.BS.get("WALL")
