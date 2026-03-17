import board


class Game:
    def __init__(self, player_turn):
        self.b = board.Board()
        self.PLAYER_TURN = player_turn
        self.COM_TURN = self.PLAYER_TURN * -1
        self.current_turn = 1

    def draw_board(self):
        print("＋ー" * self.b.ROWS + "＋")

        for y in range(self.b.COLS):
            for x in range(self.b.ROWS):
                status = (
                    "⚫️"
                    if self.b.board[y + 1][x + 1] == 1
                    else "⚪️" if self.b.board[y + 1][x + 1] == -1 else "　"
                )

                print("｜" + status, end="")

            print("｜")
            print("＋ー" * self.b.ROWS + "＋")
