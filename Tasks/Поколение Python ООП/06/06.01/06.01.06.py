# Реализуйте класс Peekable.
# При создании экземпляра класс должен принимать один аргумент:
# iterable — итерируемый объект
# Экземпляр класса Peekable должен являться итератором, который генерирует элементы итерируемого объекта iterable в исходном порядке,
# а затем возбуждает исключение StopIteration.
# Класс Peekable должен иметь один метод экземпляра:\
# peek() — метод, возвращающий следующий элемент итератора аналогично функции next(), но при этом не сдвигающий итератор.
# Если итератор пуст, должно быть возбуждено исключение StopIteration.
# Также метод должен уметь принимать один необязательный аргумент default — объект,
# который будет возвращен вместо возбуждения исключения StopIteration, если итератор пуст

class Peekable:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.curr = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr is not None:
            temp, self.curr = self.curr, None
            return temp
        return next(self.iterable)

    def peek(self, default=StopIteration):
        if self.curr is None:
            if default == StopIteration:
                self.curr = next(self.iterable)
            else:
                try:
                    self.curr = next(self.iterable)
                except StopIteration:
                    return default
        return self.curr
