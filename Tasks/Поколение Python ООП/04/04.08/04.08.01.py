# Вам доступен класс Processor. При создании экземпляра класс не принимает никаких аргументов.
# Класс Processor имеет один статический метод:
# process() — метод, который принимает в качестве аргумента произвольный объект, преобразует его в зависимости от его типа и возвращает полученный результат.
# Если тип переданного объекта не поддерживается методом, возбуждается исключение TypeError с текстом:
# Аргумент переданного типа не поддерживается

from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(int)
    @process.register(float)
    @staticmethod
    def from_int(data):
        return data * 2

    @process.register(str)
    @staticmethod
    def from_str(data):
        return data.upper()

    @process.register(list)
    @staticmethod
    def from_list(data):
        return sorted(data)

    @process.register(tuple)
    @staticmethod
    def from_tuple(data):
        return tuple(sorted(data))
