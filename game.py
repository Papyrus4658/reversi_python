import board
import constants as c
import random
import time

import pprint


class Game:
    def __init__(self, chose_stone, com_level):
        self.b = board.Board()
        self.PLAYER_TURN = chose_stone if chose_stone == 1 else -1
        self.COM_TURN = self.PLAYER_TURN * -1
        self.COM_LEVEL = com_level
        self.current_turn = 1

    def play_game(self) -> str:
        pass_count = 0

        while pass_count < 2:
            valid_squares = self.check_squares()

            if len(valid_squares) > 0:
                self.draw_board()

                self.reverse_stones(
                    self.player_move(valid_squares)
                    if self.current_turn == self.PLAYER_TURN
                    else self.com_move1(valid_squares)
                )

                pass_count = 0
                self.current_turn *= -1
            else:
                pass_count += 1

        return self.end_game()

    def check_squares(self) -> list:
        valid_squares = []

        for y in range(1, c.COLS + 1):
            for x in range(1, c.ROWS + 1):
                if self.b.b[y][x] == c.BS.get("SPACE"):
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            next_y = y + i
                            next_x = x + j

                            if self.b.b[next_y][next_x] == self.current_turn * -1:
                                while True:
                                    next_y += i
                                    next_x += j

                                    if self.b.b[next_y][next_x] == self.current_turn:
                                        valid_squares.append([y, x])
                                        break
                                    elif self.b.b[next_y][next_x] == c.BS.get("SPACE"):
                                        break
                                    elif self.b.b[next_y][next_x] == c.BS.get("WALL"):
                                        break
                                    elif (
                                        self.b.b[next_y][next_x]
                                        == self.current_turn * -1
                                    ):
                                        continue

        return valid_squares

    def draw_board(self):
        print("　　１　２　３　４　５　６　７　８")
        print("　＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋")

        for y in range(c.COLS):
            print(" " + str(y + 1), end="")

            for x in range(c.ROWS):
                status = (
                    "黒"
                    if self.b.b[y + 1][x + 1] == 1
                    else "白"
                    if self.b.b[y + 1][x + 1] == -1
                    else "　"
                )

                print("｜" + status, end="")

            print("｜")
            print("　＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋")

    def player_move(self, valid_squares) -> list:
        is_thinking = True
        print("あなたの番です。")
        print("打つマスを選択します。")

        while is_thinking:
            coord = []

            for i in c.AXES:
                coord.append(self.input_coord(i))
                pprint.pprint(coord)

            for i in valid_squares:
                if coord == i:
                    is_thinking = False

        return coord

    def input_coord(self, axis) -> int:
        while True:
            try:
                coord = int(input(axis + ">"))

                if coord >= 1 and coord <= 8:
                    print(coord)
                    return coord
                else:
                    print("無効な値です。1~8の範囲で入力してください。")
            except ValueError:
                print("無効な値です。1~8の範囲で入力してください。")

        return coord

    def com_move1(self, valid_squares) -> list:
        print("COMの番です。")
        time.sleep(1)
        coord = random.choice(valid_squares)
        return coord

    def com_move2(self, valid_squares) -> list:
        print("COMの番です。")
        time.sleep(1)
        coord = []
        return coord

    def reverse_stones(self, coord):
        y = coord[0]
        x = coord[1]

        for i in range(-1, 2):
            for j in range(-1, 2):
                next_y = y + i
                next_x = x + j

                if self.b.b[next_y][next_x] == self.current_turn * -1:
                    while True:
                        next_y += i
                        next_x += j

                        if self.b.b[next_y][next_x] == self.current_turn:
                            pre_y = next_y - 1
                            pre_x = next_x - 1

                            while pre_y != y and pre_x != x:
                                self.b.b[pre_y][pre_x] = self.current_turn
                                pre_y = next_y - i
                                pre_x = next_x - j

                            break
                        elif self.b.b[next_y][next_x] == c.BS.get("SPACE"):
                            break
                        elif self.b.b[next_y][next_x] == c.BS.get("WALL"):
                            break
                        elif self.b.b[next_y][next_x] == self.current_turn * -1:
                            continue

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
