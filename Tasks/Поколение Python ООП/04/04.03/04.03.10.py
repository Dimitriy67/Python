# Реализуйте класс Numbers, описывающий изначально пустой расширяемый набор целых чисел.
# При создании экземпляра класс не должен принимать никаких аргументов.
# Класс Numbers должен иметь три метода экземпляра:
# add_number() — метод, принимающий в качестве аргумента целое число и добавляющий его в набор
# get_even() — метод, возвращающий список всех четных чисел из набора
# get_odd() — метод, возвращающий список всех нечетных чисел из набора

class Numbers:
    def __init__(self):
        self.number_list = []

    def add_number(self, n):
        self.number_list.append(n)

    def get_even(self):
        return list(filter(lambda x: not x % 2, self.number_list))

    def get_odd(self):
        return list(filter(lambda x: x % 2, self.number_list))
