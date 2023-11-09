# Реализуйте класс SkipIterator.
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:
# iterable — итерируемый объект
# n — целое неотрицательное число
# Экземпляр класса SkipIterator должен являться итератором, который генерирует элементы итерируемого объекта iterable,
# пропуская по n элементов, а затем возбуждает исключение StopIteration

class SkipIterator:
    def __init__(self, iterable, n):
        self.iterator = iter(iterable)
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        el = next(self.iterator)

        for _ in range(self.n):
            next(self.iterator, None)

        return el
