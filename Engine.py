from random import randint


class Engine:

    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
        self.secret_number = randint(min_num, max_num)
        self.num_attempts = 0
        self.guess = randint(1, 10)

# Game_one
    def user_guess(self):
        while True:
            try:
                guess = int(input("Твоё число - "))
                if guess < self.min_num or guess > self.max_num:
                    raise ValueError
                return guess
            except ValueError:
                print("Фигню вводишь, давай нормально")

# Game_two

    def validation(self):
        if self.min_num != self.max_num:
            if 1 <= self.max_num - 1 <= 10 and 1 <= self.min_num + 1 <= 10:
                return True
        else:
            return False
