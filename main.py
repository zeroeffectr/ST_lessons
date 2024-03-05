import random

class Game:
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
        self.secret_number = random.randint(min_num, max_num)
        self.num_attempts = 0

    def user_guess(self):
        while True:
            try:
                guess = int(input("Твоё число - "))
                if guess < self.min_num or guess > self.max_num:
                    raise ValueError
                return guess
            except ValueError:
                print("Фигню вводишь, давай нормально")

    def play(self):
        print(f"Загадано число от {self.min_num} до {self.max_num}, пробуй угадать (перебором вообще кайф)")

        while True:
            guess = self.user_guess()
            self.num_attempts += 1

            if guess < self.secret_number:
                print("Кто такие маленькие числа вообще загадывает? Попробуй больше")
            elif guess > self.secret_number:
                print("Переборщил, бери поменьше")
            else:
                print(f"Поразительно, ты угадал число {self.secret_number} всего за {self.num_attempts} попыток")
                break

game = Game(1, 100)
game.play()