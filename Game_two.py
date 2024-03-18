from Engine import Engine
from exceptions import UserException

class GameTwo(Engine):

    def start_game(self):
        print("Загадай число от 1 до 10 в уме.")
        print("Отвечай компьютеру символами <, > или =")

        while True:
            print(f"Твое число {self.guess}?")
            try:
                self.user_input = input("Ответ: ")
                if self.user_input == "<":
                    if not self.validation() or self.guess == self.min_num:
                        raise UserException
                    self.max_num = self.guess - 1
                    self.guess = self.min_num + (self.max_num - self.min_num) // 2
                elif self.user_input == ">":
                    if not self.validation() or self.guess == self.max_num:
                        raise UserException
                    self.min_num = self.guess + 1
                    self.guess = self.min_num + (self.max_num - self.min_num) // 2
                elif self.user_input == "=":
                    print(f"Было легко, твоё число: {self.guess}")
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Некорректный ввод, используй символы <, > или =")
            except UserException:
                print("Определись с числом, дружище. Я так играть не буду")
                break



game = GameTwo(1,10)
game.start_game()
