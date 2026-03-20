import game
import constants as c


class Main:
    def __init__(self):
        self.player_stone = 0
        self.com_level = 0
        self.result = ""

    def main(self):
        print("ようこそ、ここではリバーシをプレイできます。")

        while (_ := input("プレイしますか？[y/n]>")) == "y":
            self.player_stone = self.choose(c.PROMPTS.get("STONE"))
            self.com_level = self.choose(c.PROMPTS.get("LEVEL"))

            g = game.Game(self.player_stone, self.com_level)
            self.result = g.play_game()
            print(self.result)

            print("もう一度", end="")

        print("終了します。")

    def choose(self, prompt) -> int:
        chose = 0

        while True:
            if (chose := int(input(prompt))) == 1 or 2:
                return chose

            print("無効な値です。")


if __name__ == "__main__":
    m = Main()
    m.main()
