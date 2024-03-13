from Engine import Engine


class GameOne(Engine):

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


game = GameOne(1, 10)
game.play()
