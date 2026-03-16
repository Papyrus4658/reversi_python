# 列と行
rows = cols = 8

# 盤の状態を示す値
bs = {"BLACK": 1, "WHITE": -1, "SPACE": 0, "WALL": 9}

# 盤
board = [[0 for _ in range(rows + 2)] for _ in range(cols + 2)]

# 初期配置
board[4][5] = board[5][4] = bs.get("BLACK")
board[4][4] = board[5][5] = bs.get("WHITE")

for i in range(rows + 2):
    board[i][0] = 9
    board[0][i] = 9
    board[i][rows + 1] = 9
    board[cols + 1][i] = 9

print("＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋")

for y in range(cols):
    for x in range(rows):
        status = (
            "黒"
            if board[y + 1][x + 1] == 1
            else "白" if board[y + 1][x + 1] == -1 else "　"
        )

        print("｜" + status, end="")
    print("｜")
    print("＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋")
