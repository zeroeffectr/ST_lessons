from Engine import Engine


class GameTwo(Engine):

    def start_game(self):
        print("Загадай число от 1 до 10 в уме.")
        print("Отвечай компьютеру символами <, > или =")

        while True:
            print(f"Твое число {self.guess}?")
            self.user_input = input("Ответ: ")

            if self.user_input == "<":
                if not self.validation():
                    break
                self.max_num = self.guess - 1
                self.guess = self.min_num + (self.max_num - self.min_num) // 2
            elif self.user_input == ">":
                if not self.validation():
                    break
                self.min_num = self.guess + 1
                self.guess = self.min_num + (self.max_num - self.min_num) // 2
            elif self.user_input == "=":
                print(f"Было легко, твоё число: {self.guess}")
                break
            else:
                print("Некорректный ввод, используй символы <, > или =")


game = GameTwo(1,10)
game.start_game()
