# Реализуйте класс Scales, описывающий весы с двумя чашами. При создании экземпляра класс не должен принимать никаких аргументов.

class Scales:
    def __init__(self):
        self.balance = 0

    def add_right(self, mass):
        self.balance += mass

    def add_left(self, mass):
        self.balance -= mass

    def get_result(self):
        if self.balance > 0:
            return 'Правая чаша тяжелее'
        if self.balance < 0:
            return 'Левая чаша тяжелее'
        return 'Весы в равновесии'
