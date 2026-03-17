import game
import constants as c


class Main:
    def __init__(self):
        self.player_stone = 0
        self.stones
        self.com_level = 0
        self.result = ""

    def main(self):
        print("ようこそ、ここではリバーシをプレイできます。")

        while True:
            if (_ := input("プレイしますか？[y/n]>")) != "y":
                print("終了します。")
                break

            self.player_stone = self.choose(c.PROMPTS.get("STONE"))
            self.com_level = self.choose(c.PROMPTS.get("LEVEL"))

            g = game.Game(self.player_stone, self.com_level)
            self.result = g.play_game()
            print(self.result)

            print("もう一度", end="")

    def choose(self, prompt) -> int:
        while (chose := int(input(prompt))) != 1 or 2:
            print("無効な値です。")

        return chose


if __name__ == "__main__":
    m = Main
    m.main()
