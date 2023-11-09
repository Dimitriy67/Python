# Реализуйте класс RandomLooper.
# При создании экземпляра класс должен принимать произвольное количество позиционных аргументов,
# каждый из которых является итерируемым объектом.
# Экземпляр класса RandomLooper должен являться итератором, который генерирует в случайном порядке все элементы
# всех итерируемых объектов, переданных в конструктор, а затем возбуждает исключение StopIteration.

import random


class RandomLooper:
    def __init__(self, *iterables):
        self.elements = [element for iterable in iterables for element in iterable]
        random.shuffle(self.elements)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.elements:
            raise StopIteration
        return self.elements.pop()
