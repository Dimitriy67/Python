# Реализуйте класс IPAddress, описывающий IP-адрес. 
# При создании экземпляра класс должен принимать один аргумент:
# ipaddress — IP-адрес, представленный в одном из следующих вариантов:
# строка из четырех целых чисел, разделенных точками
# список или кортеж из четырех целых чисел
# Экземпляр класса IPAddress должен иметь следующее формальное строковое представление:
# IPAddress('<IP-адрес в виде четырех целых чисел, разделенных точками>')
# И следующее неформальное строковое представление:
# <IP-адрес в виде четырех целых чисел, разделенных точками>

from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        raise TypeError('Неверный формат данных')

    @__init__.register(str)
    def _from_str(self, ipaddress):
        self.ipaddress = str(ipaddress)

    @__init__.register(list)
    @__init__.register(tuple)
    def _from_list_or_tuple(self, ipaddress):
        self.ipaddress = ".".join(map(str, ipaddress))

    def __str__(self):
        return self.ipaddress

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.ipaddress}')"

