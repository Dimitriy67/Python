# Реализуйте класс Formatter. 
# При создании экземпляра класс не должен принимать никаких аргументов.
# Класс Formatter должен иметь один статический метод:
# format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict и выводящий информацию о переданном объекте в формате, зависящем от его типа. 
# Если переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:
# Аргумент переданного типа не поддерживается

from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(obj):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @format.register(int)
    @staticmethod
    def _from_int(obj):
        print(f'Целое число: {obj}')

    @format.register(float)
    @staticmethod
    def _from_float(obj):
        print(f'Вещественное число: {obj}')

    @format.register(tuple)
    @staticmethod
    def _from_tuple(obj):
        print(f'Элементы кортежа: {", ".join(map(str, obj))}')

    @format.register(list)
    @staticmethod
    def _from_list(obj):
        print(f'Элементы списка: {", ".join(map(str, obj))}')

    @format.register(dict)
    @staticmethod
    def _from_dict(obj):
        print(f'Пары словаря: {", ".join(map(str, obj.items()))}')
