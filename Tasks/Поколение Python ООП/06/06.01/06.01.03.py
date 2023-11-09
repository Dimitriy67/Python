# Реализуйте класс AttrsIterator. При создании экземпляра класс должен принимать один аргумент:
# obj — произвольный объект
# Экземпляр класса AttrsIterator должен являться итератором, который генерирует все атрибуты объекта obj в виде кортежей
# из двух элементов, первый из которых представляет имя атрибута, второй — значение атрибута.

class AttrsIterator:
    def __init__(self, obj):
        self._obj = list(obj.__dict__.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self._obj):
            raise StopIteration
        return self._obj[self.index]