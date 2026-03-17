# # 列と行
# ROWS = COLS = 8

# # 盤の状態を示す値
# BS = {"BLACK": 1, "WHITE": -1, "SPACE": 0, "WALL": 9}

# # 盤
# board = [[0 for _ in range(ROWS + 2)] for _ in range(COLS + 2)]

# # 初期配置
# board[4][5] = board[5][4] = BS.get("BLACK")
# board[4][4] = board[5][5] = BS.get("WHITE")

# for i in range(ROWS + 2):
#     board[i][0] = 9
#     board[0][i] = 9
#     board[i][ROWS + 1] = 9
#     board[COLS + 1][i] = 9

# print("＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋")

# for y in range(COLS):
#     for x in range(ROWS):
#         status = (
#             "黒"
#             if board[y + 1][x + 1] == 1
#             else "白" if board[y + 1][x + 1] == -1 else "　"
#         )

#         print("｜" + status, end="")
#     print("｜")
#     print("＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋")


class Board:
    def __init__(self):
        self.ROWS = self.COLS = 8
        self.BS = {"BLACK": 1, "WHITE": -1, "SPACE": 0, "WALL": 9}
        self.board = [[0 for _ in range(self.ROWS + 2)] for _ in range(self.COLS + 2)]

        self.board[4][5] = self.board[5][4] = self.BS.get("BLACK")
        self.board[4][4] = self.board[5][5] = self.BS.get("WHITE")

        for i in range(self.ROWS + 2):
            self.board[i][0] = self.BS.get("WALL")
            self.board[0][i] = self.BS.get("WALL")
            self.board[i][self.ROWS + 1] = self.BS.get("WALL")
            self.board[self.COLS + 1][i] = self.BS.get("WALL")
