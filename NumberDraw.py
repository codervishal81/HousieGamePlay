import random

class NumberDraw:
    def __init__(self, lower, upper) -> None:
        self.number_pool = [x for x in range(lower, upper + 1)]

    def draw(self):
        number = random.choice(self.number_pool)
        self.number_pool.remove(number)
        return number

    def is_number_available(self):
        return len(self.number_pool) > 0
        
