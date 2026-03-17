import board
import constants as c


class Game:
    def __init__(self, chose_stone, com_level):
        self.b = board.Board()
        self.PLAYER_TURN = chose_stone if chose_stone == 1 else -1
        self.COM_TURN = self.PLAYER_TURN * -1
        self.COM_LEVEL = com_level
        self.current_turn = 1

    def play_game(self) -> str:
        pass_count = 0

        while pass_count >= 2:
            valid_squares = self.check_squares()

            if range(valid_squares) > 0:
                self.draw_board()
                self.player_move() if self.current_turn == self.PLAYER_TURN else self.com_move1
                self.reverse_stone()
            else:
                pass_count += 1

        return self.end_game()

    def check_squares(self) -> list:
        valid_squares = []
        return valid_squares

    def draw_board(self):
        print("＋ー" * c.ROWS + "＋")

        for y in range(c.COLS):
            for x in range(c.ROWS):
                status = (
                    "⚫️"
                    if self.b.b[y + 1][x + 1] == 1
                    else "⚪️"
                    if self.b.b[y + 1][x + 1] == -1
                    else "　"
                )

                print("｜" + status, end="")

            print("｜")
            print("＋ー" * c.ROWS + "＋")

    def player_move(self) -> list:
        square = []

        print("打つマスを選択します。")

        for i in range(c.AXES):
            square.append(self.input_coord(c.AXES[i]))

        return square

    def input_coord(self, axis) -> int:
        while (coord := int(input(axis + ">"))) not in range(1, 9):
            print("無効な値です。1~8の範囲で入力してください。")

        return coord

    def com_move1(self, valid_squares) -> list:
        square = []
        return square

    def com_move2(self, valid_squares) -> list:
        square = []
        return square

    def reverse_stones(self):
        return

    def end_game(self) -> str:
        print("対局が終了しました。")

        stones = self.count_stones()

        if stones[0] > stones[1]:
            if self.PLAYER_TURN == c.BS.get("BLACK"):
                return c.RESULTS.get("WIN")
            else:
                return c.RESULTS.get("LOSE")
        elif stones[0] < stones[1]:
            if self.PLAYER_TURN == c.BS.get("BLACK"):
                return c.RESULTS.get("LOSE")
            else:
                return c.RESULTS.get("WIN")
        else:
            return c.RESULTS.get("DRAW")

    def count_stones(self) -> list:
        bc = wc = 0

        for y in range(1, c.COLS + 1):
            for x in range(1, c.ROWS + 1):
                if self.b.b[y][x] == c.BS.get("BLACK"):
                    bc += 1
                elif self.b.b[y][x] == c.BS.get("WHITE"):
                    wc += 1

        return [bc, wc]
